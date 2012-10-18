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
request  = container.REQUEST
RESPONSE = request.RESPONSE



"""Allow fedora to fetch private content without authentication. This script runs with proxyrole Manager
   but can only be called from the machine where fedora is installed.
"""

ALLOWED_IPS = ( "193.30.112.23", "193.30.112.98", "193.30.112.184", "193.30.112.185")


def get_ip(request):
    """  Extract the client IP address from the HTTP request in proxy compatible way.
    found at http://plone.org/documentation/manual/plone-community-developer-documentation/serving/http-request-and-response
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
fedora = getToolByName(self,'fedora')
fedoraIP = fedora.address

context.plone_log ("private Id: %s" % (self.id))

#if IP == fedoraIP:
if IP in ALLOWED_IPS:

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
        print "Unsupported MIME Type"
        return printed
else:
    print "Your IP %s is not allowed to access this content!" % (IP)
    return printed

