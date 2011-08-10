# -*- coding: utf-8 -*-
#
# File: peerreview.py
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
import time, random, md5, socket
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger("DiPP")

class PeerReviewTool(UniqueObject, SimpleItem):
    """
    """
    id = "dipp_peerreview"
    title = 'Manages the peerreview'
    meta_type = 'DiPP Peerreview Tool'
    
    security = ClassSecurityInfo()
        
    global_allow = 0
    #content_icon = 'peerreview.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "peerreview"
    typeDescMsgId = 'description_edit_peerreview'
    #toolicon = 'peerreview.gif'


    actions =  (


       {'action': "string:${object_url}/submissions_overview",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/manuscript_submit_form",
        'category': "object",
        'id': 'manuscript_submit_form',
        'name': 'Submit Manuscript',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/statistics_form",
        'category': "object",
        'id': 'statistics_form',
        'name': 'statistics_form',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True


    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # tool should not appear in portal_catalog
    def at_post_edit_script(self):
        self.unindexObject()
        
        ##code-section post-edit-method-footer #fill in your manual code here
        ##/code-section post-edit-method-footer


    # Methods

    # Manually created methods

    def uniqueString(self):
        """Returns a string that is random and unguessable, or at
        least as close as possible.

        This is used by 'requestReset' to generate the auth
        string. Override if you wish different format.

        This implementation ignores userid and simply generates a
        UUID. That parameter is for convenience of extenders, and
        will be passed properly in the default implementation."""
        # this is the informal UUID algorithm of
        # http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/213761
        # by Carl Free Jr
        t = long( time.time() * 1000 )
        r = long( random.random()*100000000000000000L )
        try:
            a = socket.gethostbyname( socket.gethostname() )
        except:
            # if we can't get a network address, just imagine one
            a = random.random()*100000000000000000L
        data = str(t)+' '+str(r)+' '+str(a)#+' '+str(args)
        data = md5.md5(data).hexdigest()
        return str(data)

    def createuniqueids(self):
        """create unique ids for agreeing to review
        """
        agree = self.uniqueString()
        decline = self.uniqueString()
        unavailable = self.uniqueString()
        ids =  {'agree':agree, 'decline':decline, 'unavailable':unavailable}
        return ids

    def getSectionEditors(self, section_id):

        portal_url = getToolByName(self, 'portal_url')
        portal  = portal_url.getPortalObject()
        sections = self.portal_catalog(portal_type='Section', id=section_id, review_state='active')
        mship = self.portal_membership

        editors = []

        for  section in sections:
            obj = section.getObject()
            local_roles = obj.get_local_roles()
            for user, role in local_roles:
                if 'pr_SectionEditor' in role:
                    user = mship.getMemberById(user)
                    id = user.getId()
                    email = user.getProperty('email')
                    fullname = user.getProperty('fullname')
                    editors.append({'id':id,'email':email,'fullname':fullname,'user':user})
        return editors





