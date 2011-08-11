## Script (Python) "availableWorkflowtransitions"
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
wtool = portal.portal_workflow
objs = request.get('paths',None)
target = test(objs, objs, self)
transitions = wtool.getTransitionsFor(target, self) 
ids = []
for transition in transitions:
    ids.append(transition['id'])

return ids
