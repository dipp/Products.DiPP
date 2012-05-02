## Controller Python Script "mig23to24"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self, ip
##title=
##


""" run this script to move the configuration from the
plone root properties to the fedora tool
"""
from Products.CMFCore.utils import getToolByName

request = container.REQUEST
RESPONSE =  request.RESPONSE

fedora = getToolByName(self, 'fedora')
portal = getToolByName(self, 'portal_url').getPortalObject()

port = str(9280)

if hasattr(portal, 'PID'):
    PID = str(portal.PID)

if hasattr(portal, 'gap_container'):
    label = portal.gap_container

print "### current fedora settings:"
print fedora.PID
print fedora.label
print fedora.address
print fedora.port

print "### new fedora settings:\n"
if fedora.PID  and fedora.label:
    print "fedora tool already configured. do nothing"
else:
    fedora.manage_setFedoraSettings(PID, label, ip, port, None)
    print "configure fedora tool..."

print fedora.PID
print fedora.label
print fedora.address
print fedora.port

# clearing the root properties:
portal.manage_changeProperties({'PID':'','gap_container':''})
return printed
