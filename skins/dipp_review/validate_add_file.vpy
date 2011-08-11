## Controller Validator "validate_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters= file='', type=''
##title=Validates the contact form
##

if not file:
    state.setError('file', 'You did not select a file.', 'input_required')

if not type:
    state.setError('file', 'You did not select a file type.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')

else:
    return state

