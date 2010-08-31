## Script (Python) "article_rss"
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
response = request.RESPONSE

bibtool = getToolByName(self, "bibtool")
feed = bibtool.rss()
return feed