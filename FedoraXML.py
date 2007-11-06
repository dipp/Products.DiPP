from Products.Archetypes.public import *
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from config import PROJECTNAME
import Permissions

class FedoraXML(BaseContent):
    """stores the DocBOOK XML Files"""
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
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15')
        ),
        StringField('DsID',
                required=1,
                widget=StringWidget(label='DsID',description='Datastream Identifier',size='15')
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
        { 'id': 'edit',
          'name': 'Edit',
          'action': 'fedoraxml_edit_form',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'view',
          'name': 'View',
          'action': 'fedoraxml_view',
          'permissions': (Permissions.VIEW_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'preview',
          'name': 'Preview',
          'action': 'fedoraxml_preview',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'references',
          'name': 'References',
          'visible': 0,
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
          
        { 'id': 'versions',
          'name': 'Versions',
          'action': 'fedoraxml_versions',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          },
 
    )
registerType(FedoraXML,PROJECTNAME)
