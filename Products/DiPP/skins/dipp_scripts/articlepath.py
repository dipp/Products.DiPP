## Script (Python) "articlepath"
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
RESPONSE = request.RESPONSE


object = context.aq_inner

infos = {
    'article':  None,
    'issue' : None
    }

while object.portal_type != "Plone Site":
    if object.portal_type == "FedoraArticle":
        infos['article'] = object
    if object.portal_type == "Issue":
        infos['issue'] = object
    object = object.aq_parent

return infos

