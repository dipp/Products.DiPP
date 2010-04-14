# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = context.REQUEST

fedora = getToolByName(context, 'fedora')

Location   = request.get('Location')
storageType = request.get('storageType')

if Location.startswith('https'):
    Location = Location.replace('https','http',1)

JournalPID = request.get('journalPID')
params     = request.form

if storageType == 'temporary':
    params['alternative'] = [{'value':'','lang':''}]
    params['DCTermsAbstract'] = []
    params['creatorPerson'] = []
    params['creatorCorporated'] = []
    params['contributor'] = []
    params['DDC'] = ['']
    params['subjectClassified'] = []
    params['pubType'] = ['']
    params['docType'] = ['']
    params['bibliographicCitation'] = [{'journalIssueDate':'','journalIssueNumber':'','journalTitle':'','journalVolume':''}]
    params['rights'] = ['DPPL']


newPID = fedora.createNewArticle(JournalPID, JournalPID, params, Location)
context.plone_log('neuer Artikel: %s' % Location)

state.set(status='success')
state.set(portal_status_message='Datei wurde hochgeladen und wird konvertiert!')
return state
