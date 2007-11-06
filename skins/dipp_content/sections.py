## Script (Python) "gap_login"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# -*- coding: utf-8 -*-
request  = container.REQUEST
RESPONSE = request.RESPONSE

sections = {
    'accounting': {'name':'Accounting',
                   'contact':'Rainer Niemann (Graz)',
                   'mail':'niemann@business-research.org'},
    'finance':    {'name':'Finance',
                   'contact':'Christian Schlag (Frankfurt am Main)',
                   'mail':'schlag@business-research.org'},
    'managemant': {'name':'Management',
                   'contact':'Peter Walgenbach (Erfurt)',
                   'mail':'walgenbach@business-research.org'},
    'marketing':  {'name':'Marketing',
                   'contact':'Adamantios Diamantopoulos (Vienna)',
                   'mail':'diamantopoulos@business-research.org'},
    'operations': {'name':'Operations and Information Systems',
                   'contact':'Karl Inderfurth (Magdeburg)',
                   'mail':'inderfurth@business-research.org'},
}

sections = {}

return sections
