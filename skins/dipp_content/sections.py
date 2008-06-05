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
    'sec1': {'name':'Section 1',
             'contact':'Max Muster',
             'mail':''},
    'sec2': {'name':'Section 2',
             'contact':'Erika Mustermann',
             'mail':''}
}


return sections
