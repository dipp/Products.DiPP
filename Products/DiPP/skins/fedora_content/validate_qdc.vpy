## Controlled Python Script "validate_qdc"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Validates qualified Dublin Core metadata
##

request  = container.REQUEST
RESPONSE = request.RESPONSE

translate = context.translate

file                    = request.get('file', None)
storageType             = request.get('storageType', None)
language                = request.get('language', None)
DDC                     = request.get('DDC', None)
title                   = request.get('title', None)
creatorPerson           = request.get('creatorPerson', None)
subject                 = request.get('subject', None)
subjectClassified       = request.get('subjectClassifield', None)
bibliographicCitation   = request.get('bibliographicCitation', None)
startpage               = request.get('startpage', None)
endpage                 = request.get('endpage', None)
rights                  = request.get('rights', None)
dateSubmitted           = request.get('dateSubmitted', None)
dateAccepted            = request.get('dateAccepted', None)
dateCopyrighted         = request.get('dateCopyrighted', None)

from DateTime import DateTime

def is_integer(pagenumber):
    try: 
        int(pagenumber)
        return True
    except ValueError:
        return False


if storageType == "permanent":

    for aDDC in DDC:
        if aDDC == "":
            state.setError('DDC', translate('error_ddc', domain='qdc'), new_status='failure')

    for aLanguage in language:
        if aLanguage == "":
            state.setError('language', translate('error_language_required', domain='qdc'), new_status='failure')
    
    for author in creatorPerson:
        if author['lastName'] == '' and author['firstName'] == '':
            state.setError('creatorPerson', translate('error_creatorperson', domain='qdc'), new_status='failure')

    if str(subject) == '[]':
        state.setError('subject', 'Bitte geben Sie Schlagworte ein.', new_status='failure')
    
    for date in (dateAccepted, dateCopyrighted, dateSubmitted):
        try:
            if date.strip() != '':
                x = DateTime(date)
        except:
            state.setError('dates', translate('error_dateformat', domain='qdc'), new_status='failure')
        
    # citation   
    citation = bibliographicCitation[0]
    
    for x in citation.keys():
        if citation[x] == '':
            state.setError('bibliographicCitation', translate('error_citation_required', domain='qdc'), new_status='failure')
    try:
        date = DateTime(citation['journalIssueDate'])
    except:
        state.setError('bibliographicCitation', translate('error_dateformat', domain='qdc'), new_status='failure')
        #context.plone_log(e)
    
    # pagenumbers
    for page in (startpage, endpage):
        if page and not is_integer(page):
            state.setError('bibliographicCitation', translate('error_pagenumber_integer', domain='qdc'), new_status='failure')
    
    if is_integer(startpage) and is_integer(endpage):
        if int(startpage) > int(endpage):
            state.setError('bibliographicCitation', translate('error_pagenumber_order', domain='qdc'), new_status='failure')
            
    
    #if rights[0] == '':
    if not rights:
        state.setError('rights', translate('error_licence_required', domain='qdc'), new_status='failure')

for aTitle in title:
    if aTitle['value'] == '' or aTitle['lang'] == '':
        state.setError('title', translate('error_title_required', domain='qdc'), new_status='failure')


if state.getErrors():
    state.set(portal_status_message=translate('error_fix_indicated_errors', domain='qdc'))
     
return state


