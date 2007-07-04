newId     = context.REQUEST.get('newId', None)
isChildOf = context.REQUEST.get('isChildOf', None)
autor = context.REQUEST.get('autor', None)
autorOK_required = context.REQUEST.get('autorOK_required', None)
type = context.REQUEST.get('type', None)


if newId is not None:
    # PloneTool.contentEdit strips the id, so make sure we test the stripped version
    newId = newId.strip() 

if not newId:
    state.setError('newId', 'You must specify an Id.', new_status='failure')

if type == 'DiPP:article':
    if not autor and autorOK_required == True:
        state.setError('autor', 'You must specify an autor.', new_status='failure')

id_error = context.check_id(newId, 0, None)
if id_error:
    state.setError('newId', id_error, new_status='failure')


if not isChildOf:
    state.setError('isChildOf', 'You must specify a folder.', new_status='failure')

if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')

#print state
return state


