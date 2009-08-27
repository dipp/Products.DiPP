## Script (Python) "synchronize"
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
from StringIO import StringIO

request  = container.REQUEST
RESPONSE = request.RESPONSE

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
out = StringIO()

articles   = container.portal_catalog(portal_type='FedoraArticle')
for article in articles:
    if article.id.split('_')[0] == 'temp':
        print >> out, "Skipping: " + article.getURL()
    else:
        obj = article.getObject()
        obj.syncMetadata()        
        print >> out, "Syncing: " + article.getURL()
return out.getvalue()
