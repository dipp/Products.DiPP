# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName
from AccessControl import ClassSecurityInfo
from zLOG import LOG, ERROR, INFO
import Permissions
from config import PROJECTNAME

class FedoraDocument(BaseContent):
    """store text files in the repository"""

    security = ClassSecurityInfo()
    schema = BaseSchema + Schema((
        TextField('body',
                searchable=1,
                required=0,
                primary=1,
                allowable_content_types=('text/plain',
                                   'text/structured',
                                   'text/html',
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
                widget=StringWidget(label='MIMEType',description='MIMEType of Object',size='25')
        ),
    ),
    marshall=PrimaryFieldMarshaller(),
    )
    
    _at_rename_after_creation = True
    content_icon = "fedoradocument_icon.gif"

    actions = (
        { "id": "view",
          "name": "View",
          "action": "string:${object_url}/fedoradocument_view",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          },
          
        { "id": "preview",
          "name": "Preview",
          "action": "string:${object_url}/fedoradocument_preview",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { "id": "references",
          "name": "References",
          "visible": 0,
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { "id": "versions",
          "name": "Versions",
          "action": "string:${object_url}/fedoradocument_versions",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
         { "id": "citation",
          "name": "Citation and Metadata",
          "action": "string:${object_url}/metadata",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"document_actions",
          },

    )
    
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

        if self.DsID == '' and self.PID == '':
            DsID = fedora.addDatastream(None,PID,Label,MIMEType,Location,"M","","","A")
            self.setPID(PID)
            self.setDsID(DsID)

        self.reindexObject()
        

registerType(FedoraDocument,PROJECTNAME)
