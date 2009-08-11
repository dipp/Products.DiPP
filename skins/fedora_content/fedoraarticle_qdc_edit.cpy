##script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST

fedora = getToolByName(self, 'fedora')

params = REQUEST.form

new_subjects = params['new_subjects']
subject = params['subject'] + new_subjects 
params['subject'] = subject

self.syncMetadata()
fedora.setQualifiedDCMetadata(params)

portal_status_message = "Änderungen wurden gespeichert"

if REQUEST:
     REQUEST.RESPONSE.redirect(REQUEST.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
