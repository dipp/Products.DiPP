## Script (Python) "userHasLocalRole"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, user, role
##title=
##

# -*- coding: utf-8 -*-
"""
find out, wether a given user has a given role in the current context
"""
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal     = portal_url.getPortalObject()

entries = self.computeRoleMap()

hasRole = False
for entry in entries:
    if user == entry['id'] and role in entry['local']:
        hasRole = True
    else:
        pass

return hasRole

