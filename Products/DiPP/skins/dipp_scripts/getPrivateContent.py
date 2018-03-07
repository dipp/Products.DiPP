## Script (Python) "getPrivateContent"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,file=""
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request = container.REQUEST
RESPONSE = request.RESPONSE

"""Allow fedora to fetch private content without authentication. This script runs with proxyrole Manager
   but can only be called from the machine where fedora is installed.
"""


def get_ip(request):
    """ Extract the client IP address from the HTTP request in proxy compatible way.

    Found at http://plone.org/documentation/manual/plone-community-developer-documentation/serving/http-request-and-response
    @return: IP address as a string or None if not available
    """
    if "HTTP_X_FORWARDED_FOR" in request.environ:
        # Virtual host
        ip = request.environ["HTTP_X_FORWARDED_FOR"]
    elif "HTTP_HOST" in request.environ:
        # Non-virtualhost
        ip = request.environ["REMOTE_ADDR"]
    else:
        # Unit test code?
        ip = None

    return ip


IP = get_ip(request)
fedora = getToolByName(self, 'fedora')

FEDORA_IP, FEDORA_PORT = fedora.getServerConfiguration()
context.plone_log((FEDORA_IP, FEDORA_PORT))

if IP == FEDORA_IP:

    context.plone_log("getPrivateContent: trying to fetch  '%s' (%s)" % (self.id, IP))
    MIMEType = self.content_type
    MIMETypeCategory = MIMEType.split('/')[0]

    RESPONSE.setHeader('Content-Type', MIMEType)
    if MIMETypeCategory in ['application', 'image', 'audio', 'video']:
        cd = 'attachment; filename=%s' % (id)
        RESPONSE.setHeader('Content-Disposition', cd)
        return self.getFile()

    if MIMETypeCategory == 'text':
        return self.body
    else:
        print "Unsupported MIME Typ"
        return printed
else:
    msg = "Your IP %s is not allowed to access this content!" % (IP)
    print msg
    context.plone_log(msg)
    return printed
