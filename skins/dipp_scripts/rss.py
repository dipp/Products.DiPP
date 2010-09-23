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

if len(request.traverse_subpath) < 1:
    msg = "No valid Feed"
    RESPONSE.redirect('%s/worklist' % context.absolute_url() + '?portal_status_message=' + msg)
else:
    return rss.rss()

