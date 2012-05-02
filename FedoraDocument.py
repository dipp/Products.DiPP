# -*- coding: utf-8 -*-
# The Fedoradocument ContentType
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

from AccessControl import ClassSecurityInfo
from zope.interface import implements, Interface

from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName

from Products.DiPP.config import PROJECTNAME
from Products.DiPP.interfaces import IFedoraDocument
from Products.DiPP import Permissions

FedoraDocumentSchema = BaseSchema + Schema((
        TextField('body',
                searchable=1,
                required=0,
                primary=1,
                allowable_content_types=('text/html',
                                   'text/structured',
                                   'text/plain',
                                   'text/xml'),
                widget=RichWidget(label='Body Content')
        ),
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible=-1
                    ),
                index='FieldIndex:brains:schema'
        ),
        StringField('DsID',
                required=0,
                widget=StringWidget(
                    label='DsID',
                    description='Datastream Identifier',
                    size='15',
                    visible=-1)
        ),
        StringField('MIMEType',
                required=0,
                widget=StringWidget(
                    label='MIMEType',
                    description='MIMEType of Object',
                    size='25',
                    visible={'edit':'invisible','view':'visible'}
                    )
        ),
    ),
    marshall=PrimaryFieldMarshaller(),
    )


class FedoraDocument(BaseContent):
    """store text files in the repository"""

    security = ClassSecurityInfo()
    implements(IFedoraDocument)
    
    schema = FedoraDocumentSchema
    
    _at_rename_after_creation = True

    
    def at_post_create_script(self):
        """ when a document is not converted but added manually via the "add article"
            menu, it does not have PID and DsID. This method takes care of creating a
            a digital object for the page.
        """

        fedora = getToolByName(self, 'fedora')
        article = self.getParentNode()
        PID = fedora.getContentModel(PID=article.PID, Type='HTML')
        MIMEType = "text/html"
        Label = self.id
        Location = article.absolute_url() + "/dummy.html"
        if Location.startswith('https'):
            Location = Location.replace('https','http',1)

        if self.DsID == '' and self.PID == '':
            DsID = fedora.addDatastream(None,PID,Label,MIMEType,Location,"M","","","A")
            self.setPID(PID)
            self.setDsID(DsID)

        self.reindexObject()
        

registerType(FedoraDocument,PROJECTNAME)
