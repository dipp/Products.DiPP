# -*- coding: utf-8 -*-
#
# File: peerreview.py
#
# Copyright (c) 2010 by DiPP, hbz
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the 
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#

__author__ = """Peter Reimer <reimer@hbz-nrw.de>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.DiPP.config import *


from Products.CMFCore.utils import UniqueObject

    

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

editorialtoolbox_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class editorialtoolbox(UniqueObject, BaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(UniqueObject,'__implements__',()),) + (getattr(BaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'editorialtoolbox'

    meta_type = 'editorialtoolbox'
    portal_type = 'editorialtoolbox'
    allowed_content_types = ['Fedora Article']
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'peerreview.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "editorialtoolbox"
    typeDescMsgId = 'description_editorialtoolbox'
    #toolicon = 'peerreview.gif'


    actions =  (


       {'action': "string:${object_url}/editorialtoolbox_view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },



    )

    _at_rename_after_creation = True

    schema = peerreview_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    # tool-constructors have no id argument, the id is fixed
    def __init__(self, id=None):
        BaseFolder.__init__(self,'editorialtoolbox')
        self.setTitle('Editorial toolbox')
        
        ##code-section constructor-footer #fill in your manual code here
        ##/code-section constructor-footer


    # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        self.unindexObject()
        
        ##code-section post-edit-method-footer #fill in your manual code here
        ##/code-section post-edit-method-footer


    # Methods

    # Manually created methods



registerType(editorialtoolbox, PROJECTNAME)
# end of class peerreview

##code-section module-footer #fill in your manual code here
##/code-section module-footer



