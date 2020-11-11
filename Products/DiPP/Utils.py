# -*- coding: utf-8 -*-
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.

from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject
# from dipp.awstats.statistics import Statistics
import urllib2
import urllib
import urlparse
import socket
import logging
import Permissions

logger = logging.getLogger(__name__)

# VERIFY_SERVER="www.google.com"


class Utils(UniqueObject, SimpleItem):
    """Utilities for e.g. reCAPTCHA."""

    meta_type = 'Utils'
    id = 'Utils'
    title = 'Utilities'
    security = ClassSecurityInfo()

    def get_ip(self, request):
        """Extract the client IP address from the HTTP request in proxy compatible way.

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

    def get_location(self, path, request):
        """Return the URL of an uploaded file based on ip and port.

        not rewritten by VHM/Apache and without https. Requires a
        FQDN of the server running zope
        """
        address = socket.gethostbyname(socket.getfqdn())
        port = request.environ["SERVER_PORT"]
        netloc = ':'.join((address, port))
        url = urlparse.urlunparse(('http', netloc, '/'.join(path), '', '', ''))
        logger.info(url)
        return url

    def encode_if_necessary(self, s):
        if isinstance(s, unicode):
            return s.encode('utf-8')
        return s
    
    """
    security.declareProtected(Permissions.VIEW_STATISTICS, 'awstats_years')
    def awstats_years(self, journal):
        stats = Statistics(journal)
        return stats.available_years()

    security.declareProtected(Permissions.VIEW_STATISTICS, 'awstats_months')
    def awstats_months(self, journal, year):
        stats = Statistics(journal)
        return stats.months(year)


    security.declareProtected(Permissions.VIEW_STATISTICS, 'awstats_data')
    def awstats_data(self, journal, year, urls):
        stats = Statistics(journal)
        urls = [urlparse.urlparse(url)[2] for url in urls]
        return stats.get_data(year, urls)
    """
