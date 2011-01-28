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

for article in articles:
    print "%s, %s, %s" % (article.getPID, article.review_state, article.Title)

return printed
