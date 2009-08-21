# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from config import PROJECTNAME
import Permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName
from zLOG import LOG, ERROR, INFO

class FedoraHierarchie(BrowserDefaultMixin, OrderedBaseFolder):
    """
    Hierarchical Object representing an issue or volume
    """
    
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)
    
    schema = BaseSchema + Schema((
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='PID',
                    description='Persistent Identifier',
                    size='15',
                    visible={'edit':'invisible','view':'visible'}
                ),
                index='FieldIndex:brains:schema'
        ),

        TextField('description',
            required=0,
            widget=TextAreaWidget(label="description")
        ),

        StringField('MetaType',
                required=0,
                vocabulary=('volume','series','category','topic','article','congress','other'),
                widget=SelectionWidget(label='MetaType',description='Art des Containers',size='15')
        )
    ))
    _at_rename_after_creation = True
    allowed_content_types = ('FedoraHierarchie','FedoraArticle','Document','Image')
    immediate_view = 'base_view'
    default_view = 'issue_contents_view'
    suppl_views = ('base_view', 'issue_contents_view')
    content_icon = 'fedorahierarchie_icon.gif'
    actions = (
        #{ "id": "edit",
        #  "name": "Edit",
        #  "action": "string:${folder_url}/fedorahierarchie_edit_form",
        #  "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
        #  "category":"folder",
        #  },
         
        { "id": "view",
          "name": "View",
          "action": "string:${folder_url}/",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "folderlisting",
          "name": "Folder Listing",
          "action": "string:${folder_url}/folder_listing",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"folder",
          "visible":0,
          },
          
        { "id": "dc",
          "name": "MetaData",
          "action": "string:${folder_url}/fedorahierarchie_meta",
          "visible":0,
          "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
        { "id": "references",
          "name": "References",
          "visible":0,
          #"action": "fedoraarticle_fedora",
          #"permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
          "category":"folder",
          },
          
    )

    def at_post_create_script(self):

        fedora = getToolByName(self, 'fedora')
        isChildOf = self.getParentNode().PID
        MetaType = self.MetaType
        title = self.title
        id = self.id
        AbsoluteURL = self.absolute_url()
        PID = fedora.createNewContainer(isChildOf, MetaType, title, id, AbsoluteURL)
        msg = "isChildOf %s, MetaType %s, title %s, id %s, AbsoluteURL %s" % (isChildOf, MetaType, title, id, AbsoluteURL)
        LOG ('DIPP', INFO, msg)
        self.setPID(PID)
        
    
registerType(FedoraHierarchie,PROJECTNAME)
