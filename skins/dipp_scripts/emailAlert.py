## Script (Python) "gap_login"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

mhost = context.MailHost

from_address = self.portal_properties.email_from_address
from_name = self.portal_properties.email_from_name
addresses = self.portal_properties.dipp_properties.alertEmailAddresses

# the message format, %s will be filled in from data
message = """
From: %s <%s>
To: %s
Subject: New item submitted for approval - %s

%s

URL: %s
"""

for address in addresses:
    msg = message % (
        from_name,
        from_address,
        address,
        'XXX',
        'das ist die nachricht',
        'http://www.....'
        )

    print msg
    #print addresses
    mhost.send(msg)

return printed
