## Script (Python) "synchronize"
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
from StringIO import StringIO

request  = container.REQUEST
RESPONSE = request.RESPONSE

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
out = StringIO()

articles   = container.portal_catalog(portal_type='FedoraArticle')
for article in articles:
    # only permanently stored articles are synchronized
    # those with id/PID starting with 'temp' are skipped
    if article.id.split('_')[0] == 'temp':
        print >> out, "Skipping: " + article.getURL()
    else:
        obj = article.getObject()
        # Journal section could be emty till now. It is required now
        # and filled with a default 'no-section' Needed for the new
        # issue_content_view template
        if obj.journal_section == "":
            print >> out, "FIX ME"
            obj.setJournal_section('no-section')
            obj.reindexObject()
        print >> out, "Section:" + obj.journal_section
        
        # write the QDC Metadata stored in fedora to the available
        # metadata fields of the Plone object
        try:
            obj.syncMetadata()
            print >> out, "Syncing: " + article.getURL()
        except:
            print >> out, "Can't connect to Fedora repository, no syncing"

return out.getvalue()
