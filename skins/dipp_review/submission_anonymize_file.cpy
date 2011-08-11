## Controller Python Script "manuscript_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,file="", fileid
##title=
##
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
 
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

filename = file.filename

obj = getattr(self, fileid)
obj.setAnonym(file)
context.plone_log(obj.id)
state.set(portal_status_message='Anonymized file is uploaded')

return state
