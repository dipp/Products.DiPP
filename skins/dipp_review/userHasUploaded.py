## Script (Python) "userHasUploaded"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, user, content_type, revision
##title=
##

# -*- coding: utf-8 -*-
# check wether a user has already uploaded a certain content_type to the current folder
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
mtool = getToolByName(self, 'portal_membership')
portal     = portal_url.getPortalObject()
path = '/'.join(self.getPhysicalPath())
Creator = str(user)
results = container.portal_catalog(portal_type=content_type, getCurrent_revision=revision,path=path,Creator=Creator)
for x in results:
    context.plone_log(x.getURL())

if results:
    return False
else: 
    return True
