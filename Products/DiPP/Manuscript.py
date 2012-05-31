# -*- coding: utf-8 -*-
#
# File: Manuscript.py
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
import Permissions
from Products.DiPP.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    FileField(
        name='original',
        widget=FileWidget(
            label="The Manuscript",
            description="The original manuscript submitted by the author.",
            label_msgid='DiPPReview_label_original',
            description_msgid='DiPPReview_help_original',
            i18n_domain='DiPPReview',
        ),
        required=1,
        storage=AttributeStorage(),
        read_permission=Permissions.VIEW_ORIGINAL_MANUSCRIPT_PERMISSION,
        view=Permissions.VIEW_ORIGINAL_MANUSCRIPT_PERMISSION
    ),

    FileField(
        name='anonym',
        widget=FileWidget(
            label="Anonymized Manuscript",
            description="For a double blind review the manuscript must not contain the authors name",
            label_msgid='DiPPReview_label_anonym',
            description_msgid='DiPPReview_help_anonym',
            i18n_domain='DiPPReview',
        ),
        storage=AttributeStorage(),
        view=Permissions.VIEW_ANONYM_MANUSCRIPT_PERMISSION,
        read_permission=Permissions.VIEW_ANONYM_MANUSCRIPT_PERMISSION,
        write_permission=Permissions.ADD_ANONYM_MANUSCRIPT_PERMISSION
    ),

    IntegerField(
        name='revision',
        widget=IntegerField._properties['widget'](
            label='Revision',
            label_msgid='DiPPReview_label_revision',
            i18n_domain='DiPPReview',
        ),
        write_permission="Manager"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Manuscript_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Manuscript(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Manuscript'

    meta_type = 'Manuscript'
    portal_type = 'Manuscript'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Manuscript.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Manuscript"
    typeDescMsgId = 'description_edit_manuscript'

    _at_rename_after_creation = True

    schema = Manuscript_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Manuscript, PROJECTNAME)
# end of class Manuscript

##code-section module-footer #fill in your manual code here
##/code-section module-footer



