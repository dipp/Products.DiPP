## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,selected_reviewer_id
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

reviewer_list = self.reviewer_considered
self.setReviewer_considered(reviewer_list +(selected_reviewer_id,))
revision = self.current_revision
self.setReviewerInfo(revision=revision, reviewer=selected_reviewer_id)
return state
