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
startpage               = context.REQUEST.get('startpage', None)
endpage                 = context.REQUEST.get('endpage', None)
rights                  = context.REQUEST.get('rights', None)
dateSubmitted           = context.REQUEST.get('dateSubmitted', None)
dateAccepted            = context.REQUEST.get('dateAccepted', None)
dateCopyrighted         = context.REQUEST.get('dateCopyrighted', None)

from DateTime import DateTime

def is_integer(pagenumber):
    try: 
        int(pagenumber)
        return True
    except ValueError:
        return False


if storageType == "permanent":

    if DDC[0] == "":
        state.setError('DDC', 'Es muß eine DDC-Sachgruppe angegeben werden', new_status='failure')

    if language[0] == "":
        state.setError('language', 'Es muß eine Sprache angegeben werden', new_status='failure')

    if creatorPerson[0]['firstName'] == "" or creatorPerson[0]['lastName'] == "":
        state.setError('creatorPerson', 'Es muß mindestens ein Autor mit Vor- und Nachnamen angegeben werden.', new_status='failure')

    if str(subject) == '[]':
        state.setError('subject', 'Bitte geben Sie Schlagworte ein.', new_status='failure')
    
    for date in (dateAccepted, dateCopyrighted, dateSubmitted):
        try:
            if date.strip() != '':
                x = DateTime(date)
        except:
            state.setError('dates', 'Falsches Datumsformat, verwenden Sie JJJJ-MM-TT', new_status='failure')
        
        
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
    
    # pagenumbers
    if startpage and not is_integer(startpage):
        state.setError('bibliographicCitation', 'Seitenzahlen sind ganze Zahlen.', new_status='failure')
    if endpage and not is_integer(endpage):
        state.setError('bibliographicCitation', 'Seitenzahlen sind ganze Zahlen.', new_status='failure')
    
    if is_integer(startpage) and is_integer(endpage):
        if int(startpage) > int(endpage):
            state.setError('bibliographicCitation', 'Erste Seite ist grüßer als zweite seite.', new_status='failure')
            
    
    #if rights[0] == '':
    if not rights:
        state.setError('rights', 'Bitte wählen Sie eine Lizenz.', new_status='failure')

if title_value[0] == "" or title_lang[0] == "":
    state.setError('title', 'Es muß ein Titel und eine Sprache  angegeben werden', new_status='failure')


if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')
    #state.set(portal_status_message=convert_only)
     
return state


