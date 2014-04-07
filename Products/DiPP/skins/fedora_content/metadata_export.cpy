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
# doi = REQUEST.get('DOI', None)

url = self.absolute_url()
doi = self.getDOI()

if REQUEST.has_key('form.button.register'):
    # registering an article with DataCite is a two-step-process:
    # 1. uploading the metadata and thus minting an doi
    # 2. registering an url with the doi
    status_code, content = doi_tool.post_metadata(metadata)
    if status_code == '201':
        status_code, content = doi_tool.create_or_modify_doi(doi,url)
        if status_code == '201':
            status = 'success'
            msg = "DOI erfolgreich registriert"
        else:
            status = 'failure'
            msg = "DOI konnte nicht registriert werden!"
    portal_status_message = "%s (DataCite: %s, %s)" % (msg, status_code, content)


elif REQUEST.has_key('form.button.post_metadata'):
    status_code, content = doi_tool.post_metadata(metadata)
    if status_code == '201':
        status = 'success'
        msg = 'Metadata erfolgreich aktualisiert'
    else:
        status = 'failure'
        msg = 'Metadata nicht aktualisiert'
    portal_status_message = "%s (DataCite: %s, %s)" % (msg, status_code, content)

elif REQUEST.has_key('form.button.create_or_modify_doi'):
    status_code, content = doi_tool.create_or_modify_doi(doi,url)
    context.plone_log('new url: %s' % url)
    if status_code == '201':
        status = 'success'
        msg = 'URL erfolgreich aktualisiert'
    else:
        status = 'failure'
        msg = 'URL nicht aktualisiert'
    portal_status_message = "%s (DataCite: %s, %s)" % (msg, status_code, content)
        
    
else:
    portal_status_message = "nix passiert"
    status = 'failure'

# portal_status_message = translate('field-added', domain='qdc')

context.plone_utils.addPortalMessage(portal_status_message)
return state.set(status=status)
