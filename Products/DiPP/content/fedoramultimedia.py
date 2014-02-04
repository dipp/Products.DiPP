# -*- coding: utf-8 -*-
# The FedoraMultemedia ContentType
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

import logging
from AccessControl import ClassSecurityInfo
from zope.interface import implements, Interface
from textindexng.interfaces import IIndexableContent
from textindexng.content import IndexContentCollector as ICC
from Products.Archetypes.public import *
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.utils import getToolByName
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products. DiPP.config import PROJECTNAME
from Products.DiPP.interfaces import IFedoraMultimedia
from Products.DiPP import Permissions

logger = logging.getLogger(__name__)

FedoraMultimediaSchema = BaseSchema + Schema((
        FileField('File',
                required=0,
                primary=1,
                widget=FileWidget(
                    label='File',
                    description='Multimedia file'
                ),
        ),
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='Persistent Identifier (PID)',
                    description='The PID of this digital object as given by the repository software. DO NOT EDIT.',
                    size='15',
                    visible={'edit':'invisible','view':'visible'}
                ),
        ),
        StringField('DsID',
                required=0,
                widget=StringWidget(
                    label='Datastream Identifier (DsID)',
                    description='The Datastream Identifier. DO NOT EDIT.',
                    size='15',
                    visible={'edit':'invisible','view':'visible'}
                )
        ),
        StringField('MMType',
                required=0,
                widget=SelectionWidget(
                    label='Multimedia type',
                    description='You can select, wether this file should be listed separatly in one of the categories below.'
                ),
                multiValued=0,
                default = "",
                vocabulary = "getTypeOfList"
        )
    ),
    marshall = PrimaryFieldMarshaller()
)

class FedoraMultimedia(BrowserDefaultMixin, BaseContent):
    """Multimedia files (Images, PDF, Movies) for storing in Fedora"""
    
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(BaseContent,'__implements__',()),)
    implements(IIndexableContent, IFedoraMultimedia)
    
    schema = FedoraMultimediaSchema
    
    inlineMimetypes= ('application/msword',
                      'application/vnd.ms-excel',
                      'application/vnd.ms-powerpoint',
                      'application/rtf',
                      'application/pdf')


    security = ClassSecurityInfo()

    def reindex_article(self):
        """ if this object is a pdf version of the article the article has to be 
            reindexed upon changes/creation.
        """
        if self.MMType == "alternative_format":
            article = self.getParentNode()
            article.reindexObject()
            logger.info("reindexed %s" % article.PID)
    

    def at_post_create_script(self):
        """ reindex article folder when pdf flltext is added
        """
        self.reindex_article()
    
    def at_post_edit_script(self):
        """ reindex article folder when pdf flltext is modified
        """
        self.reindex_article()
    
    def indexableContent(self, fields):
        """get the binary datastream from fedora and return in to TextIndexNG
           Only pdf Files should be indexed (via pdftotext) mimetype is checked in plone
           to keep the burdon of fedora when reindexing the portal_catalog
        """
        icc = ICC()
        fedora = getToolByName(self, 'fedora')
        PID = self.PID
        DsID = self.DsID
        MIMEType = self.get_content_type()
        if PID and DsID and MIMEType == "application/pdf": 
            data =  fedora.accessMultiMediaByFedoraURL(PID,DsID,None)
            stream = data['stream']
            logger.info("Fetching %s/%s for indexing." % (PID, DsID))
            icc.addBinary('SearchableText', 
                          stream,
                          MIMEType,
                          'iso-8859-15',
                          None)
            return icc
        return None
        
    security.declareProtected(View, 'index_html')
    def index_html(self, REQUEST=None, RESPONSE=None):
        """ fetch a file from the repository
        """
        
        fedora = getToolByName(self, 'fedora')
        PID = self.PID
        DsID = self.DsID
        data =  fedora.accessMultiMediaByFedoraURL(PID,DsID,None)
        stream = data['stream']
        MIMEType =data['MIMEType']
        RESPONSE.setHeader('Content-Type', MIMEType)
        return stream

    security.declareProtected(View, 'preview')
    def preview(self, REQUEST=None, RESPONSE=None):
        """Download the file
        """
        field = self.getPrimaryField()

        if field.getContentType(self) in self.inlineMimetypes:
            # return the PDF and Office file formats inline
            return ATCTFileContent.index_html(self, REQUEST, RESPONSE)
        # otherwise return the content as an attachment 
        # Please note that text/* cannot be returned inline as
        # this is a security risk (IE renders anything as HTML).
        return field.download(self)

    security.declareProtected(View, 'getTypeOfList')
    def getTypeOfList(self):
        vocabulary = (
            ('','Do not list.'),
            ('alternative_format','Alternative format of the main text.'),
            ('supplementary_material','Supplementary Material')
        )
        return vocabulary

registerType(FedoraMultimedia,PROJECTNAME)
