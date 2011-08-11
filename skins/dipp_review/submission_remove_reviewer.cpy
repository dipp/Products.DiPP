## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,reviewer_ids
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

pm = context.portal_membership
rc = self.reviewer_considered

nrc = []
for i in rc:
    if i not in reviewer_ids:
        nrc.append(i)

for reviewer_id in reviewer_ids:
    pm.deleteLocalRoles(obj=self,member_ids=reviewer_ids)

self.setReviewer_considered(nrc)

return state
