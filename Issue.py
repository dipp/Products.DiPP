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

from Products.Archetypes.public import *
from config import PROJECTNAME
import Permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.CMFCore.utils import getToolByName

from zLOG import LOG, ERROR, INFO

class Issue(BrowserDefaultMixin, OrderedBaseFolder):
    """Hierarchical Object representing an issue."""
    
    __implements__ = (getattr(BrowserDefaultMixin,'__implements__',()),) + (getattr(OrderedBaseFolder,'__implements__',()),)
    
    schema = BaseSchema + Schema((
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
                index='FieldIndex:brains'
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
            index='FieldIndex:brains',
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
            index='FieldIndex:brains',
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
            index='FieldIndex:brains',
            schemata='Bibliographic Data'
        ),
        FileField('CompleteIssue',
            required=0,
            widget=FileWidget(
                label='Complete Isse',
                description='The complete Issue in a single PDF file'
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
    _at_rename_after_creation = True
    archetype_name = "Issue"
    archetype_description = "Hierarchical Object representing an issue"
    allowed_content_types = ('FedoraArticle')
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ('base_view', 'issue_contents_view')
    content_icon = 'fedorahierarchie_icon.gif'
    actions = (
          
        { "id": "view",
          "name": "View",
          "action": "string:${folder_url}/",
          "permissions": (Permissions.VIEW_CONTENTS_PERMISSION,),
          "category":"folder",
          },
    )

    def at_post_create_script(self):
        """add a hierarchical object to fedora and write the PID back to the Plone object
        """

        fedora = getToolByName(self, 'fedora')
        portal = getToolByName(self, 'portal_url').getPortalObject()
        parent = self.getParentNode()
        if parent == portal:
            isChildOf = fedora.PID
        else:
            isChildOf = parent.PID
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
        
    
registerType(Issue,PROJECTNAME)
