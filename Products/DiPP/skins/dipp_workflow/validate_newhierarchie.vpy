title      = context.REQUEST.get('title', None)
MetaType   = context.REQUEST.get('MetaType', None)
journalPID = context.REQUEST.get('journalPID', None)

if not title:
    state.setError('title', 'Please enter a title', new_status='failure')

if not MetaType:
    state.setError('MetaType', 'Please select a MetaType', new_status='failure')

if not journalPID:
    state.setError('journalPID', 'Please select a PID', new_status='failure')

if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')

return state


