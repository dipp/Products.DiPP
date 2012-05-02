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
to_address = from_address
from_name = self.portal_properties.email_from_name
email = request.form['email']
subject = request.form['subject']

# the message format, %s will be filled in from data
message = """
From: %s <%s>
To: %s
Subject: %s

Email: %s
"""

msg = message % (
    from_name,
    from_address,
    to_address,
    subject,
    email
    )

mhost.send(msg)

msg = "Thank you for subscribing to the BMM newsletter! You will be informed about new BMM articles and BMM website content."
RESPONSE.redirect(request.HTTP_REFERER + "?portal_status_message=" + msg)


#print msg


#return printed
