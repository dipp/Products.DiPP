## Script (Python) "getIdentifiers"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, prefix=None
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
articles   = container.portal_catalog(portal_type='FedoraArticle', sort_on='getIssueDate')

print "H:email=support@crossref.org;fromPrefix=%s;toPrefix=%s" % (prefix, prefix)
for article in articles:
    PID = article.getPID
    URL = article.getURL()
    qdc = fedora.getQualifiedDCMetadata(PID)
    DOI = qdc['identifierDOI']
    print "%s\t%s" % (DOI, URL)
return printed
