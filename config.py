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
    {'id': "dipp_article.css", 'media': 'screen', 'rendering': 'import'},
    {'id': "dipp_article_print.css", 'media': 'print', 'rendering': 'import'}
)
        
GLOBALS = globals()
