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

context.plone_log('habs gelogt!')

return 'log mich'
