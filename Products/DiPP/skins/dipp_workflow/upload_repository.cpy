# -*- coding: utf-8 -*-
##script (Python) "upload_repository"
##title=Ingest article to the fedora repository
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=

from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
request  = context.REQUEST

translate = context.translate
fedora = getToolByName(context, 'fedora')
portal_url = getToolByName(context, 'portal_url')
portal     = portal_url.getPortalObject()

Location   = request.get('Location')
storageType = request.get('storageType')
targetFormat = request.get('targetFormat')
article_title = request.get('title_value')
article_language = request.get('title_lang')


if Location.startswith('https'):
    Location = Location.replace('https','http',1)

JournalPID = request.get('journalPID')
params     = request.form

new_subjects = params.get('new_subjects', [])
subject = params.get('subject',[])
subjects = subject + new_subjects
params['subject'] = subjects

now = DateTime().strftime("%Y-%m-%d")
if storageType == 'temporary':
    params['storageType'] = storageType
    params['targetFormat'] = targetFormat
    params['title'] = [{'value':article_title,'lang':article_language}]
    params['alternative'] = [{'value':'','lang':''}]
    params['DCTermsAbstract'] = []
    params['creatorPerson'] = [{'firstName':'John','lastName':'Doe'}]
    params['creatorCorporated'] = []
    params['contributor'] = []
    params['DDC'] = ['']
    params['subjectClassified'] = []
    params['bibliographicCitation'] = [{'journalIssueDate':now,'journalIssueNumber':'n/a','journalTitle':'n/a','journalVolume':'n/a'}]
    params['rights'] = ['DPPL']

context.plone_log(params['title'])

newPID = fedora.createNewArticle(JournalPID, JournalPID, params, Location)
context.plone_log('new article created: %s' % newPID)

state.set(status='success')
msg = translate('file_uploaded_and_being_converted', domain='dipp')
context.plone_utils.addPortalMessage(msg)

return state
