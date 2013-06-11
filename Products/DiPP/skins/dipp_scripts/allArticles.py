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
articles   = container.portal_catalog(portal_type='FedoraArticle', Language='all', sort_on='getPID')
# articles   = container.portal_catalog(portal_type='FedoraArticle')


PIDs = []
for article in articles:
    try:
        PID = article.getObject().PID
    except:
        PID = "dipp:XXXX"
    PIDs.append((PID, article.getURN, article.review_state, article.getURL(), article.Title))


uniquePIDs = {}
multiPIDs = {}

urls = {}
for PID, URN, state, url, title in PIDs:
    if not PID in uniquePIDs:
        uniquePIDs[PID] = url
    elif PID in multiPIDs:
        multiPIDs[PID].append(url)
    else:
        multiPIDs[PID] = [url]

for PID in multiPIDs.keys():
    multiPIDs[PID].append(uniquePIDs[PID])


print "# nur sichtbare und veröffentlichte Artikel werden angezeigt."
print "# Private Artikel erscheinen nur für authentifizierte Manager."
print "# PIDs:", len(PIDs)
print "# unique PIDs:", len(uniquePIDs)
print "# doubles"
for PID in multiPIDs.keys():
    print PID
    for url in multiPIDs[PID]:
        print "    " + url
print "# all articles"
for PID, URN, state, url, title in PIDs:
    print "; ".join((PID, URN, state, title, url))

response.headers['Content-disposition'] = 'attachment; filename=alle-artikel.txt'
response.headers['Content-type'] = 'text/plain; charset="utf-8'
return printed

