## Script (Python) "checkForNewPIDs"
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

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

#besitzer = 'redak'
#new_owner_obj = self.acl_users.getUser(besitzer)
#new_owner_obj = new_owner_obj.__of__(self.acl_users)
#print new_owner_obj
tempDir = getattr(portal,'tmp')
id ="XXX"
print tempDir.id
tempDir.invokeFactory('FedoraArticle',id=id,title='bla bla',PID='dipp:1')
obj = getattr(tempDir,id)
obj.manage_addProperty(id="tmp", value=True, type='boolean')
print obj.id
return printed
