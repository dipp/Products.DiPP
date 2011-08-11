## Controller Python Script "submission_invite_reviewer"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,reviewer_id, code_accept, code_decline, code_unavailable, comment
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
#context.plone_log("reviewer_id:" + reviewer_id)
context.plone_log(reviewer_id)
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

id = context.getId()
new_context = context.portal_factory.doCreate(context, id)

context.portal_workflow.doActionFor(
    new_context,'invite_reviewer',
    comment=comment,
    reviewer_id=reviewer_id,
    code_accept=code_accept,
    code_decline=code_decline,
    code_unavailable=code_unavailable,
)
return state.set(context=new_context,status='success')
