## Script (Python) "make_citation"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,authors, titles
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

ct = self.portal_properties.dipp_properties.citation_format

authors_list = ""
for author in authors:
    authors_list += author['firstName'] + " " + author['lastName'] + ", "

title = titles[0]['value']

cite = ct % {'authors':authors_list, 'title':title}
return cite
