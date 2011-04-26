"""
$Id$
"""
from Products.Archetypes.public import DisplayList
from Products.CMFCore import permissions

from Permissions import ADD_CONTENTS_PERMISSION
from Permissions import EDIT_CONTENTS_PERMISSION
from Permissions import VIEW_CONTENTS_PERMISSION

view_permission = permissions.ManagePortal

PROJECTNAME = 'DiPP'

STYLESHEETS = (
    {'id': "dipp.css", 'media': 'screen', 'rendering': 'import'},
    {'id': "tabber.css", 'media': 'screen', 'rendering': 'import'},
    {'id': "dipp_article.css", 'media': 'all', 'rendering': 'import'},
    {'id': "dipp_article_print.css", 'media': 'print', 'rendering': 'import'}
)

DEPENDENCIES = [
    'Archetypes',
    'ATVocabularyManager',
    'CMFOpenflow',
    'DiPPContent',
    'LinguaPlone',
    'PloneLanguageTool',
    'TextIndexNG3'
    ]

VOCABULARIES = (
    ( 'SimpleVocabulary','journal-sections','The sections of the journal, used to organize an issue. Do not delete the "no section" entry.', 'Journal Sections'),
    ( 'SimpleVocabulary','areas-of-expertise','Areas, in which the potentiel reviewer feels competend.', 'Areas of expertise'),
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
    'hun':'Magyar'
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

TOOLS = (
    ('EditorialToolbox','Fedora2DiPP3','BibTool')
)

INDEXES = (
    ('Contributors','KeywordIndex'),
)
GLOBALS = globals()

# Configuration for the testrunner

PID = 'dipp:1898'
label = '81' 
address = '193.30.112.98'
port = '9280'
