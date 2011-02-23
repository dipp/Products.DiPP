##script (Python) "fedoraarticle_qdc_edit"
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
subject = params.get('subject',[])
params['subject'] = subject + new_subjects

#  pagenumbers are only kept in plone
startpage = params.get('startpage',[])
endpage = params.get('endpage',[])
self.setStartpage(startpage)
self.setEndpage(endpage)

fedora.setQualifiedDCMetadata(params)
self.syncMetadata()

portal_status_message = "Änderungen wurden gespeichert"

if REQUEST:
     REQUEST.RESPONSE.redirect(REQUEST.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
