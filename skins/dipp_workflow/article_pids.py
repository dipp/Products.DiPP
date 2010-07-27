## Script (Python) "instance_pids"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE
from Products.CMFCore.utils import getToolByName
portal = getToolByName(self, 'portal_url').getPortalObject()

"""
openflow = getToolByName(portal, 'portal_openflow')
workitems = openflow.Catalog(meta_type='Workitem')
PIDs = []
for workitem in workitems:
    wi = workitem.getObject()
    action = openflow.getUserActionsOnWorkitem(wi.instance_id,wi.id,request)
    if action:
        PIDs.append(wi.PID)
"""

catalog = getToolByName(portal, 'portal_catalog')
results = catalog.searchResults(portal_type='FedoraArticle')
articles = {}

for result in results:
    if result.getPID:
        articles[result.getPID] = result.getURL()
return articles
