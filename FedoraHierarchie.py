# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from config import PROJECTNAME
import Permissions
from Products.CMFPlone.interfaces.OrderedContainer import IOrderedContainer
from UpDownMixin import UpDownMixin

#class FedoraHierarchie(BaseFolder):
class FedoraHierarchie(OrderedBaseFolder):
    """
        Folder, that represents a digital Object of the Fedora Database.
        It can only contain FedoraDocument, FedoraImages,...
    """

    schema = BaseSchema + Schema((
        StringField('PID',
                required=0,
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15')
        ),
        StringField('MetaType',
                required=0,
                vocabulary=('volume','series','category','topic','article','congress','other'),
                widget=SelectionWidget(label='MetaType',description='Art des Containers',size='15')
        )
    ))

    allowed_content_types = ('FedoraHierarchie','FedoraArticle','Document','Image')
#    filter_content_types  = 1
    content_icon = "fedorahierarchie_icon.gif"    
    actions = (
        { 'id': 'edit',
          'name': 'Edit',
          'action': 'string:${folder_url}/fedorahierarchie_edit_form',
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          'category':'folder',
          },
          
        { 'id': 'view',
          'name': 'View',
          'action': 'string:${folder_url}/',
          'permissions': (Permissions.VIEW_CONTENTS_PERMISSION,),
          'category':'folder',
          },
          
        { 'id': 'folderlisting',
          'name': 'Folder Listing',
          'action': 'string:${folder_url}/folder_listing',
          'permissions': (Permissions.VIEW_CONTENTS_PERMISSION,),
          'category':'folder',
          'visible':0,
          },
          
        { 'id': 'dc',
          'name': 'MetaData',
          'action': 'string:${folder_url}/fedorahierarchie_meta',
          'visible':0,
          'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          'category':'folder',
          },
          
        { 'id': 'references',
          'name': 'References',
          'visible':0,
          #'action': 'fedoraarticle_fedora',
          #'permissions': (Permissions.EDIT_CONTENTS_PERMISSION,),
          'category':'folder',
          },
          
    )
    
registerType(FedoraHierarchie,PROJECTNAME)
