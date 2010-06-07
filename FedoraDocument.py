# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from config import PROJECTNAME
import Permissions

class FedoraDocument(BaseContent):
    """store text files in the repository"""

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
                required=1,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible=-1
                    ),
                index='FieldIndex:brains:schema'
        ),
        StringField('DsID',
                required=1,
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
 
    )
registerType(FedoraDocument,PROJECTNAME)
