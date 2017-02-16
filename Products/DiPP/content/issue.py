# -*- coding: utf-8 -*-
#
# File: Issue.py
#
# Copyright (c) 2009 by DiPP, hbz
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the 
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#

__author__ = """Peter Reimer <reimer@hbz-nrw.de>"""
__docformat__ = 'plaintext'
from zope.interface import implements, Interface
try:
    from Products.LinguaPlone.public import *
    from Products.LinguaPlone import utils
except ImportError:
    from Products.Archetypes.public import *

from AccessControl import ClassSecurityInfo
try:
    from Products.CMFCore.permissions import ManagePortal
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal
    from Products.CMFCore.CMFCorePermissions import View
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from Products.DiPP.config import PROJECTNAME
from Products.DiPP.interfaces import IIssue
from Products.DiPP import Permissions
from Products.DiPP import event_utils

IssueSchema = BaseSchema + Schema((
        StringField('PID',
                required=0,
                widget=StringWidget(
                    label='PID',
                    label_msgid='label_pid_field',
                    description='Persistent Identifier',
                    description_msgid='help_pid_field',
                    i18n_domain='dipp',
                    size='15',
                    visible={'edit':'invisible','view':'visible'}
                ),
        ),

        TextField('description',
            required=0,
            widget=TextAreaWidget(label="description")
        ),

        StringField('MetaType',
                required=0,
                vocabulary=('volume','series','category','topic','article','congress','other'),
                widget=SelectionWidget(
                    label='MetaType',
                    label_msgid='label_metatype_field',
                    description='Art des Containers',
                    description_msgid='help_metatype_field',
                    i18n_domain='dipp',
                    size='15'),
        ),
        StringField('Volume',
            required=0,
            widget=StringWidget(
                label='Volume',
                label_msgid='label_volume_field',
                description='An Volume to hold the Issues.',
                description_msgid='help_volume_field',
                i18n_domain='dipp',
            ),
            schemata='Bibliographic Data'
        ),
        StringField('Issue',
            required=0,
            widget=StringWidget(
                label='Issue',
                label_msgid='label_issue_field',
                description='An Issue to hold the Articles. Usally part of a volume',
                description_msgid='help_issue_field',
                i18n_domain='dipp',
            ),
            schemata='Bibliographic Data'
        ),
        DateTimeField('IssueDate',
            required=0,
            widget=CalendarWidget(
                label='Date',
                label_msgid='label_issuedate_field',
                description='The Date on which this issue is published.',
                description_msgid='help_issuedate_field',
                i18n_domain='dipp',
            ),
            schemata='Bibliographic Data'
        ),
        FileField('CompleteIssue',
            required=0,
            widget=FileWidget(
                label='Complete Issue',
                label_msgid='label_completeissue_field',
                description='The complete Issue in a single PDF file',
                description_msgid='help_completeissue_field',
                i18n_domain='dipp',
            ),
            schemata='Advanced'
        ),
        TextField('Body',
            required=0,
            widget=RichWidget(
                label='Body',
                description='Introductory Text for this issue.'
            ),
            schemata='Advanced'
        ),
        ImageField('TitleImage',
            required=0,
            widget=ImageWidget(
                label='Cover picture',
                label_msgid='label_titleimage_field',
                description='Select an image for the frontpage of this issue',
                description_msgid='help_titleimage_field',
                i18n_domain='dipp',
            ),
            sizes={'small':(120,120),'medium':(250,250),'large':(600,600)},
            schemata='Advanced'
        )
    ))

class Issue(BrowserDefaultMixin, OrderedBaseFolder):
    """Hierarchical Object representing an issue."""
    
    security = ClassSecurityInfo()
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)
    implements(IIssue)

    manage_urn_form = PageTemplateFile('../www/urn_form.pt', globals())
    security.declareProtected(ManagePortal, 'manage_urn_form')

    manage_options = OrderedBaseFolder.manage_options[0:1] + ({'label':'View',
                       'action':''},
                      {'label':'URN Management',
                       'action':'manage_urn_form',
                       'help':('DiPP', 'urn.stx')}, 
        ) + OrderedBaseFolder.manage_options[2:]

    schema = IssueSchema
    _at_rename_after_creation = True
    archetype_name = "Issue"

    def at_post_create_script(self):

        """add a hierarchical object to fedora and write the PID back to the Plone object
        """
        event_utils.createFedoraContainer(self, None)
        
    
registerType(Issue,PROJECTNAME)
