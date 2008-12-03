# -*- coding: utf-8 -*-
from Products.Archetypes.public import *
from config import PROJECTNAME
from AccessControl import ClassSecurityInfo
import Permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

class FedoraArticle(BrowserDefaultMixin, OrderedBaseFolder):
    """
        Folder, that represents a digital Object of the Fedora Database.
        It can only contain FedoraDocument, FedoraImages,...
    """
    
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)

    schema = BaseSchema + Schema((
        StringField('PID',
                required=1,
                widget=StringWidget(label='PID',description='Persistent Identifier',size='15'),
                searchable=1,
                index="FieldIndex:brains"        
        ),
        StringField('pixel_domain',
                required=0,
                widget=StringWidget(label='VG Kürzel',description='Domain auf dem Zählserver: vgXX.met.vgwort.de, z.B. vg06',size='4')
        ),
        StringField('pixel_id',
                required=0,
                widget=StringWidget(label='VGWort Public ID',description='Der öffentliche Identifikationscode des Zählpixels',size='40')
        ),
        IntegerField('position',
                widget=IntegerWidget(label="The Postion of the article in a special issue."),
                storage=AttributeStorage(),
                searchable=1,
                index="FieldIndex"        
        ),
        StringField(
            name='comment_to',
            widget=SelectionWidget(
                label="Comment to",
                description="This Article is a comment to another article",
            ),
            searchable=1,
            index="FieldIndex:brains",
            multiValued=0,
            vocabulary="getPublishedArticles"
        ),
    ))

    allowed_content_types = ('FedoraDocument','FedoraMultimedia','FedoraXML')
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ('base_view', 'metadata_view', 'splash_screen')
    filter_content_types= 1
    content_icon = 'fedoraarticle_icon.gif'
    actions = (
    #    { "id": "edit",
    #      "name": "Edit",
    #      "action": "string:${folder_url}/fedoraarticle_edit_form",
    #      "permissions": (Permissions.EDIT_CONTENTS_PERMISSION,),
    #      "category":"folder",
    #      },
          
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
    
    security.declareProtected(Permissions.EDIT_CONTENTS_PERMISSION, 'syncMetadata')
    def syncMetadata(self,params):
        """keep Metadata of Plone and Fedora synchron"""

        firstNames = params['author_firstName'] 
        lastNames = params['author_lastName']
        contributors = []
        for i in range(len(firstNames)):
            contributors.append(lastNames[i] + ", " + firstNames[i])
        
        self.setContributors(contributors)
        self.setSubject(params['subject'])
        self.setRights(params['rights'][0])
        self.reindexObject()
    
    def getPublishedArticles(self):

        results = self.portal_catalog.searchResults(Type='Fedora Article')
        articles = (('','None'),)
        for result in results:
            PID = result.getPID
            title = result.Title
            if not PID.startswith('temp'):
                articles += ((PID,title),)

        return articles
         

        
    
registerType(FedoraArticle,PROJECTNAME)
