## Script (Python) "makeGoogleScholarLink"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, qdc
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.PythonScript import DateTime

request  = container.REQUEST
RESPONSE = request.RESPONSE

authors = qdc['creatorPerson']
titles = qdc['title']
title = titles[0]['value']
bibliographicCitation = qdc['bibliographicCitation'][0]
journal = bibliographicCitation['journalTitle']
volume = bibliographicCitation['journalVolume']
issue = bibliographicCitation['journalIssueNumber']
date = DateTime(bibliographicCitation['journalIssueDate'])
year = date.strftime('%Y')
urn = qdc['identifierURN'];
id = self.PID.split(':')[-1]

authors_list = []

for author in authors:
    lastname = author['lastName']
    authors_list.append(lastname)

query = "+".join(title.split())
authors = "+".join(authors_list)
link = "http://scholar.google.de/scholar?as_q=%(as_q)s&as_sauthors=%(as_authors)s" % {'as_q':query,'as_authors':authors}

return link

