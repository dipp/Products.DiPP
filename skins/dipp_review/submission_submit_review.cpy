## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self, current_revision, comment_for_author, comment_for_editor, review_for_author, review_for_editor, vote
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

id = context.getId()
new_context = context.portal_factory.doCreate(context, id)

formatted_comment =  """Comment for the author:
%s

Comment for the Editor
%s
"""
comment = formatted_comment % (comment_for_author, comment_for_editor)
context.portal_workflow.doActionFor(new_context,'submit_review', comment=comment)

current_revision = self.current_revision

review_counter = self.review_counter + 1
review_id = "review-%drev%d" % (review_counter, int(current_revision))
self.invokeFactory(id=review_id, 
                   type_name='Review', 
                   current_revision=current_revision,
                   title=review_id,
                   vote=vote,
                   comment_for_author=comment_for_author,
                   comment_for_editor=comment_for_editor,
                   review_for_author=review_for_author,
                   review_for_editor=review_for_editor)

obj = getattr(self,review_id)
obj.setVote(vote)
obj.setCurrent_revision(current_revision)
self.reindexObject()

context.plone_log("Revision %d" % int(current_revision))
context.plone_log("Vote %s" % vote)


self.manage_changeProperties({'review_counter':review_counter})

return state.set(context=new_context, portal_status_message="Thank you for submitting your report")
