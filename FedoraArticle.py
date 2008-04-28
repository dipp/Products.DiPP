# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from config import PROJECTNAME
import Permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

class FedoraArticle(BrowserDefaultMixin, OrderedBaseFolder):
    """
        Folder, that represents a digital Object of the Fedora Database.
        It can only contain FedoraDocument, FedoraImages,...
    """
    
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)

    schema = BaseSchema + Schema((
        StringField('PID',
                required=1,
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15')
        )
    ))

    allowed_content_types = ('FedoraDocument','FedoraMultimedia','FedoraXML')
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ('base_view', 'metadata_view', 'splash_screen')
    filter_content_types= 1
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
          
          
        { "id": "references",
          "name": "References",
          "visible":0,
          #"action": "string:${object_url}/fedoraarticle_fedora",
          #"permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
    )
    
registerType(FedoraArticle,PROJECTNAME)
