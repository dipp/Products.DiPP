file                    = context.REQUEST.get('file', None)
storageType             = context.REQUEST.get('storageType', None)
language                = context.REQUEST.get('language', None)
DDC                     = context.REQUEST.get('DDC', None)
title_value             = context.REQUEST.get('title_value', None)
title_lang              = context.REQUEST.get('title_lang', None)
creatorPerson           = context.REQUEST.get('creatorPerson', None)
subject                 = context.REQUEST.get('subject', None)
subjectClassified       = context.REQUEST.get('subjectClassifield', None)
bibliographicCitation   = context.REQUEST.get('bibliographicCitation', None)
rights                  = context.REQUEST.get('rights', None)
created                 = context.REQUEST.get('created', None)
modified                = context.REQUEST.get('modified', None)
valid                   = context.REQUEST.get('valid', None)

from DateTime import DateTime

"""
filename = file.filename
if filename == "":
    state.setError('file', 'Es muß eine Datei zum hochladen ausgewählt werden.', new_status='failure')
else:
    try:
        extension = filename.split(".")[-1]
        if extension not in ('rtf','xml'):
            state.setError('file', 'Nur rtf oder xml.', new_status='failure')
    except:
        pass
"""
if storageType == "permanent":

    if DDC[0] == "":
        state.setError('DDC', 'Es muß eine DDC-Sachgruppe angegeben werden', new_status='failure')

    if language[0] == "":
        state.setError('language', 'Es muß eine Sprache angegeben werden', new_status='failure')

    if creatorPerson[0]['firstName'] == "" or creatorPerson[0]['lastName'] == "":
        state.setError('creatorPerson', 'Es muß mindestens ein Autor mit Vor- und Nachnamen angegeben werden.', new_status='failure')

    if str(subject) == '[]':
        state.setError('subject', 'Bitte geben Sie Schlagworte ein.', new_status='failure')

    if  created == '' or modified == '' or valid == '':
        state.setError('dates', 'Bitte Daten angeben', new_status='failure')

    try:
        if created != '':
            date = DateTime(created)
    except:
        state.setError('dates', 'Falsches Format', new_status='failure')
        
    try:
        if modified != '':
            date = DateTime(modified)
    except:
        state.setError('dates', 'Falsches Format', new_status='failure')
        
    try:
        if valid != '':
            date = DateTime(valid)
    except:
        state.setError('dates', 'Falsches Format', new_status='failure')

        
    bc = bibliographicCitation[0]
    if str(bc['journalTitle']) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')
    if str(bc['journalVolume']) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')
    if str(bc['journalIssueDate']) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')
    else:
        try:
            date = DateTime(bc['journalIssueDate'])
        except:
            state.setError('bibliographicCitation', 'Falsches Datumsformat.', new_status='failure')
        
    #if rights[0] == '':
    if not rights:
        state.setError('rights', 'Bitte wählen Sie eine Lizenz.', new_status='failure')

if title_value[0] == "" or title_lang[0] == "":
    state.setError('title', 'Es muß ein Titel und eine Sprache  angegeben werden', new_status='failure')


if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')
    #state.set(portal_status_message=convert_only)
     
return state


