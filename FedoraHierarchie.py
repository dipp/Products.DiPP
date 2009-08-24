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
                index='FieldIndex:brains'
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
    default_view = 'base_view'
    suppl_views = ('base_view', 'issue_contents_view')
    content_icon = 'fedorahierarchie_icon.gif'

    def at_post_create_script(self):
        """add a hierarchical object to fedora and write the PID back to the Plone object
        """

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
        self.reindexObject()

    def at_post_edit_script(self):
        """ keep metadata in sync
        """

        fedora = getToolByName(self, 'fedora')
        id = self.id
        AbsoluteURL = self.absolute_url()
        msg = "new id: %s, new url: %s" % (id, AbsoluteURL)
        LOG ('DIPP', INFO, msg)
        
    
registerType(FedoraHierarchie,PROJECTNAME)
