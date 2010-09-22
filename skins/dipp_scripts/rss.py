## Script (Python) "feeds"
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
rss = getToolByName(self, 'feeds')
portal     = portal_url.getPortalObject()

feeds = request.traverse_subpath
return rss.rss()
print feeds
return printed
