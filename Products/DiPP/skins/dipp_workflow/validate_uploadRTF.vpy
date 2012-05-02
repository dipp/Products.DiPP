import string
file          = context.REQUEST.get('file', None)
title_value   = context.REQUEST.get('title_value', None)
title_lang    = context.REQUEST.get('title_lang', None)
LANGUAGE      = context.REQUEST.get('LANGUAGE', None)
if not file:
    if LANGUAGE == 'de':
        state.setError('file', 'Bitte eine Datei auswählen', new_status='failure')
    else:
        state.setError('file', 'Please select a file', new_status='failure')
else:
    extension = file.filename.lower().split('.')[-1]
    if extension not in ['rtf', 'pdf', 'xml']:
        state.setError('file', 'This seems not to be a RTF, PDF or XML file', new_status='failure')

if title_value[0] == "" or title_lang[0] == "":
    if LANGUAGE == 'de':
        state.setError('title', 'Es muß ein Titel und eine Sprache  angegeben werden', new_status='failure')
    else:
        state.setError('title', 'Please enter title and language', new_status='failure')
if state.getErrors():
    if LANGUAGE == 'de':
        state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')
    else:
        state.set(portal_status_message='Please correct the indicated errors!')
return state
