# -*- coding: utf-8 -*-
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id: BibTool.py 4526 2013-04-29 19:38:02Z reimer $

from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from Products.DiPP.config import PRIVATE_KEY, PUBLIC_KEY, VERIFY_SERVER
import urllib2
import urllib

import logging

logger = logging.getLogger("DiPP")

VERIFY_SERVER="www.google.com"

class Utils(UniqueObject, SimpleItem):
    """ Utilities for e.g. reCAPTCHA """
    
    meta_type = 'Utils'
    id = 'Utils'
    title = 'Utilities'
    security = ClassSecurityInfo()

    def get_ip(self,request):
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

    def encode_if_necessary(self, s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s

    def get_recaptcha_keys(self):
        """Return the reCAPTCHA keys from the config file for use in pagetemplates """
        return {'private':PRIVATE_KEY, 'public': PUBLIC_KEY}

    def validate_recaptcha(self, recaptcha_challenge_field, recaptcha_response_field, remoteip):
        """ Captcha code from
        http://recaptcha.googlecode.com/svn/trunk/recaptcha-plugins/python/recaptcha/client/captcha.py
        """

        params = urllib.urlencode ({
                'privatekey': self.encode_if_necessary(PRIVATE_KEY),
                'remoteip' :  self.encode_if_necessary(remoteip),
                'challenge':  self.encode_if_necessary(recaptcha_challenge_field),
                'response' :  self.encode_if_necessary(recaptcha_response_field),
                })

        request = urllib2.Request (
            url = "https://%s/recaptcha/api/verify" % VERIFY_SERVER,
            data = params,
            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "User-agent": "reCAPTCHA Python"
                }
            )
        
        httpresp = urllib2.urlopen(request)

        return_values = httpresp.read().splitlines();
        httpresp.close();

        return_code = return_values[0]
        
        if return_code == "true":
            is_valid = True
            error_code = None
        else:
            is_valid = False
            error_code = return_values[1]

        logger.info("reCAPTCHA - IP: %s, response: %s, error code: %s" % (remoteip, recaptcha_response_field, error_code))        
        return is_valid, error_code


    
