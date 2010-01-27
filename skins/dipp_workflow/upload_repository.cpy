# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = context.REQUEST

fedora = getToolByName(context, 'fedora')

Location   = request.get('Location')

if Location.startswith('https'):
    Location = Location.replace('https','http',1)

JournalPID = request.get('journalPID')
params     = request.form

newPID = fedora.createNewArticle(JournalPID, JournalPID, params, Location)
context.plone_log('neuer Artikel: %s', Location)

state.set(status='success')
state.set(portal_status_message='Datei wurde hochgeladen und wird konvertiert!')
return state
