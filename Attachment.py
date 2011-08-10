# -*- coding: utf-8 -*-
#
# File: Attachment.py
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
            label='Original',
            label_msgid='DiPPReview_label_original',
            i18n_domain='DiPPReview',
        ),
        storage=AttributeStorage(),
        read_permission=Permissions.VIEW_ORIGINAL_ATTACHMENT_PERMISSION
    ),

    FileField(
        name='anonym',
        widget=FileWidget(
            label='Anonym',
            label_msgid='DiPPReview_label_anonym',
            i18n_domain='DiPPReview',
        ),
        storage=AttributeStorage(),
        read_permission=Permissions.VIEW_ANONYM_ATTACHMENT_PERMISSION
    ),

    IntegerField(
        name='revision',
        index="FieldIndex:brains",
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

Attachment_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Attachment(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Attachment'

    meta_type = 'Attachment'
    portal_type = 'Attachment'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Attachment.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Attachment"
    typeDescMsgId = 'description_edit_attachment'

    _at_rename_after_creation = True

    schema = Attachment_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Attachment, PROJECTNAME)
# end of class Attachment

##code-section module-footer #fill in your manual code here
##/code-section module-footer



