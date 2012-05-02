# -*- coding: utf-8 -*-
#
# File: SubmissionFolder.py
#
# Copyright (c) 2011 by DiPP, hbz
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
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
import Permissions

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SubmissionFolder_schema = BaseBTreeFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class SubmissionFolder(BaseBTreeFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseBTreeFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Submission folder'

    meta_type = 'SubmissionFolder'
    portal_type = 'SubmissionFolder'
    allowed_content_types = ['Submission']
    filter_content_types = 1
    global_allow = 1
    #content_icon = 'SubmissionFolder.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Submission folder"
    typeDescMsgId = 'description_edit_submissionfolder'


    actions =  (


       {'action': "string:${object_url}/manuscript_submit_form",
        'category': "object",
        'id': 'manuscript_submit_form',
        'name': 'Submit manuscript',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/submissions_overview",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },

    )

    _at_rename_after_creation = True

    schema = SubmissionFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(SubmissionFolder, PROJECTNAME)
# end of class SubmissionFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



