# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from Products.DiPP.config import PROJECTNAME
from Products.DiPP import Permissions

class FedoraXML(BaseContent):
    """stores the DocBOOK XML Files"""
    
    schema = BaseSchema + Schema((
        TextField('body',
                searchable=1,
                required=0,
                primary=1,
                allowable_content_types=('text/xml'),
                widget=TextAreaWidget(label='Body Content')
        ),
        StringField('PID',
                required=1,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible=-1
                ),
                index='FieldIndex:brains'
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
    content_icon = "fedoraxml_icon.gif"

    actions = (
          
        { "id": "view",
          "name": "View",
          "action": "string:${object_url}/fedoraxml_view",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          },
          
        { "id": "preview",
          "name": "Preview",
          "action": "string:${object_url}/fedoraxml_preview",
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
registerType(FedoraXML,PROJECTNAME)
