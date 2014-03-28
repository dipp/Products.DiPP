# -*- coding: utf-8 -*-
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id: BibTool.py 4819 2014-02-11 16:12:25Z reimer $

from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from dipp.datacite import datacite
from dipp.datacite.endpoints import ENDPOINTS
import Permissions
import logging

logger = logging.getLogger(__name__)


class DataCite(UniqueObject, SimpleItem):
        
    meta_type = 'DataCite'
    id = "portal_doiregistry"
    title = 'Manage DOI registration with DataCite'
    toolicon = 'skins/dipp_images/fedora.png'
    security = ClassSecurityInfo()

    manage_options = ({ 'label'  : 'Configuration',
                        'action' : 'datacite_config_form'},
                     ) + SimpleItem.manage_options

    security.declareProtected(Permissions.MANAGE_JOURNAL, 'datacite_config_form')
    datacite_config_form = PageTemplateFile('www/datacite_config_form.pt', globals())
    
    
    def __init__(self):
        
        self.prefix = ""
        self.user = ""
        self.password = ""
        self.endpoint = ""
        self.reserved_dois = []
        self.testMode = False

    security.declareProtected(Permissions.MANAGE_JOURNAL, 'set_datacite_settings')
    def set_datacite_settings(self, REQUEST, prefix, user, password, endpoint, reserved_dois, testMode=False):
        """ZMI method to store the datacite configuration."""
        self.prefix = prefix
        self.user = user
        self.password = password
        self.endpoint = endpoint
        self.reserved_dois = reserved_dois
        if testMode:
            self.testMode = True
        else: 
            self.testMode = False
        manage_tabs_message = "Saved"
        logger.info("Saved DataCite configuration")
        return self.datacite_config_form(REQUEST, management_view='Configuration', manage_tabs_message=manage_tabs_message)

    security.declareProtected(Permissions.MANAGE_JOURNAL, 'make_datacite_client')
    def _make_datacite_client(self):
        return datacite.Client(self.user, self.password, self.endpoint, self.testMode)

    security.declareProtected(Permissions.MANAGE_JOURNAL, 'get_endpoints')
    def get_endpoints(self):
        return ENDPOINTS
        
    security.declareProtected(Permissions.MANAGE_JOURNAL, 'get_url')
    def get_url(self, doi):
        client = self._make_datacite_client()
        return client.get_url(doi)

    security.declareProtected(Permissions.MANAGE_JOURNAL, 'post_metadata')
    def post_metadata(self, metadata):
        client = self._make_datacite_client()
        return client.post_metadata(metadata)
    
    security.declareProtected(Permissions.MANAGE_JOURNAL, 'get_metadata')
    def get_metadata(self, doi):
        client = self._make_datacite_client()
        return client.get_metadata(doi)

    security.declareProtected(Permissions.MANAGE_JOURNAL, 'create_or_modify_doi')
    def create_or_modify_doi(self, doi, url):
        client = self._make_datacite_client()
        return client.create_or_modify_doi(doi, url)
        
