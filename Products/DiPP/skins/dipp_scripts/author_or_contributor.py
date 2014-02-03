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

self.plone_log("AUTHORSEARCH DEACTIVATED! user_id: %s, contributor: %s" % (user_id, contributor))
return {'author':[None], 'contributor': contributor}

mtool = getToolByName(self, 'portal_membership')
self.plone_log("user_id: %s, contributor: %s" % (user_id, contributor))

# try to find a memberid for a given contributor (Lastname, Firstname)
# if none is found, return none. in rare cases, were more than one 
# members match the Contributors name, return all as a list
author = [None]
if contributor:
    try:
        name = contributor.split(',')
        fullname = name[1] + ' ' + name[0];
        results = mtool.searchForMembers(name=fullname)
        author = []
        if results:
            for result in results:
                author.append(result.getMemberId())
        else:
            author.append(None)
    except:
        author = [user_id]

if user_id:
    self.plone_log("ID:" + user_id)
    authorinfo = mtool.getMemberInfo(user_id)
    if authorinfo:
        self.plone_log(authorinfo)
        fullname = authorinfo['fullname']
        name = fullname.split(' ')
        if len(name) > 0:
            last = name[-1]
            firstnames = name[0:len(name) - 1]
            first = ' '.join(firstnames) 
            contributor = last + ', '+ first
        author = [user_id]
        

return {'author':author, 'contributor': contributor}
