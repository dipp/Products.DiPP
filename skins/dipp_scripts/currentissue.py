## Script (Python) "setArticleTitle"
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

portal_url = getToolByName(self, 'portal_url')

catalog = getToolByName(self, 'portal_catalog')
issues = catalog(
            portal_type=('Issue','FedoraHierarchie'),
            review_state='published',
            sort_on='Date',
            sort_order='reverse',
            sort_limit=1)
if issues:
    RESPONSE.redirect(issues[0].getURL())
else:
    RESPONSE.redirect(portal_url() + '?portal_status_message=There are no published issues.')
