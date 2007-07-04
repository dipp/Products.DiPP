file                    = context.REQUEST.get('file', None)
storageType             = context.REQUEST.get('storageType', None)
language                = context.REQUEST.get('language', None)
DDC                     = context.REQUEST.get('DDC', None)
title_value             = context.REQUEST.get('title_value', None)
title_lang              = context.REQUEST.get('title_lang', None)
author_firstName        = context.REQUEST.get('author_firstName', None)
author_lastName         = context.REQUEST.get('author_lastName', None)
subject                 = context.REQUEST.get('subject', None)
sc_subjectClassified    = context.REQUEST.get('sc_subjectClassifield', None)
sc_classificationIdent  = context.REQUEST.get('sc_classificationIdent', None)
sc_classificationSystem = context.REQUEST.get('sc_classificationSystem', None)
bc_journalTitle         = context.REQUEST.get('bc_journalTitle', None)
bc_journalVolume        = context.REQUEST.get('bc_journalVolume', None)
bc_journalIssueNumber   = context.REQUEST.get('bc_journalIssueNumber', None)
bc_journalIssueDate     = context.REQUEST.get('bc_journalIssueDate', None)
rights                  = context.REQUEST.get('rights', None)
created                 = context.REQUEST.get('created', None)
modified                = context.REQUEST.get('modified', None)
valid                   = context.REQUEST.get('valid', None)

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

if storageType == "permanent":

    if DDC[0] == "":
        state.setError('DDC', 'Es muß eine DDC-Sachgruppe angegeben werden', new_status='failure')

    if language[0] == "":
        state.setError('language', 'Es muß eine Sprache angegeben werden', new_status='failure')

    if author_firstName[0] == "" or author_lastName[0] == "":
        state.setError('creatorPerson', 'Es muß mindestens ein Autor mit Vor- und Nachnamen angegeben werden.', new_status='failure')

    if str(subject) == '[]':
        state.setError('subject', 'Bitte geben Sie Schlagworte ein.', new_status='failure')

    #if sc_subjectClassified[0] == "" or sc_classificationIdent[0] == "" or sc_classificationSystem[0] == "":
    #    state.setError('subjectClassified', 'Bitte geben Sie normierte Schlagworte ein.', new_status='failure')

    if created == '' or modified == '' or valid == '':
        state.setError('dates', 'Bitte Daten angeben', new_status='failure')
    if str(bc_journalTitle) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')
    if str(bc_journalVolume) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')
    if str(bc_journalIssueNumber) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')
    if str(bc_journalIssueDate) == '':
        state.setError('bibliographicCitation', 'Bitte füllen Sie das bibliographische Zitat vollständig aus.', new_status='failure')

    if rights[0] == '':
        state.setError('rights', 'Bitte wählen Sie eine Lizenz.', new_status='failure')

if title_value[0] == "" or title_lang[0] == "":
    state.setError('title', 'Es muß ein Titel und eine Sprache  angegeben werden', new_status='failure')


if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')
    #state.set(portal_status_message=convert_only)

"""
return state


