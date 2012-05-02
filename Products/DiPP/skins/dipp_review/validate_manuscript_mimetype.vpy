## Controller Validator "validate_manuscript_mimetype"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self, manuscript_file=''
##title=Validates the contact form
##

from Products.CMFCore.utils import getToolByName

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()


if not manuscript_file:
    state.setError('manuscript_file', 'Please upload a manuscript.', 'input_required')
else:
    mimetype = manuscript_file.headers['Content-Type']
    allowed_mimetypes = portal.portal_properties.dippreview_properties.manuscript_mimetypes
    if mimetype not in allowed_mimetypes:
        state.setError('manuscript_file', 'Filetype %s is not allowed.'%mimetype, 'input_required')


if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')

else:
    return state

