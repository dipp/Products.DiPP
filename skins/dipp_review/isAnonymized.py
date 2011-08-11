## Script (Python) "isAnonymized"
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
portal = portal_url.getPortalObject()

path = '/'.join(self.getPhysicalPath())
results = self.portal_catalog(Type=('Manuscript', 'Attachment'), path=path)

anonymized = 0

for result in results:
    obj = result.getObject()
    if self.getObjSize(obj.anonym) != '0 kB':
        anonymized = anonymized + 1

if len(results) == anonymized:
    return True
else:
    return False
