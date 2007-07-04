## Script (Python) "checkForNewPIDs"
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
ALLOWED_IPS = ["193.30.112.98","193.30.112.23","10.1.1.57","10.1.1.67"]

IP = request.HTTP_X_FORWARDED_FOR


"""

if IP in ALLOWED_IPS:

    MIMEType = self.content_type
    type = MIMEType.split('/')[0]
    
    RESPONSE.setHeader('Content-Type', MIMEType)
    if type in ['application','image']:
        return self
    if type in ['text']:
        return self.body
    else:
        print "Unsupported MIME Type"
        return printed
else:
    print "Your IP (%s) is not allowed to access this content!" % (IP)
    return printed
"""
