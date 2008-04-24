## Script (Python) "URLcheck"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, fix=0
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
fedora     = getToolByName(self, 'fedora')
portal     = portal_url.getPortalObject()
articles   = container.portal_catalog(portal_type='FedoraArticle',sort_on='Date', review_state=['visible','published'])

print '#', len(articles)
print 'fix:', fix

for article in articles:
    obj       = article.getObject()
    PID       = obj.PID
    ploneURL  = obj.absolute_url()
    fedoraURL = fedora.getQualifiedDCMetadata(PID)['identifierURL']
    
    if ploneURL == fedoraURL:
        OK = "OK"
    else:
        if fix == "1":
            fedora.setURL(PID, ploneURL)
            OK = "FIXED"
        else:
            OK = "BROKEN"
    
    print PID, OK
    print "\t p",ploneURL
    print "\t f",fedoraURL
return printed
