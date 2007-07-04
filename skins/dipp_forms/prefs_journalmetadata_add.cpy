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
    newSubjectClassifiedNumber=newSubjectClassifiedNumber,
    identifierISSN             = REQUEST.get('identifierISSN',None),
    identifierURL              = REQUEST.get('identifierURL',None),
    DDC                        = REQUEST.get('DDC',None),
    language                   = REQUEST.get('language',None),
    title_value                = REQUEST.get('title_value',None),
    title_lang                 = REQUEST.get('title_lang',None),
    alternative_value          = REQUEST.get('alternative_value',None),
    alternative_lang           = REQUEST.get('alternative_lang',None),
    corp_firstName             = REQUEST.get('corp_firstName',None),
    corp_lastName              = REQUEST.get('corp_lastName',None),
    corp_emailAddress          = REQUEST.get('corp_emailAddress',None),
    corp_organization          = REQUEST.get('corp_organization',None),
    corp_postalAddress         = REQUEST.get('corp_postalAddress',None),
    corp_GKDIdentNumber        = REQUEST.get('corp_GKDIdentNumber',None),
    corp_PNDIdentNumber        = REQUEST.get('corp_PNDIdentNumber',None),
    corp_academicTitle         = REQUEST.get('corp_academicTitle',None),
    corp_institutionelAuthor   = REQUEST.get('corp_institutionelAuthor',None),
    corp_role                  = REQUEST.get('corp_role',None),
    subject                    = subject,
    sc_subjectClassified       = REQUEST.get('sc_subjectClassified',None),
    sc_classificationIdent     = REQUEST.get('sc_classificationIdent',None),
    sc_classificationSystem    = REQUEST.get('sc_classificationSystem',None),
    dateAccepted               = REQUEST.get('dateAccepted',None),
    dateSubmitted              = REQUEST.get('dateSubmitted',None),
    dateCopyrighted            = REQUEST.get('dateCopyrighted',None),
    publisher                  = REQUEST.get('publisher',None)
)
