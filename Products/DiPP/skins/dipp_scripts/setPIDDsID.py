## Script (Python) "setPIDDsID"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

# set creationDate and effectiveDate to a given date.
# by jensens

PID = traverse_subpath[0]
DsID = traverse_subpath[1]

if len(PID.split(':')) < 2:
    return "PID widthout colon"

# return printed

context.setPID(PID)
return "PID on '%s' successfully set to %s." % (context.title_or_id(), PID)
context.setDsID(DsID)
return "DsID on '%s' successfully set to %s." % (context.title_or_id(), DsID)

context.reindexObject()

