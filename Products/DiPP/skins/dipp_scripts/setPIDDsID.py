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

# code inspired by:
# set creationDate and effectiveDate to a given date.
# by jensens

sub_path = traverse_subpath

msg = ""

if len(sub_path) == 1:
    PID = traverse_subpath[0]
    context.setPID(PID)
    context.reindexObject()
    msg += "PID on '%s' successfully set to %s." % (context.title_or_id(), PID)
        

elif len(sub_path) == 2:
    PID = traverse_subpath[0]
    DsID = traverse_subpath[1]
    context.setPID(PID)
    msg += "PID on '%s' successfully set to %s." % (context.title_or_id(), PID)
    try:
        context.setDsID(DsID)
        msg += "DsID on '%s' successfully set to %s." % (context.title_or_id(), DsID)
    except:
        msg += "DsID could not be set"
    context.reindexObject()

else:
    msg += "done nothing"

context.plone_utils.addPortalMessage(msg)
RESPONSE.redirect('%s/base_view' % context.absolute_url())



