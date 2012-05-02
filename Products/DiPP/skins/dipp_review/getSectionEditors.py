## Script (Python) "getSectionEditors"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, section_id=None
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

ds = getToolByName(self, 'dipp_sections')
sections = ds.getSections()

mship = self.portal_membership


editors = []

for  section in sections:
    id = section['editor']
    if id:
        user = mship.getMemberById(id)
        email = user.getProperty('email')
        fullname = user.getProperty('fullname')
        editors.append({'id':id,'email':email,'fullname':fullname,'user':user})

return editors
