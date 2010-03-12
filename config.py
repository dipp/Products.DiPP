"""
$Id$
"""
from Permissions import ADD_CONTENTS_PERMISSION
from Permissions import EDIT_CONTENTS_PERMISSION
from Permissions import VIEW_CONTENTS_PERMISSION
from Products.Archetypes.public import DisplayList

PROJECTNAME = 'DiPP'
SKINS_DIR   = 'skins'

SKIN_NAMES = [
    'dipp_content',
    'dipp_forms',
    'dipp_form_scripts',
    'dipp_styles',
    'dipp_portlets',
    'dipp_scripts',
    'dipp_workflow',
    'dipp_images',
    'fedora_content'
    ]

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
    'PloneLanguageTool'
    ]

VOCABULARIES = (
    ( 'SimpleVocabulary','journal-sections','The sections of the journal, used to organize an issue. Do not delete the "no section" entry.', 'Journal Sections'),
    ( 'SimpleVocabulary','areas-of-expertise','Areas, in which the potentiel reviewer feels competend.', 'Areas of expertise'),
)

INDEXES = (
    ('Contributors','KeywordIndex'),
)
GLOBALS = globals()
