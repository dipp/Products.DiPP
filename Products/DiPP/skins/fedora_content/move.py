## Script (Python) "pub_modify_instance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

request     = container.REQUEST
RESPONSE    = request.RESPONSE
oftool      = container.portal_openflow
mtool       = context.portal_membership
portal_url  = getToolByName(self, 'portal_url')
portal      = portal_url.getPortalObject()

instance_id = "auto1097738577.57"

destination = getattr(portal,'journal')
tempDir = getattr(portal,'tmp')

cut = tempDir.manage_cutObjects(instance_id)
print cut
print destination
#destination.manage_pasteObjects(cut)
print instance_id
return printed
