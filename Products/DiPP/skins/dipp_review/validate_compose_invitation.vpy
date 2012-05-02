## Controller Validator "validate_compose_invitation"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters= reviewer_id=''
##title=Validates the contact form
##

if not reviewer_id:
    state.setError('reviewer_id', 'Select a reviewer.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')

else:
    return state

