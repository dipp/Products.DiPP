## Script (Python) "bibtex"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,PID
##title=
##

# -*- coding: utf-8 -*-
request  = container.REQUEST
RESPONSE = request.RESPONSE

from Products.CMFCore.utils import getToolByName
fedora = getToolByName(self, 'fedora')

id = "Reimer:2006"
author = "Peter Reimer"
title = "Kurzanleitung"
journal = "Das Testjournal"
year = "2006"
number = "2"

template = """
@Article{%s,
  author  = "%s", 
  title   = "%s",
  journal = "%s",
  number  = "%s",
  year    = "%s"
}
"""
bibitem = template % (id, author, title, journal, number, year)
return bibitem
