## Script (Python) "allArticles"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
response = request.RESPONSE

portal_url = getToolByName(context, 'portal_url')
portal     = portal_url.getPortalObject()
articles   = container.portal_catalog(portal_type='FedoraArticle', sort_on='getPID')
# articles   = container.portal_catalog(portal_type='FedoraArticle')


PIDs = []
for article in articles:
    try:
        PID = article.getObject().PID
    except:
        PID = "dipp:XXXX"
    PIDs.append((PID, article.review_state, article.getURL(), article.Title))


uniquePIDs = {}
multiPIDs = {}

urls = {}
for PID, state, url, title in PIDs:
    if not PID in uniquePIDs:
        uniquePIDs[PID] = url
    elif PID in multiPIDs:
        multiPIDs[PID].append(url)
    else:
        multiPIDs[PID] = [url]

for PID in multiPIDs.keys():
    multiPIDs[PID].append(uniquePIDs[PID])


print "PIDs", len(PIDs)
print "unique PIDs:", len(uniquePIDs)
print "doubles"
for PID in multiPIDs.keys():
    print PID
    for url in multiPIDs[PID]:
        print "    " + url
print "all articles"
for PID, state, url, title in PIDs:
    print PID, state, title, url
return printed

