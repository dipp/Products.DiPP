# -*- coding: utf-8 -*-
"""
 $Id$

"""

from Globals import package_home
from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from config import *

def initialize(context):
    ##Import Types to register them
    import FedoraHierarchie
    import FedoraArticle
    import FedoraDocument
    import FedoraXML
    import FedoraMultimedia
    import MyThreadTest

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME), PROJECTNAME)

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
registerDirectory('skins/dipp_portlets', globals())
registerDirectory('skins/dipp_scripts', globals())
registerDirectory('skins/dipp_workflow', globals())
registerDirectory('skins/dipp_images', globals())
registerDirectory('skins/dipp_forms', globals())
registerDirectory('skins/dipp_form_scripts', globals())
registerDirectory('skins/fedora_content', globals())

