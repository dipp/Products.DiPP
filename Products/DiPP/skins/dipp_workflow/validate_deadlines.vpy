deadline_max     = context.REQUEST.get('deadline_max', None)
deadline_default = context.REQUEST.get('deadline_default', None)
deadline_yellow  = context.REQUEST.get('deadline_yellow', None)
deadline_red = context.REQUEST.get('deadline_red', None)

#MAX
if not deadline_max:
    state.setError('deadline_max', 'Please enter a value', new_status='failure')
    max=-1
else:
    try:
        max = int(deadline_max)
    except ValueError:
        max=-1
        state.setError('deadline_max', 'Please enter an integer',new_status='failure')

#DEFAULT
if not deadline_default:
    state.setError('deadline_default', 'Please enter a value', new_status='failure')
    default = -1
else:
    try:
        default = int(deadline_default)
    except ValueError:
        default = -1
        state.setError('deadline_default', 'Please enter an integer',new_status='failure')


if default != -1 and max != -1:
    if max <= default:
        state.setError('deadline_default', 'The default deadline must be smaller than the maximum!', new_status='failure')


#YELLOW
if not deadline_yellow:
    state.setError('deadline_yellow', 'Please enter a value', new_status='failure')
    yellow = -1
else:
    try:
        yellow = int(deadline_yellow)
    except ValueError:
        yellow = -1
        state.setError('deadline_yellow', 'Please enter an integer',new_status='failure')

#RED
if not deadline_red:
    state.setError('deadline_red', 'Please enter a value', new_status='failure')
    red = -1
else:
    try:
        red = int(deadline_red)
    except ValueError:
        red = -1
        state.setError('deadline_red', 'Please enter an integer',new_status='failure')

if red != -1 and yellow != -1:
   if yellow <= red:
        state.setError('deadline_red', 'The red deadline must be smaller than the yellow!', new_status='failure')


if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')

#print state
return state


