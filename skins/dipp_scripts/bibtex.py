## Script (Python) "bibtex"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=qdc
##title=
##

# -*- coding: utf-8 -*-
request  = container.REQUEST
RESPONSE = request.RESPONSE
from DateTime import DateTime


authors = []
persons = qdc['creatorPerson']
for person in persons:
    authors.append(person["firstName"] + " " + person["lastName"])
author = ", ".join(authors)
    
title = qdc["title"][0]["value"]
journal = qdc['bibliographicCitation'][0]["journalTitle"]
number = qdc['bibliographicCitation'][0]["journalIssueNumber"]
year = qdc['bibliographicCitation'][0]["journalVolume"]
date = DateTime(qdc['bibliographicCitation'][0]["journalIssueDate"])
id = ":".join((qdc['creatorPerson'][0]["lastName"],year))

bibitem = """
@Article{%(id)s,
  author  = "%(author)s", 
  title   = "%(title)s",
  journal = "%(journal)s",
  number  = "%(number)s",
  year    = "%(year)s"
}
"""

return bibitem % {"id": id, "author":author, "title":title, "journal":journal, "number":number, "year":year}
