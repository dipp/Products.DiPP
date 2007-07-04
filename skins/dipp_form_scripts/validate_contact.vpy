## Controller Validator "validate_submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters= name=''
##title=Validates the contact form
##

if not name:
    state.setError('name', 'Please give your full name.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')

else:
    return state

