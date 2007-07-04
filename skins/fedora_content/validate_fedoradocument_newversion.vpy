PID     = context.REQUEST.get('PID', None)
DsID    = context.REQUEST.get('DsID', None)
LogMessage    = context.REQUEST.get('LogMessage', None)

# Überarbeiten!! ist arbeitsversion mit fedoraversio identisch
#
#if context.fedoraAccess(PID,DsID,Date=None)['stream'] == "leer":
#    message = """
#    Es wurde keine neue Version angelegt!
#    Die derzeitige Arbeitsversion ist identisch mit der letzten gespeicherten Version.
#    """
#    state.set(portal_status_message=message)
#    state.setError('','',new_status='failure') 
#    return state

if LogMessage == "":
    state.setError('LogMessage', 'Bitte eine aussagekräftige Beschreibung der Änderungen hinterlassen', new_status='failure')


if state.getErrors():
    message ="Bitte die angezeigten Fehler korrigieren!"
    state.set(portal_status_message=message)
#print state
return state

