## Script (Python) "make_citation"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, qdc, citation_format, initials_only, initials_period, comma_separated
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.PythonScript import DateTime

request  = container.REQUEST
RESPONSE = request.RESPONSE

PID = self.getParentNode().PID

if PID.split(':')[0] != 'temp':
    authors = qdc['creatorPerson']
    titles = qdc['title']
    title = titles[0]['value']
    bibliographicCitation = qdc['bibliographicCitation'][0]
    journal = bibliographicCitation['journalTitle']
    volume = bibliographicCitation['journalVolume']
    issue = bibliographicCitation['journalIssueNumber']
    issuedate = DateTime(bibliographicCitation['journalIssueDate'])
    date = issuedate.strftime(self.portal_properties.site_properties.localTimeFormat)
    year = issuedate.strftime('%Y')
    urn = qdc['identifierURN'];
    id = self.PID.split(':')[-1]
    authors_list = ""
    period = ""
    comma = ""
    
    if initials_period:
        period = "."

    if comma_separated:
        comma = ','

    for author in authors:
        author_number = authors.index(author) + 1
        firstnames = author['firstName'].split()
        firstnames_initials = ""
        for firstname in firstnames:
            firstnames_initials += firstname[0] + period
        lastname = author['lastName']
        if author_number == len(authors):
            glue = ""
        else:
            glue = ", "
        if initials_only:
            firstname = firstnames_initials
        authors_list += "%s%s %s%s" % (lastname, comma, firstname, glue)


    cite = citation_format % {
    'authors':authors_list, 
    'title':title,
    'journal':journal,
    'volume':volume,
    'issue':issue,
    'year':year,
    'date':date,
    'id':id,
    'urn': '<a href="http://nbn-resolving.de/%(urn)s">%(urn)s</a>' % {'urn':urn}
    }
    
else:
    cite = "This is just a temporary conversion, no metadata available for PID %s. to build a citation" % PID
    
return cite
