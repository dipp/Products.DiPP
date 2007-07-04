## Controller Validator "validate_submitemail"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=file='', licence=''
##title=Validates the submit
##

if not file:
    state.setError('file', 'Select a file on your harddisk for upload.', 'input_required')

if not licence:
    state.setError('licence', 'Please agree to the licence.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')

else:
    return state
