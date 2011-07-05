## Script (Python) "getPublishingYears.py"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# -*- coding: utf-8 -*-
"""
return a list of years with published articles
"""

from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(context, 'portal_url')
portal = portal_url.getPortalObject()


catalog = getToolByName(context, 'portal_catalog')

articles = catalog(
            portal_type=('FedoraArticle'),
            sort_on='getIssueDate',
            sort_order='ascending',
            Language='all',
            sort_limit=1
            )
            
today = int(DateTime().earliestTime().strftime("%Y"))
if len(articles) > 0:
    oldest = articles[0].getIssueDate
    first =  int(oldest.strftime("%Y"))
else:
    first = today

return range(today, first - 1, -1)
