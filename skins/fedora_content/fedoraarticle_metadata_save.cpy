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
translate = context.translate

params = REQUEST.form

new_subjects = params['new_subjects']
subject = params.get('subject',[])
params['subject'] = subject + new_subjects

#  pagenumbers and section are only kept in plone
startpage = params.get('startpage',[])
endpage = params.get('endpage',[])
journal_section = params.get('journal_section','no-section')
self.setStartpage(startpage)
self.setEndpage(endpage)
self.setJournal_section(journal_section)

fedora.setQualifiedDCMetadata(params)
self.syncMetadata()


if REQUEST:
    msg = context.safePortalMessage(translate('metadata-updated', domain='qdc'))
    context.plone_utils.addPortalMessage(msg)
    REQUEST.RESPONSE.redirect(REQUEST.HTTP_REFERER)
    #REQUEST.RESPONSE.redirect(REQUEST.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
