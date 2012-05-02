## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,r,c
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
wtool = getToolByName(self, 'portal_workflow')

id = context.getId()

reviewer_id = r
code = c
context.plone_log(code)
revision = int(wtool.getInfoFor(self, 'revision', 0))

code_accept = self.getReviewerInfo()[revision][reviewer_id]['code_accept']
code_decline = self.getReviewerInfo()[revision][reviewer_id]['code_decline']
code_unavailable = self.getReviewerInfo()[revision][reviewer_id]['code_unavailable']

context.plone_log('code_accept', code_accept)
context.plone_log('code', code)

if code == code_accept:
    transition = 'accept_invitation'
    comment = "accepted via mail link"
    answer = "accepted"

elif code == code_decline:
    transition = 'decline_invitation'
    comment = "declined via mail link"
    answer = "declined"

elif code == code_unavailable:
    transition = 'decline_invitation'
    comment = "declined via mail link, not available"
    answer = "unavailable"

else:
    transition = 'undefinded transition'

context.plone_log(transition)

new_context = context.portal_factory.doCreate(context, id)

context.portal_workflow.doActionFor(
    new_context,transition,
    comment=comment,
    reviewer_id=reviewer_id
)
return state.set(context=new_context,answer=answer)

