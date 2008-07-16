## Script (Python) "make_citation"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, qdc, citation_format
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
authors_list = ""

for author in authors:
    author_number = authors.index(author) + 1
    firstnames = author['firstName'].split()
    firstnames_initials = ""
    for firstname in firstnames:
        firstnames_initials += firstname[0]
    lastname = author['lastName']
    if author_number == len(authors):
        glue = ""
    else:
        glue = ", "
    authors_list += "%s %s%s" % (lastname, firstnames_initials, glue)


#citation_format = """
#%(authors)s (%(year)s). %(title)s. %(journal)s, Vol. %(volume)s, bmm%(id)s. (%(urn)s) 
#"""
cite = citation_format % {
    'authors':authors_list, 
    'title':title,
    'journal':journal,
    'volume':volume,
    'issue':issue,
    'year':year,
    'date':date,
    'id':id,
    'urn':urn
    }
return cite
