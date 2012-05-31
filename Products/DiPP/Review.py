# -*- coding: utf-8 -*-
#
# File: Review.py
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
        name='review_for_author',
        widget=FileWidget(
            label="Review for the author",
            description="If you have written your review with an word processor you can uload your file here.",
            label_msgid='DiPPReview_label_review_for_author',
            description_msgid='DiPPReview_help_review_for_author',
            i18n_domain='DiPPReview',
        ),
        storage=AttributeStorage(),
        read_permission=Permissions.VIEW_AUTHOR_REVIEW_PERMISSION
    ),

    FileField(
        name='review_for_editor',
        widget=FileWidget(
            label="Review for the editor",
            description="If you have written your review with an word processor you can uload your file here.",
            label_msgid='DiPPReview_label_review_for_editor',
            description_msgid='DiPPReview_help_review_for_editor',
            i18n_domain='DiPPReview',
        ),
        storage=AttributeStorage(),
        read_permission=Permissions.VIEW_EDITOR_REVIEW_PERMISSION
    ),

    IntegerField(
        name='current_revision',
        widget=IntegerField._properties['widget'](
            label='Current_revision',
            label_msgid='DiPPReview_label_current_revision',
            i18n_domain='DiPPReview',
        ),
        required=1
    ),

    TextField(
        name='comment_for_author',
        widget=TextAreaWidget(
            label="Comment for the author",
            description="You can add your comment directly in the textbox below.",
            label_msgid='DiPPReview_label_comment_for_author',
            description_msgid='DiPPReview_help_comment_for_author',
            i18n_domain='DiPPReview',
        ),
        read_permission=Permissions.VIEW_AUTHOR_REVIEW_PERMISSION
    ),

    TextField(
        name='comment_for_editor',
        widget=TextAreaWidget(
            label="Comment for the editor",
            description="You can add your comment directly in the textbox below.",
            label_msgid='DiPPReview_label_comment_for_editor',
            description_msgid='DiPPReview_help_comment_for_editor',
            i18n_domain='DiPPReview',
        ),
        read_permission=Permissions.VIEW_EDITOR_REVIEW_PERMISSION
    ),

    StringField(
        name='vote',
        widget=SelectionWidget(
            label="Recommendation",
            description="Make your recommendation based on the available choices.",
            label_msgid='DiPPReview_label_vote',
            description_msgid='DiPPReview_help_vote',
            i18n_domain='DiPPReview',
        ),
        required=1,
        vocabulary="getVotes"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Review_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Review(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Review'

    meta_type = 'Review'
    portal_type = 'Review'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'Review.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Review"
    typeDescMsgId = 'description_edit_review'

    _at_rename_after_creation = True

    schema = Review_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def getVotes(self):
        """return all possible votes/recommendtions a reviewer can make"""

        return self.portal_properties.dippreview_properties.votes

    def getRevisions(self):
        """return all revision of this submission"""

        current_revision = self.getParentNode().current_revision
        return list(tuple(range(0,current_revision + 1,1)))



registerType(Review, PROJECTNAME)
# end of class Review

##code-section module-footer #fill in your manual code here
##/code-section module-footer



