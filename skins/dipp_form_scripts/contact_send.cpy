## Controller Python Script "submit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self, name='', email="", comment=""
##title=
##

from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

mhost = context.MailHost

recipient = self.portal_properties.email_from_address

message = """
From: %s <%s>
To: %s
Subject: Anfrage an SWS
Content-Type: text/plain; charset=UTF-8;

name: %s
email: %s
%s
"""

msg = message % (
    name,
    email,
    recipient,
    name,
    email,
    comment
    )

mhost.send(msg)

#print msg
#return printed
return state

