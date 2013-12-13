## Controlled Python Script "validate_qdc_title"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Validates qualified Dublin Core metadata
##

request  = container.REQUEST
RESPONSE = request.RESPONSE

translate = context.translate

storageType             = request.get('storageType', None)
titles                   = request.get('title', None)

for title in titles:
    if title['value'].strip() == '' or title['lang'] == '':
        state.setError('title', translate('error_title_required', domain='qdc'), new_status='failure')

if state.getErrors():
    state.set(portal_status_message=translate('error_fix_indicated_errors', domain='qdc'))
     
return state


