# -*- coding: utf-8 -*-
# The FedoraTool for adding and manipulating objects in Fedora
# File: SectionsTool.py
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
import logging

logger = logging.getLogger("DiPP")

class SectionsTool(UniqueObject, SimpleItem):
    
    id = 'dipp_sections'
    title = 'Manages Journal Sections and Editors'
    meta_type = 'DiPP Sections Tool'
    
    security = ClassSecurityInfo()
    
    manage_options = ({ 'label'  : 'Sections Configuration',
                        'action' : 'manage_SectionsConfig'},
                      ) + SimpleItem.manage_options
    
    manage_SectionsConfig = PageTemplateFile('www/sections_config_form.pt', globals())
    security.declareProtected(ManagePortal, 'manage_SectionsConfig')

    def __init__(self):
        self.sections = {}

    security.declareProtected(ManagePortal, 'updateSection')
    def updateSection(self, id, title, position, editor=None, allow=None):
        """Updates a section."""
        
        sections = self.sections
        sections[id] = {'title': title, 'position':position, 'allow':allow, 'editor':editor}
        self.sections = sections
        
    security.declareProtected(ManagePortal, 'addSection')
    def addSection(self, id, title, position, editor=None, allow=None):
        """Adds a new section."""
        
        sections = self.sections
        sections[id] = {'title': title, 'position':position, 'allow':allow, 'editor':editor}
        self.sections = sections

    security.declareProtected(ManagePortal, 'delSection')
    def delSection(self, id):
        """Deletes a section."""
        
        sections = self.sections
        sections.pop(id)
        self.sections = sections

    security.declareProtected(ManagePortal, 'manage_updateSection')
    def manage_updateSection(self, id, title, position, editor=None, allow=None, REQUEST=None):
        """Updates a section via the ZMI."""
        
        self.updateSection(id, title, position, editor, allow)
        manage_tabs_message = "Section '%s' updated" % id

        REQUEST['RESPONSE'].redirect( '%s/manage_SectionsConfig?manage_tabs_message=%s'
                            % (self.absolute_url(), manage_tabs_message)
                            )

    security.declareProtected(ManagePortal, 'manage_addSection')
    def manage_addSection(self, id, title, position, editor=None, allow=None, REQUEST=None):
        """Adds a new section via the ZMI."""
        
        self.addSection(id, title, position, editor=None, allow=None)                        
        manage_tabs_message = "Section '%s' added" % id
        REQUEST['RESPONSE'].redirect( '%s/manage_SectionsConfig?manage_tabs_message=%s'
                            % (self.absolute_url(), manage_tabs_message)
                            )

    security.declareProtected(ManagePortal, 'manage_delSection')
    def manage_delSection(self, id, REQUEST=None):
        """Deletes a section via the ZMI."""
        
        self.delSection(id)
        manage_tabs_message = "Section '%s' deleted" % id
        REQUEST['RESPONSE'].redirect( '%s/manage_SectionsConfig?manage_tabs_message=%s'
                            % (self.absolute_url(), manage_tabs_message)
                            )
            
    
    security.declarePublic('getSections')
    def getSections(self):
        
        return self.sections

