## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,file="",type=""
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
wtool = getToolByName(self, 'portal_workflow')

revision = int(wtool.getInfoFor(self, 'revision', 0))
context.plone_log("Revision %d" % revision)

if type == 'Manuscript':
    manuscript_counter = self.manuscript_counter + 1
    manuscript_id = "man-%drev%d" % (manuscript_counter, revision)
    self.invokeFactory(id=manuscript_id, type_name='Manuscript', title=manuscript_id, original=file, revision=revision)
    self.manage_changeProperties({'manuscript_counter':manuscript_counter})

if type == 'Attachment':
    attachment_counter = self.attachment_counter + 1
    attachment_id = "att-%drev%d" % (attachment_counter,revision)
    self.invokeFactory(id=attachment_id, type_name='Attachment', title=attachment_id, original=file,revision=revision)
    self.manage_changeProperties({'attachment_counter':attachment_counter})

state.set(portal_status_message='File is uploaded')

return state
