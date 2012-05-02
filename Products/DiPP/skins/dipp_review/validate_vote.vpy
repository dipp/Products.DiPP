## Controller Validator "validate_vote"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=vote=''
##title=Validates the contact form
##

if not vote:
    state.setError('vote', 'Please place your vote.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')
else:
    return state

