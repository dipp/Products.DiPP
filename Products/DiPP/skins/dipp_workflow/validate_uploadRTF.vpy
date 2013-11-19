## Controlled Python Script "validate_upload_RTF"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Validates the rtf upload
##

request  = container.REQUEST
RESPONSE = request.RESPONSE

translate = context.translate

available_languages = self.portal_properties.metadata_properties.available_languages

file             = request.get('file', None)
article_title    = request.get('article_title', None)
article_language = request.get('article_language', None)

if not file:
    state.setError('file', translate('error_file_required', domain='qdc'), new_status='failure')
else:
    extension = file.filename.lower().split('.')[-1]
    if extension not in ['rtf', 'pdf', 'xml']:
        state.setError('file', translate('error_wrong_fileformat', domain='qdc'), new_status='failure')
    #'This seems not to be a RTF, PDF or XML file'
if article_title == "":
    state.setError('article_title', translate('error_title_required', domain='qdc'), new_status='failure')

if article_language not in available_languages:
    state.setError('article_language', translate('error_language_required', domain='qdc'), new_status='failure')

if state.getErrors():
    state.set(portal_status_message=translate('error_fix_indicated_errors', domain='qdc'))

return state
