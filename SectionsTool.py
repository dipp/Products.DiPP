# -*- coding: utf-8 -*-
# The FedoraTool for adding and manipulating objects in Fedora
# File: Fedora2DiPP3Tool.py
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
try:
    from Products.CMFCore.permissions import ManagePortal
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal
    from Products.CMFCore.CMFCorePermissions import View

class SectionsTool(UniqueObject,SimpleItem):
    
    id = 'dipp_sections'
    title = 'Manages Journal Sections and Editors'
    meta_type = 'DiPP Sections Tool'
    
    security = ClassSecurityInfo()
    
    def __init__(self):
        self.id = 'dipp_sections'
