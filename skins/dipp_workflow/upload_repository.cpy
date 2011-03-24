# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime
request  = context.REQUEST

fedora = getToolByName(context, 'fedora')
portal_url = getToolByName(context, 'portal_url')
portal     = portal_url.getPortalObject()
Location   = request.get('Location')
storageType = request.get('storageType')

if Location.startswith('https'):
    Location = Location.replace('https','http',1)

JournalPID = request.get('journalPID')
params     = request.form

new_subjects = params.get('new_subjects', [])
subject = params.get('subject',[])
subjects = subject + new_subjects
params['subject'] = subjects

context.plone_log(subjects)

journalTitle = portal.Title()
now = DateTime().strftime("%Y-%m-%d")
if storageType == 'temporary':
    params['alternative'] = [{'value':'','lang':''}]
    params['DCTermsAbstract'] = []
    params['creatorPerson'] = [{'firstName':'John','lastName':'Doe'}]
    params['creatorCorporated'] = []
    params['contributor'] = []
    params['DDC'] = ['']
    params['subjectClassified'] = []
    params['pubType'] = ['']
    params['docType'] = ['']
    params['bibliographicCitation'] = [{'journalIssueDate':now,'journalIssueNumber':'n/a','journalTitle':journalTitle,'journalVolume':'n/a'}]
    params['rights'] = ['DPPL']


newPID = fedora.createNewArticle(JournalPID, JournalPID, params, Location)
context.plone_log('neuer Artikel: %s' % Location)

state.set(status='success')
state.set(portal_status_message='Datei wurde hochgeladen und wird konvertiert!')
return state
