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
from Products.Five.fiveconfigure import logger
try:
    from Products.CMFCore.permissions import ManagePortal
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal
    from Products.CMFCore.CMFCorePermissions import View
import logging
from operator import itemgetter

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
        self.sections = []

    security.declareProtected(ManagePortal, 'updateSection')
    def updateSection(self, id, title, position, editor=None, allow=None):
        """Updates a section."""
        
        sections = self.sections
        i = self.findSectionIndex(sections, id)
        sections[i] = (id, title, position, editor, allow)
        self.sections = sections
        
    security.declareProtected(ManagePortal, 'addSection')
    def addSection(self, id, title, position, editor=None, allow=None):
        """Adds a new section."""
        
        sections = self.sections
        sections.append((id, title, position, editor, allow))
        self.sections = sections

    security.declareProtected(ManagePortal, 'delSection')
    def delSection(self, id):
        """Deletes a section."""
        
        sections = self.sections
        i = self.findSectionIndex(sections, id)
        sections.pop(i)
        self.sections = sections
        
    def findSectionIndex(self, sections, id):
        """return the list index of a section according to its id"""
        
        for i, x in enumerate(sections):
            if x[0] == id: 
                return i

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
        
        self.addSection(id, title, position, editor, allow)                        
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
    def getSections(self, lang='all'):
        """return the list of sections sorted by position"""
        
        sections = self.sections
        sections.sort(key = itemgetter(2))
        sorted_sections = []
        for id, title, position, editor, allow in sections:
            if lang != 'all':
                translated_title = title.get(lang,id)
            else:
                translated_title = title
            sorted_sections.append({'id':id, 'title': translated_title, 'position':position, 'allow':allow, 'editor':editor})
        return sorted_sections
    
    security.declarePublic('getSectionById')
    def getSectionById(self, id, lang='all'):
        """return a section of a given ID. If not found, return None"""

        sectiondetails = None
        for section in self.getSections(lang):
            if section['id'] == id:
                sectiondetails = section
        
        return sectiondetails
               
                
