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
doi = REQUEST.get('DOI', None)
url = REQUEST.get('URL', None)

if REQUEST.has_key('form.button.post_metadata'):
    status_code, content = doi_tool.post_metadata(metadata)
    portal_status_message = "Antwort von DataCite: %s, %s" % (status_code, content)
    status = 'success'

if REQUEST.has_key('form.button.create_or_modify_doi'):
    status_code, content = doi_tool.create_or_modify_doi(doi,url)
    portal_status_message = "Antwort von DataCite: %s, %s" % (status_code, content)
    status = 'success'
    
else:
    portal_status_message = "nix passiert"
    status = 'failure'

# portal_status_message = translate('field-added', domain='qdc')

context.plone_utils.addPortalMessage(portal_status_message)
return state.set(status=status)
