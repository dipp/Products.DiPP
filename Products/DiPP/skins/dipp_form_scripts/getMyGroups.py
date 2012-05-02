## Script (Python) "getMyGroups"
##title=Get Groups
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
RESPONSE =  request.RESPONSE

mtool = context.portal_membership
userid = request.AUTHENTICATED_USER
member = mtool.getMemberById(userid.id)
groups = member.getGroups

#for group in groups:
#    print group

return groups
