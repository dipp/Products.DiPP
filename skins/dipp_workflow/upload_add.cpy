##script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id=''

REQUEST = context.REQUEST

# add DDC
if REQUEST.form.has_key('form.button.addDDC'):
    newDDCNumber =int(REQUEST.get('newDDCNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues DDC-Feld wurde hinzugefügt')
else:
    newDDCNumber =int(REQUEST.get('newDDCNumber',None))

#add Title
if REQUEST.form.has_key('form.button.addTitle'):
    newTitleNumber =int(REQUEST.get('newTitleNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues Titel-Feld wurde hinzugefügt')
else:
    newTitleNumber =int(REQUEST.get('newTitleNumber',None))

#add Alternative
if REQUEST.form.has_key('form.button.addAlternative'):
    newAlternativeNumber =int(REQUEST.get('newAlternativeNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues Alternativ-Feld wurde hinzugefügt')
else:
    newAlternativeNumber =int(REQUEST.get('newAlternativeNumber',None))
#add Author
if REQUEST.form.has_key('form.button.addAuthor'):
    newAuthorNumber =int(REQUEST.get('newAuthorNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues Autoren-Feld wurde hinzugefügt')
else:
    newAuthorNumber =int(REQUEST.get('newAuthorNumber',None))

#add Abstract
if REQUEST.form.has_key('form.button.addAbstract'):
    newAbstractNumber =int(REQUEST.get('newAbstractNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues Abstract-Feld wurde hinzugefügt')
else:
   newAbstractNumber = int(REQUEST.get('newAbstractNumber',None))
    #newAbstractNumber = REQUEST.get('newAbstractNumber',None)
    #newAbstractNumber = 2

#add CorporateAuthor
if REQUEST.form.has_key('form.button.addCorporateAuthor'):
    newCorporateAuthorNumber =int(REQUEST.get('newCorporateAuthorNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues CorporateAutoren-Feld wurde hinzugefügt')
else:
    newCorporateAuthorNumber =int(REQUEST.get('newCorporateAuthorNumber',None))

#add Keyword
if REQUEST.form.has_key('form.button.addKeyword'):
    newSubjectClassifiedNumber =int(REQUEST.get('newSubjectClassifiedNumber',None)) + 1
    portal_status_message = REQUEST.get('portal_status_message', 'Neues Schlagword-Feld wurde hinzugefügt')
else:
    newSubjectClassifiedNumber =int(REQUEST.get('newSubjectClassifiedNumber',None))

subjects = REQUEST.get('subject',None)
print 'LEN',len(subjects)
subject = ""
for i in subjects:
    subject += i + "\n" 
subject = [subject]

return state.set(status='success',\
    portal_status_message=portal_status_message,\
    newDDCNumber=newDDCNumber,
    newTitleNumber=newTitleNumber,
    newAlternativeNumber=newAlternativeNumber,
    newAuthorNumber=newAuthorNumber,
    newAbstractNumber=newAbstractNumber,
    newSubjectClassifiedNumber=newSubjectClassifiedNumber,
    storageType                = REQUEST.get('storageType',None),
    DDC                        = REQUEST.get('DDC',None),
    language                   = REQUEST.get('language',None),
    targetFormat               = REQUEST.get('targetFormat',None),
    title_value                = REQUEST.get('title_value',None),
    title_lang                 = REQUEST.get('title_lang',None),
    alternative_value          = REQUEST.get('alternative_value',None),
    alternative_lang           = REQUEST.get('alternative_lang',None),
    abstract_lang              = REQUEST.get('abstract_lang',None),
    abstract_value             = REQUEST.get('abstract_value',None),
    subjects                   = REQUEST.get('subjects',None),
    author_academicTitle       = REQUEST.get('author_academicTitle',None),
    author_firstName           = REQUEST.get('author_firstName',None),
    author_lastName            = REQUEST.get('author_lastName',None),
    author_emailAddress        = REQUEST.get('author_emailAddress',None),
    author_PNDIdentNumber      = REQUEST.get('author_PNDIdentNumber',None),
    author_organization        = REQUEST.get('author_organization',None),
    author_postalAddress       = REQUEST.get('author_postalAddress',None),
    corp_institutionelAuthor   = REQUEST.get('corp_institutionelAuthor',None),
    corp_emailAddress          = REQUEST.get('corp_emailAddress',None),
    corp_organization          = REQUEST.get('corp_organization',None),
    corp_postalAddress         = REQUEST.get('corp_postalAddress',None),
    corp_GKDIdentNumber        = REQUEST.get('corp_GKDIdentNumber',None),
    contrib_academicTitle      = REQUEST.get('contrib_academicTitle',None),
    contrib_firstName          = REQUEST.get('contrib_firstName',None),
    contrib_lastName           = REQUEST.get('contrib_lastName',None),
    contrib_emailAddress       = REQUEST.get('contrib_emailAddress',None),
    contrib_PNDIdentNumber     = REQUEST.get('contrib_PNDIdentNumber',None),
    contrib_role               = REQUEST.get('contrib_role',None),
    contrib_organization       = REQUEST.get('contrib_organization',None),
    contrib_postalAddress      = REQUEST.get('contrib_postalAddress',None),
    created                    = REQUEST.get('created',None),
    modified                   = REQUEST.get('modified',None),
    valid                      = REQUEST.get('valid',None),
    articleType                = REQUEST.get('articleType',None),
    subject                    = subject,
    sc_subjectClassified       = REQUEST.get('sc_subjectClassified',None),
    sc_classificationIdent     = REQUEST.get('sc_classificationIdent',None),
    sc_classificationSystem    = REQUEST.get('sc_classificationSystem',None),
    dateAccepted               = REQUEST.get('dateAccepted',None),
    dateSubmitted              = REQUEST.get('dateSubmitted',None),
    dateCopyrighted            = REQUEST.get('dateCopyrighted',None),
    bc_journalTitle            = REQUEST.get('bc_journalTitle',None),
    bc_journalVolume           = REQUEST.get('bc_journalVolume',None),
    bc_journalIssueNumber      = REQUEST.get('bc_journalIssueNumber',None),
    bc_journalIssueDate        = REQUEST.get('bc_journalIssueDate',None),
    identifierDOI              = REQUEST.get('identifierDOI',None),
    pubType                    = REQUEST.get('pubType',None),
    docType                    = REQUEST.get('docType',None),
    rights                     = REQUEST.get('rights',[])
)