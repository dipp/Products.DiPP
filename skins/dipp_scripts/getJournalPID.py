##Script (Python) "getJournalPID"
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

fedora = getToolByName(self, 'fedora')

try:
    GAP_CONTAINER = self.portal_properties.gap_container
except:
    raise Exception, "Keine Containerid angegeben"

if GAP_CONTAINER == "":
    raise Exception, "Keine Containerid angegeben"

query = (('label','has',GAP_CONTAINER),('cModel','has','DiPP:eJournal'),)
#new = context.fedoraSearch(query)
new = fedora.search(query)
return new[0]['PID']
