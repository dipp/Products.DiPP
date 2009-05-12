# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from Products.CMFCore.utils import getToolByName

from config import PROJECTNAME
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.utils import getToolByName
from AccessControl import ClassSecurityInfo
import Permissions
from zLOG import LOG, ERROR, INFO
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

class FedoraMultimedia(BrowserDefaultMixin, BaseContent):
    """Multimedia files (Images, PDF, Movies) for storing in Fedora"""
    
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(BaseContent,'__implements__',()),)
    
    schema = BaseSchema + Schema((
        FileField('File',
                required=0,
                primary=1,
                widget=FileWidget(
                    label='File',
                    description='Multimedia file'
                )
        ),
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='Persistent Identifier (PID)',
                    description='The PID of this digital object as given by the repository software. DO NOT EDIT.',
                    size='15'
                )
        ),
        StringField('DsID',
                required=0,
                widget=StringWidget(
                    label='Datastream Identifier (DsID)',
                    description='The Datastream Identifier. DO NOT EDIT.',
                    size='15')
        ),
        StringField('MMType',
                required=0,
                widget=SelectionWidget(
                    label='Multimedia type',
                    description='You can select, wether this file should be listed separatly in one of the categories below.'
                ),
                multiValued=0,
                default = "",
                index="FieldIndex:brains",
                vocabulary = "getTypeOfList"
        )
    ),
    marshall=PrimaryFieldMarshaller(),
    )
    immediate_view = 'view'
    default_view = 'view'
    suppl_views = ('base_view', 'mmmp3_view', 'mmimage_view', 'mmflv_view')
    content_icon = "fedoramultimedia_icon.gif"
    
    inlineMimetypes= ('application/msword',
                      'application/vnd.ms-excel',
                      'application/vnd.ms-powerpoint',
                      'application/rtf',
                      'application/pdf')

    actions = (
        { "id": "edit",
          "name": "Edit",
          "action": "string:${object_url}/fedoramultimedia_edit_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
        },
        #{ "id": "preview",
        #  "name": "Preview",
        #  "action": "string:${object_url}/preview",
        #  "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
        #  },
          
        { "id": "references",
          "name": "References",
          "visible": 0,
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { "id": "versions",
          "name": "Versions",
          "action": "string:${object_url}/fedoramultimedia_versions_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
    )

    security = ClassSecurityInfo()

    security.declareProtected(View, 'index_html')
    def index_html(self, REQUEST=None, RESPONSE=None):
        """ fetch a file from the repository
        """
        
        fedora = getToolByName(self, 'fedora')
        PID = self.PID
        DsID = self.DsID
        data =  fedora.accessMultiMedia(PID,DsID,None)
        stream = data['stream']
        MIMEType =data['MIMEType']
        RESPONSE.setHeader('Content-Type', MIMEType)
        LOG('DiPP', INFO, MIMEType)
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
