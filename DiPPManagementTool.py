# -*- coding: utf-8 -*-
# The FedoraTool for adding and manipulating objects in Fedora
# File: FedoraTool.py
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id: FedoraTool.py 2132 2010-06-04 07:08:42Z reimer $

from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from config import view_permission, LANGUAGES, DEFAULT_METADATA

try:
    from Products.CMFCore.permissions import ManagePortal
    from Products.CMFCore.permissions import View
except ImportError:
    from Products.CMFCore.CMFCorePermissions import ManagePortal
    from Products.CMFCore.CMFCorePermissions import View


class DiPPManagement(UniqueObject, SimpleItem):
    """ interact with the repository Fedora 2 und DiPP3 """
    
    meta_type = 'DiPPManagementTool'
    id = 'dmt'
    title = 'DiPP Management'
    # toolicon = 'skins/dipp_images/fedora.png'
    security = ClassSecurityInfo()
    
    manage_dippproducts_form = PageTemplateFile('www/dippproducts_form.pt', globals())
    security.declareProtected(view_permission, 'manage_dippproducts_form')
    
    manage_options = ({'label':'DiPP Products',
                       'action':'manage_dippproducts_form',
                       'help':('DiPPProducts', 'search.stx')},
        ) + SimpleItem.manage_options

    def __init__(self):
        self.products = ('DiPP','DiPPThemeNG','DiPPClassicTheme','FedoraAwstats')
        pass
