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

fedora = getToolByName(context, 'fedora')

params = REQUEST.form
params['alternative']= [{'value':'','lang':''}]
params['DCTermsAbstract']= []
params['creatorPerson']= []
params['creatorCorporated']= []
params['bibliographicCitation'] = [{'journalIssueDate':'','journalIssueNumber':'','journalTitle':'','journalVolume':''}]
fedora.setQualifiedDCMetadata(params)

portal_status_message = "Änderungen wurden gespeichert"

if REQUEST:
     REQUEST.RESPONSE.redirect(REQUEST.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
