PID     = context.REQUEST.get('PID', None)
DsID    = context.REQUEST.get('DsID', None)
body    = context.REQUEST.get('body', None)
title   = context.REQUEST.get('title', None)
id   = context.REQUEST.get('id', None)
#MIMEType = context.REQUEST.get('MIMEType', None)

"""
# check for PID
if context.fedoraSearch('PID','has',PID) == 'FALSE' :
    state.setError('PID', 'PID does not exist in Fedora database', new_status='failure')

try:
    ids = []
    for ds in context.fedoraGetdatastreams(PID):
        ids.append(ds['ID'])

    if DsID not in ids:
        state.setError('DsID', 'The Datastream id does not exist in this Object', new_status='failure')
except:
    pass
    
"""
if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')
     
return state


