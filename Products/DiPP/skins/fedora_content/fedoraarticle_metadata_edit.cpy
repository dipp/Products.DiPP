##script (Python) "fedoraarticle_metadata_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id=''

REQUEST = context.REQUEST
translate = context.translate
portal_status_message = ""

def del_from_list(old_list, selection):
    """the item with numbers from selection are deletet from list"""
    new_list = []
    for i in range(0, len(old_list)):
        if i not in selection:
            new_list.append(old_list[i])
    return new_list


# add DDC
DDC = REQUEST.get('DDC',([],)),
DDC = DDC[0]
if REQUEST.form.has_key('form.button.addDDC'):
    DDC.append('')
    portal_status_message = translate('field-added', domain='qdc')
if REQUEST.form.has_key('form.button.delDDC'):
    ddc_index = REQUEST.get('ddc_index',[])
    DDC = del_from_list(DDC,ddc_index)
    if len(DDC) == 0:
        DDC.append('') 
    portal_status_message = translate('field-removed', domain='qdc')

#add Title
default = {'value':'','lang':''}
title = REQUEST.get('title',None)
if REQUEST.form.has_key('form.button.addTitle'):
    title.append(default)
    portal_status_message = translate('field-added', domain='qdc')

if REQUEST.form.has_key('form.button.delTitle'):
    title_index = REQUEST.get('title_index',[])
    title = del_from_list(title,title_index)
    if len(title) == 0:
        title.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

#add Alternative
default = {'value':'','lang':''}
alternative = REQUEST.get('alternative',None)
if REQUEST.form.has_key('form.button.addAlternative'):
    alternative.append(default)
    portal_status_message = translate('field-added', domain='qdc')

if REQUEST.form.has_key('form.button.delAlternative'):
    alternative_index = REQUEST.get('alternative_index',[])
    alternative = del_from_list(alternative,alternative_index)
    if len(alternative) == 0:
        alternative.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

# add Abstract
default = {'value':'','lang':''}
DCTermsAbstract = REQUEST.get('DCTermsAbstract',None)
if REQUEST.form.has_key('form.button.addAbstract'):
    DCTermsAbstract.append(default)
    portal_status_message = translate('field-added', domain='qdc')

if REQUEST.form.has_key('form.button.delAbstract'):
    abstract_index = REQUEST.get('abstract_index',[])
    DCTermsAbstract = del_from_list(DCTermsAbstract,abstract_index)
    if len(DCTermsAbstract) == 0:
        DCTermsAbstract.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

# add Author
creatorPerson = REQUEST.get('creatorPerson',None)
default = {'organization': '', 'firstName': '', 'GKDIdentNumber': '', 'lastName': '', 'emailAddress': '', 'PNDIdentNumber': '', 'academicTitle': '', 'postalAddress': '', 'role': '', 'institutionelAuthor':'' }
if REQUEST.form.has_key('form.button.addAuthor'):
    creatorPerson.append(default)
    portal_status_message =translate('field-added', domain='qdc')

# del Author
if REQUEST.form.has_key('form.button.delAuthor'):
    author_index = REQUEST.get('author_index',[])
    creatorPerson = del_from_list(creatorPerson,author_index)
    if len(creatorPerson) == 0:
        creatorPerson.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

# add corp author
creatorCorporated = REQUEST.get('creatorCorporated',None)
default = {'organization': '', 'firstName': '', 'GKDIdentNumber': '', 'lastName': '', 'emailAddress': '', 'PNDIdentNumber': '', 'academicTitle': '', 'postalAddress': '', 'role': '', 'institutionelAuthor':'' }
if REQUEST.form.has_key('form.button.addCorp'):
    creatorCorporated.append(default)
    portal_status_message = translate('field-added', domain='qdc')

# del corp Author
if REQUEST.form.has_key('form.button.delCorp'):
    corp_index = REQUEST.get('corp_index',[])
    creatorCorporated = del_from_list(creatorCorporated,corp_index)
    if len(creatorCorporated) == 0:
        creatorCorporated.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

# add Contrbutor
contributor = REQUEST.get('contributor',None)
default = {'organization': '', 'firstName': '', 'GKDIdentNumber': '', 'lastName': '', 'emailAddress': '', 'PNDIdentNumber': '', 'academicTitle': '', 'postalAddress': '', 'role': '', 'institutionelAuthor':'' }
if REQUEST.form.has_key('form.button.addContributor'):
    contributor.append(default)
    portal_status_message = translate('field-added', domain='qdc')

# del Contributor
if REQUEST.form.has_key('form.button.delContributor'):
    contributor_index = REQUEST.get('contributor_index',[])
    contributor = del_from_list(contributor,contributor_index)
    if len(contributor) == 0:
        contributor.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

# add Keyword
subjectClassified = REQUEST.get('subjectClassified',None)
default = {'classificationIdent': '', 'classificationSystem': '', 'subjectClassified': ''}
if REQUEST.form.has_key('form.button.addKeyword'):
    subjectClassified.append(default)
    portal_status_message = translate('field-added', domain='qdc')

# del Keyword
if REQUEST.form.has_key('form.button.delKeyword'):
    keyword_index = REQUEST.get('keyword_index',[])
    subjectClassified = del_from_list(subjectClassified,keyword_index)
    if len(subjectClassified ) == 0:
        subjectClassified.append(default) 
    portal_status_message = translate('field-removed', domain='qdc')

subjects = REQUEST.get('subject',[])
subject = ""
for i in subjects:
    subject += i + "\n" 
subject = [subject]

context.plone_utils.addPortalMessage(portal_status_message)
return state.set(status='success',\
    storageType                = REQUEST.get('storageType',None),
    DDC                        = DDC,
    language                   = REQUEST.get('language',None),
    targetFormat               = REQUEST.get('targetFormat',None),
    alternative                = alternative,
    title                      = title,
    DCTermsAbstract            = DCTermsAbstract,
    subjects                   = REQUEST.get('subjects',None),
    creatorPerson              = creatorPerson,
    creatorCorporated          = creatorCorporated,
    contributor                = contributor,
    created                    = REQUEST.get('created',None),
    modified                   = REQUEST.get('modified',None),
    valid                      = REQUEST.get('valid',None),
    articleType                = REQUEST.get('articleType',None),
    new_subjects               = REQUEST.get('new_subjects',None),
    subjectClassified          = subjectClassified,
    dateAccepted               = REQUEST.get('dateAccepted',None),
    dateSubmitted              = REQUEST.get('dateSubmitted',None),
    dateCopyrighted            = REQUEST.get('dateCopyrighted',None),
    bibliographicCitation      = REQUEST.get('bibliographicCitation',None),
    pubType                    = REQUEST.get('pubType',None),
    docType                    = REQUEST.get('docType',None),
    rights                     = REQUEST.get('rights',[])
)

