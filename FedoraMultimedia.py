# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from config import PROJECTNAME
import Permissions

class FedoraMultimedia(BaseContent):
    """Multimedia files (Images, PDF, Movies) for storing in Fedora"""
    
    schema = BaseSchema + Schema((
        FileField('File',
                required=0,
                primary=1,
                widget=FileWidget(label='File',description='Multimedia file')
        ),
        StringField('PID',
                required=0,
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15')
        ),
        StringField('DsID',
                required=0,
                widget=StringWidget(label='DsID',description='Datastream Identifier',size='15')
        )
    ),
    marshall=PrimaryFieldMarshaller(),
    )
    content_icon = "fedoramultimedia_icon.gif"
    
    actions = (
        { "id": "edit",
          "name": "Edit",
          "action": "string:${object_url}/fedoramultimedia_edit_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { "id": "view",
          "name": "View",
          "action": "string:${object_url}/fedoramultimedia_view",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          },
          
        { "id": "preview",
          "name": "Preview",
          "action": "string:${object_url}/fedoramultimedia_preview",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { "id": "references",
          "name": "References",
          #"action": "string:${object_url}/fedoradocument_view",
          "visible": 0,
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { "id": "versions",
          "name": "Versions",
          "action": "string:${object_url}/fedoramultimedia_versions_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
    )
registerType(FedoraMultimedia,PROJECTNAME)
