## Script (Python) "instance_pids"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=PID=None
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE
from Products.CMFCore.utils import getToolByName
portal = getToolByName(context, 'portal_url').getPortalObject()

# return a PID sorted dictionary with some basic metadata

catalog = getToolByName(portal, 'portal_catalog')
if PID:
    results = catalog.searchResults(portal_type='FedoraArticle', getPID=PID)
else:
    results = catalog.searchResults(portal_type='FedoraArticle')
articles = {}

for result in results:
    if result.getPID:
        articles[result.getPID] = {}
        articles[result.getPID]['url'] = result.getURL()
        articles[result.getPID]['title'] = result.Title
        articles[result.getPID]['state'] = result.review_state
return articles
