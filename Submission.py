# -*- coding: utf-8 -*-
#
# File: Submission.py
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
from Products.CMFCore.permissions import ManagePortal, ManageProperties
from StringIO import StringIO
##/code-section module-header

schema = Schema((

    LinesField(
        name='manuscript_authors',
        index="FieldIndex:brains",
        widget=LinesField._properties['widget'](
            label="Authors",
            description="The names and affiliations of all authors in the form first name, last name, affiliation",
            label_msgid='DiPPReview_label_manuscript_authors',
            description_msgid='DiPPReview_help_manuscript_authors',
            i18n_domain='DiPPReview',
        ),
        required=1,
        read_permission=Permissions.VIEW_AUTHOR_DETAILS
    ),

    LinesField(
        name='reviewer',
        widget=LinesField._properties['widget'](
            label='Reviewer',
            label_msgid='DiPPReview_label_reviewer',
            i18n_domain='DiPPReview',
        ),
        read_permission=Permissions.VIEW_REVIEWER_DETAILS
    ),

    DateTimeField(
        name='date_submitted',
        index="DateIndex:brains",
        widget=CalendarWidget(
            label='Date_submitted',
            label_msgid='DiPPReview_label_date_submitted',
            i18n_domain='DiPPReview',
        )
    ),

    DateTimeField(
        name='date_accepted',
        widget=CalendarWidget(
            label='Date_accepted',
            label_msgid='DiPPReview_label_date_accepted',
            i18n_domain='DiPPReview',
        )
    ),

    DateTimeField(
        name='date_published',
        widget=CalendarWidget(
            label='Date_published',
            label_msgid='DiPPReview_label_date_published',
            i18n_domain='DiPPReview',
        )
    ),

    StringField(
        name='title',
        widget=StringWidget(
            description="Please add the title of your manuscript.",
            label="Manuscript title",
            label_msgid='DiPPReview_label_title',
            description_msgid='DiPPReview_help_title',
            i18n_domain='DiPPReview',
        ),
        required=1
    ),

    TextField(
        name='manuscript_abstract',
        widget=TextAreaWidget(
            label="Abstract",
            description="The abstract of your manuscript. Use only plain text and a maximum of 300 words.",
            label_msgid='DiPPReview_label_manuscript_abstract',
            description_msgid='DiPPReview_help_manuscript_abstract',
            i18n_domain='DiPPReview',
        ),
        required=1
    ),

    StringField(
        name='section',
        index="FieldIndex:brains",
        widget=StringWidget(
            label="Section",
            description="Choose the section in which your submission should appear.",
            label_msgid='DiPPReview_label_section',
            description_msgid='DiPPReview_help_section',
            i18n_domain='DiPPReview',
        ),
        required=1
    ),

    BooleanField(
        name='agb',
        widget=BooleanField._properties['widget'](
            label="Terms and Condition",
            description="Please agree to the Terms and Condition.",
            label_msgid='DiPPReview_label_agb',
            description_msgid='DiPPReview_help_agb',
            i18n_domain='DiPPReview',
        ),
        required=1
    ),

    LinesField(
        name='reviewer_considered',
        widget=LinesField._properties['widget'](
            label='Reviewer_considered',
            label_msgid='DiPPReview_label_reviewer_considered',
            i18n_domain='DiPPReview',
        ),
        read_permission=Permissions.VIEW_REVIEWER_DETAILS
    ),

    IntegerField(
        name='current_revision',
        index="FieldIndex:brains",
        widget=IntegerField._properties['widget'](
            label="Current Revision",
            description="Counter for the revisons of the submissions. Gets updated in the workflow.",
            label_msgid='DiPPReview_label_current_revision',
            description_msgid='DiPPReview_help_current_revision',
            i18n_domain='DiPPReview',
        ),
        write_permission="Manage properties"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Submission_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Submission(OrderedBaseFolder):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Submission'

    meta_type = 'Submission'
    portal_type = 'Submission'
    allowed_content_types = ['Manuscript', 'Review', 'Attachment']
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'Submission.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Submission"
    typeDescMsgId = 'description_edit_submission'


    actions =  (


       {'action': "string:${object_url}/submission_view",
        'category': "object",
        'id': 'view',
        'name': 'Submission',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/folder_localrole_form",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("Manage properties",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = Submission_schema

    ##code-section class-header #fill in your manual code here
    aliases = {
        '(Default)'  : 'submission_view',
        'view'       : 'submission_view',
        'edit'       : 'atct_edit',
        'properties' : 'base_metadata',
        }
    ##/code-section class-header

    # Methods

    # Manually created methods

    def isAnonymized(self):
        """check if all manuscripts and attachmends are anonymized
        """
        path ='/'.join(self.getPhysicalPath())
        results = self.portal_catalog.searchResults(Type=('Manuscript','Attachment'), path=path)
        files = len(results)
        anonym = 0
        for result in results:
            obj = result.getObject()
            if obj.anonym.size != 0:
                anonym += 1
        #return {'files':files, 'anonym':anonym}
        if anonym == files:
            return True
        else:
            return False

    def hasSufficientReviews(self):
        """check if the required number of reviews are submitted
           number is stored in variable min_reviewer
        """
        path ='/'.join(self.getPhysicalPath())
        results = self.portal_catalog.searchResults(Type=('Review'), path=path)
        min_reviewers = self.portal_properties.dippreview_properties.min_reviewers
        files = len(results)
        if files < min_reviewers:
            return False
        else:
            return True

    security.declareProtected(ManagePortal, 'addReviewerInfo')
    def addReviewerInfo(self, revision):
        """
        """
        self.reviewer_info = {revision:{}}

    security.declareProtected(ManageProperties, 'getReviewerInfo')
    def getReviewerInfo(self):
        """ return all information about a given reviewer of a given revision
        """
        try:
            return self.reviewer_info
        except:
            return None

    security.declareProtected(ManageProperties, 'setReviewerInfo')
    def setReviewerInfo(self,revision, reviewer):
        """
        """
        revision = revision
        reviewer = reviewer
        info = {
            'code_accept':'',
            'code_decline':'',
            'code_unavailable':'',
            'date_invited':'',
            'date_accepted':'',
            'date_submitted':'',
            'deadline':'',
            'friendly_reminders':[],
            'deadline_reminders':[],
            'due_reminders':[]
            }

        self.reviewer_info[revision][reviewer] = info

    security.declareProtected(ManageProperties, 'setReviewerProperty')
    def setReviewerProperty(self,revision, reviewer, property, value):
        """
        """
        self.reviewer_info[revision][reviewer][property] = value
        self.reindexObject()

    security.declareProtected(ManageProperties, 'resetReviewerProperties')
    def resetReviewerProperties(self,revision, reviewer):
        """
        """
        info = {
            'code_accept':'',
            'code_decline':'',
            'code_unavailable':'',
            'date_invited':'',
            'date_accepted':'',
            'date_submitted':'',
            'deadline':'',
            'friendly_reminders':[],
            'deadline_reminders':[],
            'due_reminders':[]
            }
        self.reviewer_info[revision][reviewer] = info
        self.reindexObject()
        out = StringIO()
        print >> out, "Properties of revision '%s', reviewer '%s' resetted" % (revision, reviewer)

    security.declareProtected(ManageProperties, 'removeConsideredReviewer')
    def removeConsideredReviewer(self,reviewer):
        """
        """
        self.setReviewer_considered(reviewer)



registerType(Submission, PROJECTNAME)
# end of class Submission

##code-section module-footer #fill in your manual code here
##/code-section module-footer



