## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,manuscript_file="",attachment_file="",manuscript_authors="",manuscript_abstract="",title="",section="",agb=""
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
wtool = getToolByName(self, 'portal_workflow')
portal = portal_url.getPortalObject()

dp = portal.portal_properties.dippreview_properties
SUBMISSION_PREFIX = dp.submission_prefix
SUBMISSION_COUNTER = dp.submission_counter + 1

submission_id = "%s-%d" % (SUBMISSION_PREFIX, SUBMISSION_COUNTER)  
revision = wtool.getInfoFor(self, 'revision', 0)
context.plone_log("Revision %d" % revision)

self.invokeFactory(id=submission_id, 
    type_name='Submission',
    title=title,
    manuscript_authors=manuscript_authors,
    manuscript_abstract=manuscript_abstract,
    section=section,
    current_revision=revision,
    agb=agb
    )

submission = getattr(self, submission_id)

submission.manage_addProperty('manuscript_counter', 0, 'int')
submission.manage_addProperty('attachment_counter', 0, 'int')
submission.manage_addProperty('review_counter', revision, 'int')
dest = submission.absolute_url()
context.plone_log(dest, submission.id)

if manuscript_file:
    manuscript_counter = submission.manuscript_counter + 1
    manuscript_id = "man-%drev%d" % (manuscript_counter, revision)
    submission.invokeFactory(id=manuscript_id, type_name='Manuscript', title=manuscript_id, original=manuscript_file, revision=revision)
    #context.plone_log("manuscript_id %s" % manuscript_id)
    #context.plone_log("sub_id %s" % submission.id)
    submission.manage_changeProperties({'manuscript_counter':manuscript_counter})


if attachment_file:
    attachment_counter = submission.attachment_counter + 1
    attachment_id = "att-%drev%d" % (attachment_counter,revision)
    submission.invokeFactory(id=attachment_id, type_name='Attachment', title=attachment_id, original=attachment_file, revision=revision)
    submission.manage_changeProperties({'attachment_counter':attachment_counter})

dp.manage_changeProperties({'submission_counter':SUBMISSION_COUNTER})
#submission.reindexObject()
request.set('submission_view', dest)
return state
