## Script (Python) "content_edit"
##title=Edit content
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

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

#GAP_CONTAINER = self.portal_properties.gap_container

title  = request.form['title']
journalPID  = request.form['journalPID']
MetaType  = request.form['MetaType']

PID = context.fedoraCreateNewContainer(journalPID,MetaType,title)
context.checkForNewPIDs(self,PID)
print PID

