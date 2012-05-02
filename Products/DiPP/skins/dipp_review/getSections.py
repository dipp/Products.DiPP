## Script (Python) "getSections"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal     = portal_url.getPortalObject()

sections = {}
results = container.portal_catalog(portal_type='Section', review_state='active')
for result in results:
    sections[result.getId] = result.Title

return sections
