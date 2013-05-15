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
catalog = getToolByName(self, 'portal_catalog')

authors = catalog.uniqueValuesFor('getAuthors')
fullnames = []

for author in authors:
    try:
        parts = author.split(',')
        fullnames.append(parts[1].strip() + ' ' + parts[0].strip())
    except:
        print "invalid name: %s" % author
fullnames = tuple(fullnames)

keep_members = []
members = mtool.listMembers()
for member in members:
    keep = " "
    user_id = member.id
    memberinfo = mtool.getMemberInfo(user_id)
    fullname = memberinfo['fullname']
    roles = filter(lambda role: role not in ('Member','Authenticated'), member.getRoles())
    
    if fullname in fullnames or len(roles) > 0:
        keep = "*"
        keep_members.append(user_id)

    print keep, member.id, member.getRoles(), roles,  fullname 

print "\nNumber of Members: %s" % len(members)
print "Keep: ", keep_members
return printed

