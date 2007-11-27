# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from config import PROJECTNAME
from zLOG import LOG, ERROR, INFO
import Permissions

class FedoraArticle(OrderedBaseFolder):
    """
        Folder, that represents a digital Object of the Fedora Database.
        It can only contain FedoraDocument, FedoraImages,...
    """
    schema = BaseSchema + Schema((
        StringField('PID',
                required=1,
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15')
        ),
        #LinesField('Authors',
        #        required=1,
        #        widget=LinesWidget(label='Authors',description='List of author ids')
        #),
        IntegerField('volume',
                required=0,
                widget=IntegerWidget(label='Volume',description='Journal volume')
        ),
        IntegerField('issueNumber',
                required=0,
                widget=IntegerWidget(label='Issue number',description='Number of the issue')
        ),
        IntegerField('order',
                required=0,
                widget=IntegerWidget(label='Order',description='Sorting of Articles')
        )
    ))

    allowed_content_types = ('FedoraDocument','FedoraMultimedia','FedoraXML')
    filter_content_types= 1
    default_view = 'folder_listing'
    view_methods = ('folder_listing','metadata_view')
    content_icon = 'fedoraarticle_icon.gif'
    actions = (
        { "id": "edit",
          "name": "Edit",
          "action": "string:${folder_url}/fedoraarticle_edit_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "view",
          "name": "View",
          "action": "string:${folder_url}/",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "dc",
          "name": "MetaData",
          "visible":0,
          "action": "string:${folder_url}/fedoraarticle_meta",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "qdc",
          "name": "Dublin Core",
          "action": "string:${folder_url}/fedoraarticle_qdc",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "new_file",
          "name": "new file",
          "action": "string:${folder_url}/fedoramultimedia_edit_form",
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
          
        { "id": "references",
          "name": "References",
          "visible":0,
          #"action": "string:${object_url}/fedoraarticle_fedora",
          #"permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
    )
    def _p_resolveConflict(self):
        LOG('DiPP', INFO, 'fix a conflict')
    
registerType(FedoraArticle,PROJECTNAME)
