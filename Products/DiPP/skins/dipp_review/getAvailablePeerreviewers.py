## Script (Python) "getAvailablePeerreviewers"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, section_id=None
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
gtool = getToolByName(portal, 'portal_groups')
mtool = getToolByName(portal, 'portal_membership')
mship = self.portal_membership

group = gtool.getGroupById('peerreviewer')
grouptitle = group.getGroupTitleOrName()
groupMembers = group.getGroupMembers()
peers = []
rc = []
for x in self.reviewer_considered:
    member = mtool.getMemberById(str(x))
    rc.append(member)
    
    
for groupMember in groupMembers:
    if groupMember not in rc:
        peers.append(groupMember)

return peers
