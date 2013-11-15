##script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self


from Products.CMFCore.utils import getToolByName

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE

translate = context.translate

portal_url = getToolByName(context, 'portal_url')
portal = portal_url.getPortalObject()

fedora = getToolByName(context, 'fedora')

params = REQUEST.form

# add a few empty fields. Without those the Metadataobject would be not valid
params['alternative'] = [{'value':'','lang':''}]
params['DCTermsAbstract'] = []
params['creatorPerson'] = []
params['creatorCorporated'] = []
params['bibliographicCitation'] = [
    {'journalIssueDate':'',
     'journalIssueNumber':'',
     'journalTitle':'',
     'journalVolume':''}
]

# save to fedora 
fedora.setQualifiedDCMetadata(params)

# a few fields are also saved to plone for faster access
dp = portal.portal_properties.dipp_properties
mp = portal.portal_properties.metadata_properties

journalname = params.get('title_value',None)[0]
ISSN = params.get('identifierISSN',None)
context.plone_log(journalname)
mp.manage_changeProperties({'journalname':journalname})
dp.manage_changeProperties({'ISSN':ISSN})
# TODO: issn should also go to metadata_properties

msg = translate('settings_saved', domain='dipp')

context.plone_utils.addPortalMessage(msg)

if REQUEST:
     REQUEST.RESPONSE.redirect(REQUEST.HTTP_REFERER)
