# -*- coding: utf-8 -*-
#
# File: SpecialIssue.py
#
# Copyright (c) 2011 by DiPP, hbz
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the 
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#

__author__ = """Peter Reimer <reimer@hbz-nrw.de>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.DiPP.config import *
try:
    from Products.LinguaPlone.public import *
    from Products.LinguaPlone import utils
except ImportError:
    from Products.Archetypes.public import *


schema = Schema((

    LinesField(
        name='keyword',
        widget=MultiSelectionWidget(
            label="Keywords",
            description="All articles tagged with this keywords are bundled to a special issue.",
            label_msgid='DiPPContent_label_keyword',
            description_msgid='DiPPContent_help_keyword',
            i18n_domain='DiPPContent',
        ),
        required=1,
        multiValued=1,
        vocabulary="getSubjects"
    ),

    ImageField(
        name='coverpicture',
        widget=ImageWidget(
            label="Cover picture",
            description="A cover picture for this special issue.",
            label_msgid='DiPPContent_label_coverpicture',
            description_msgid='DiPPContent_help_coverpicture',
            i18n_domain='DiPPContent',
        ),
        storage=AttributeStorage(),
        sizes={'small':(100,100),'medium':(200,200),'large':(600,600)}
    ),

    StringField(
        name='Description',
        widget=StringWidget(
            label="Description",
            label_msgid='DiPPContent_label_Description',
            i18n_domain='DiPPContent',
        )
    ),

    TextField(
        name='Details',
        allowable_content_types=('text/plain', 'text/structured', 'text/html'),
        widget=RichWidget(
            label="Details",
            description="",
            label_msgid='DiPPContent_label_Details',
            description_msgid='DiPPContent_help_Details',
            i18n_domain='DiPPContent',
        ),
        default_output_type='text/html'
    ),

    IntegerField(
        name='position',
        index="FieldIndex",
        widget=IntegerField._properties['widget'](
            label="Position",
            description="Add a number for sorting",
            label_msgid='DiPPContent_label_position',
            description_msgid='DiPPContent_help_position',
            i18n_domain='DiPPContent',
        ),
        languageIndependent="1"
    ),

    StringField(
        name='sort_on',
        widget=SelectionWidget(
            label="Sorting",
            description="Sort criteria for the articles",
            label_msgid='DiPPContent_label_sort_on',
            description_msgid='DiPPContent_help_sort_on',
            i18n_domain='DiPPContent',
        ),
        vocabulary=(('Contributors','First author'),('sortable_title','Title'),('Date','getIssueDate'))
    ),

    StringField(
        name='sort_order',
        widget=SelectionWidget(
            label="Sort order",
            description="Ascending or descending",
            label_msgid='DiPPContent_label_sort_order',
            description_msgid='DiPPContent_help_sort_order',
            i18n_domain='DiPPContent',
        ),
        vocabulary=(('ascending','Ascending order'),('descending','Reverse/descending order'))
    ),

),
)


SpecialIssue_schema = BaseSchema.copy() + \
    schema.copy()


class SpecialIssue(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Special Issue'

    meta_type = 'SpecialIssue'
    portal_type = 'SpecialIssue'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'SpecialIssue.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Special Issue"
    typeDescMsgId = 'description_edit_specialissue'


    actions =  (


       {'action': "string:${object_url}/edit",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/view",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = SpecialIssue_schema

    aliases = {
        '(Default)'  : 'specialissue_view',
        'view'       : 'specialissue_view',
        'edit'       : 'atct_edit',
        'properties' : 'base_metadata',
        }



    def getSubjects(self):
        return self.portal_catalog.uniqueValuesFor('Subject')


registerType(SpecialIssue, PROJECTNAME)
