## Script (Python) "fix_pubdate"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, fix=0
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
fedora = getToolByName(self, 'fedora')
portal     = portal_url.getPortalObject()
articles   = container.portal_catalog(portal_type='FedoraArticle', sort_on='getPID', Language="all")
print 'fix:', fix

for article in articles:
    PID = article.getPID
    if PID.split(':')[0] == 'dipp':
    #if PID == 'dipp:2152':
        qdc = fedora.getQualifiedDCMetadata(PID)
        bc = qdc['bibliographicCitation'][0]
        datum = bc['journalIssueDate']
        correct = DateTime(datum).strftime("%Y-%m-%d")
        fixme = "-"
        if datum != correct:
            fixme = "+"
            if fix:
                fedora.setJournalIssueDate(PID, correct)

        print fixme, PID, datum, correct

return printed
