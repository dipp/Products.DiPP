deadline_max     = context.REQUEST.get('deadline_max', None)
deadline_default = context.REQUEST.get('deadline_default', None)
deadline_yellow  = context.REQUEST.get('deadline_yellow', None)
deadline_red     = context.REQUEST.get('deadline_red', None)

if int(deadline_max) <= int(deadline_default):
    state.setError('deadline_default', 'The default deadline must be smaller than the maximum!', new_status='failure')

if int(deadline_yellow) <= int(deadline_red):
    state.setError('deadline_yellow', 'Yellow must be larger than Red!', new_status='failure')

#print state
return state


