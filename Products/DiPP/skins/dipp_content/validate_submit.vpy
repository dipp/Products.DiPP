username = context.REQUEST.get('username', None)
password = context.REQUEST.get('password', None)



if not username:
    state.setError('username', 'Missing username.', new_status='failure')

if not password:
    state.setError('password', 'Missing password.', new_status='failure')

auth = context.LDAPAuth(username,password)

if password and auth != True:
    state.setError('password', 'Wrong password.', new_status='failure')

if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')

#print state
return state


