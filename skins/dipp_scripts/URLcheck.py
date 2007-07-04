## Script (Python) "URLcheck"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

oftool     = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal     = portal_url.getPortalObject()
articles  = container.portal_catalog(portal_type='FedoraArticle',sort_on='Date')

for  article in articles:
    obj       = article.getObject()
    PID       = obj.PID
    ploneURL  = obj.absolute_url()
    fedoraURL = context.fedoraGetQDC(PID)['identifierURL']
    
    if ploneURL == fedoraURL:
        OK = "OK"
    else:
        OK = ""
    
    print PID, OK
    print "\t p",ploneURL
    print "\t f",fedoraURL

return printed
