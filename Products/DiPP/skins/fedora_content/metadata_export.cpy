## Controller Python Script "metadata_export"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Edit content
##
from Products.CMFCore.utils import getToolByName

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
translate = context.translate

doi_tool = getToolByName(self, 'portal_doiregistry')

metadata = REQUEST.metadata

status, content = doi_tool.post_metadata(metadata)

# portal_status_message = translate('field-added', domain='qdc')
portal_status_message = "Antwort von DataCite: %s, %s" % (status, content)
context.plone_utils.addPortalMessage(portal_status_message)
return state.set(status='success')
