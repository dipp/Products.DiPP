## Script (Python) "makeWorkingCopy"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,Date=""
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE
translate = context.translate

new_version = self.make_working_copy(Date)
if new_version:
    msg = translate('previous_version_as_workingcopy', domain='dipp')
else:
    msg = translate('could_not_create_new_workingcopy', domain='dipp')
context.plone_utils.addPortalMessage(msg)
preview_url = self.absolute_url() + "/preview"
RESPONSE.redirect(preview_url)
