# -*- coding: utf-8 -*-
"""
$Id$
"""
from Products.Archetypes.public import DisplayList
from Products.CMFCore import permissions

from Products.DiPP.Permissions import ADD_CONTENTS_PERMISSION
from Products.DiPP.Permissions import EDIT_CONTENTS_PERMISSION
from Products.DiPP.Permissions import VIEW_CONTENTS_PERMISSION

view_permission = permissions.ManagePortal

PROJECTNAME = 'DiPP'

DEPENDENCIES = [
    'Archetypes',
    'ATVocabularyManager',
    'CMFOpenflow',
    'LinguaPlone',
    'PloneLanguageTool',
    'TextIndexNG3'
    ]

VOCABULARIES = (
    ( 'SimpleVocabulary','journal-sections','The sections of the journal, used to organize an issue. Do not delete the "no section" entry.', 'Journal Sections'),
    ( 'SimpleVocabulary','areas-of-expertise','Areas, in which the potentiel reviewer feels competend.', 'Areas of expertise'),
    ( 'SimpleVocabulary','subject-areas','Areas, in which the potentiel reviewer feels competend.', 'Subject areas'),
)

LANGUAGES = {
    'ger':'Deutsch',
    'eng':'English',
    'fra':'Français',
    'spa':'Español',
    'ita':'Italiano',
    'rus':'Русский',
    'chi':'中文',
    'cze':'Čeština',
    'hun':'Magyar',
    'fin':'Finnish'
}

# format: medatata, visible, required, default
# all not listed metadata are True, True, ""
DEFAULT_METADATA = (
    ('docType', True, True, 'text'),
    ('pubType', True, True, 'article'),
    ('alternative', True, False, ''),
    ('DCTermsAbstract', True, False, ''),
    ('creatorCorporated',True, False, ''),
    ('contributor', True, False, '') 
)

SUBMISSION_FILENAME_FORMAT = "rev"

TOOLS = (
    ('Fedora2DiPP3','BibTool','DiPP Sections Tool', 'DiPP Peerreview Tool')
)

INDEXES = (
    ('Contributors', 'KeywordIndex'),
    ('getPID', 'FieldIndex'),
    ('getAuthors', 'KeywordIndex'),
)
GLOBALS = globals()

# Configuration for the testrunner

PID = 'dipp:1898'
label = '81' 
address = '193.30.112.98'
port = '9280'
