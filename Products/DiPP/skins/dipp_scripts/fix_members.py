## Script (Python) "author_or_contributor"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,user_id=None, contributor=None
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE
mtool = getToolByName(self, 'portal_membership')

members = mtool.listMembers()
for member in members:
    print member.id, member.getRoles()

print "\nNumber of Members: %s" % len(members)

return printed

