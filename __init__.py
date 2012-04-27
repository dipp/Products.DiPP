# -*- coding: utf-8 -*-
"""
 $Id$

"""

from Globals import package_home
from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from Products.GenericSetup import EXTENSION, profile_registry
from Products.CMFPlone.interfaces import IPloneSiteRoot
from config import *

def initialize(context):
    # Content Types
    import FedoraHierarchie
    import Volume
    import Issue
    import SpecialIssue
    #import FedoraArticle
    import FedoraDocument
    import FedoraXML
    import FedoraMultimedia
    import SubmissionFolder
    import Submission
    import Manuscript
    import Review
    import Attachment
    # Tools
    import EditorialToolboxTool
    import Fedora2DiPP3Tool
    import Fedora2DiPP2Tool
    import DiPPManagementTool
    import BibTool
    import SectionsTool
    import PeerReviewTool


    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME), PROJECTNAME)
    
    tools = (Fedora2DiPP3Tool.Fedora,
             Fedora2DiPP2Tool.Fedora,
             EditorialToolboxTool.toolbox,
             DiPPManagementTool.DiPPManagement,
             BibTool.BibTool,
             SectionsTool.SectionsTool,
             PeerReviewTool.PeerReviewTool)

    utils.ToolInit(PROJECTNAME + ' Tools',
        tools = tools,
        icon = 'dipptool.gif'
        ).initialize(context)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = ADD_CONTENTS_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = VIEW_CONTENTS_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = EDIT_CONTENTS_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)


dippworkflow_globals = globals()

registerDirectory('skins', globals())

profile_registry.registerProfile(
                    'install',
                    'DiPP',
                    'Extension profile for DiPP Product',
                    'profile/default',
                    'DiPP',
                    EXTENSION,
                    for_=IPloneSiteRoot)

profile_registry.registerProfile(
                    'uninstall',
                    'DiPP',
                    'Uninstall profile for DiPP Product',
                    'profile/uninstall',
                    'DiPP',
                    EXTENSION,
                    for_=IPloneSiteRoot)
