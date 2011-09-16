## Script (Python) "crossref_update"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, prefix=None, metadata=0
##title=
##

# -*- coding: utf-8 -*-
"""
Update von Crossref DOIs gemäß
http://www.crossref.org/help/Content/06_Maintaining%20DOIs/URL_update.htm
Dieses Script erzeugt eine mit Tab getrennt Liste mit DOIs und URLs.
Voraussetzung ist eine korrekte DOI in den QDC Metadaten.
Das Prefix sollte dem script beim Aufruf übergeben werden
"""

from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
fedora = getToolByName(self,'fedora')
portal     = portal_url.getPortalObject()
articles   = container.portal_catalog(portal_type='FedoraArticle', sort_on='getIssueDate', Language="all")
print "H:email=support@crossref.org;fromPrefix=%s;toPrefix=%s" % (prefix, prefix)
for article in articles:
    PID = article.getPID
    URL = article.getURL()
    obj = article.getObject()
    qdc = fedora.getQualifiedDCMetadata(PID)
    DOI = qdc['identifierDOI']
    title = qdc['title'][0]['value']
    authors = article.getAuthors
    published = article.getIssueDate
    pdf = obj.getFulltextPdf()
    if pdf:
        URL = pdf['URL']
    else:
        URL = ""
    if int(metadata) == 1:
        print "%s\t%s\t%s\t%s\t%s" % (DOI, URL, title, published, "\t".join(authors))
    else:
        print "%s\t%s" % (DOI, URL)
        
return printed
