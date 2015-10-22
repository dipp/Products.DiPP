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

from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

doi_tool = getToolByName(self, 'portal_doiregistry')
catalog = getToolByName(self, 'portal_catalog')

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
startpage               = request.get('startpage', "")
endpage                 = request.get('endpage', "")
rights                  = request.get('rights', None)
dateSubmitted           = request.get('dateSubmitted', None)
dateAccepted            = request.get('dateAccepted', None)
dateCopyrighted         = request.get('dateCopyrighted', None)
identifierDOI           = request.get('identifierDOI', None)


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

    # DOI
    if identifierDOI:
        context.plone_log("validating %s" % identifierDOI)
        # check for correct prefix and allowed characters
        valid, message = doi_tool.validate_doi(identifierDOI)
        if not valid:
             state.setError('identifierDOI', translate('error_doi_invalid', default='DOI ist ungültig: ${msg}.', mapping={u'msg':message}, domain='qdc'), new_status='failure')
        
        # is the doi already in use
        elif identifierDOI.lower() in [d.lower() for d in catalog.uniqueValuesFor('getDOI') if d]:# lowercase doi, discard '' and None entries
            results = catalog(portal_type='FedoraArticle',getDOI=identifierDOI)
            urls = [article.getURL() for article in results]
            if self.absolute_url() not in urls:
                state.setError('identifierDOI', translate('error_doi_assigned', default="DOI ist bereits vergeben.", domain='qdc'), new_status='failure')
        else:
            datacite_status = doi_tool.get_url(identifierDOI)[0]
            if not datacite_status=='404':
                state.setError('identifierDOI', translate('error_doi_registered', default="DOI ist bereits registriert", domain='qdc'), new_status='failure')
    else:
        context.plone_log("skipping validation of DOI")
    
    #if rights[0] == '':
    if not rights:
        state.setError('rights', translate('error_licence_required', domain='qdc'), new_status='failure')

for aTitle in title:
    if aTitle['value'] == '' or aTitle['lang'] == '':
        state.setError('title', translate('error_title_required', domain='qdc'), new_status='failure')


if state.getErrors():
    state.set(portal_status_message=translate('error_fix_indicated_errors', domain='qdc'))
     
return state
