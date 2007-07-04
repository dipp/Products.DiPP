from Products.Archetypes.public import *
from config import PROJECTNAME
import Permissions

class FedoraMultimedia(BaseContent):
    """temporäre Dateien für das Fedora Repository"""
    schema = BaseSchema + Schema((
        ImageField('Image',
                required=0,
                widget=ImageWidget(label='Image',description='Bild Datei')
        ),
        StringField('PID',
                required=1,
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15')
        ),
        StringField('DsID',
                required=1,
                widget=StringWidget(label='DsID',description='Datastream Identifier',size='15')
        )
    ))

    content_icon = "fedoraimage_icon.gif"

    actions = (
        { 'id': 'edit',
          'name': 'Edit',
          'action': 'fedoraimage_edit_form',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'view',
          'name': 'View',
          'action': 'fedoramultimedia_view',
          'permissions': (Permissions.VIEW_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'preview',
          'name': 'Preview',
          'action': 'fedoraimage_preview',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'references',
          'name': 'References',
          #'action': 'fedoradocument_view',
          'visible': 0,
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'versions',
          'name': 'Versions',
          'action': 'fedoraimage_versions',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
    )
registerType(FedoraMultimedia,PROJECTNAME)
