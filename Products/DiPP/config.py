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

PUBTYPES = {
    'article':'Zeitschriftenartikel',
    'report':'Bericht',
    'paper':'Paper',
    'conf-proceeding':'Tagungs- und Konferenzbeitrag',
    'lecture':'Vorlesung'
}

DOCTYPES = {
    'text':'Text',
    'image':'Bilder',
    'multimedia':'Multimediadateien',
    'data':'Daten'
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
COMMENT_SELECTION_TITLE_LENGTH = 6

TOOLS = ((
    'Fedora2DiPP3',
    'BibTool',
    'Utils',
    'Deadlines',
    'DiPP Sections Tool', 
    'DiPP Peerreview Tool'
    )
)

INDEXES = (
    ('Contributors', 'KeywordIndex'),
    ('getAuthors', 'KeywordIndex'),
    ('getComment_to', 'FieldIndex'),
    ('getIssue', 'FieldIndex'),
    ('getIssueDate', 'DateIndex'),
    ('getJournal_section', 'FieldIndex'),
    ('getMMType', 'FieldIndex'),
    ('getPID', 'FieldIndex'),
    ('getSubject_areas', 'KeywordIndex'),
    ('getURN', 'FieldIndex'),
    ('getDOI', 'FieldIndex'),
    ('getVolume', 'FieldIndex'),
)
GLOBALS = globals()


# reCAPTCHA
PRIVATE_KEY   = "6Lf2WOISAAAAAE1enAqHSxX4Y6LIgD6LaRpiCCyZ"
PUBLIC_KEY    = "6Lf2WOISAAAAABFXeiCcDPfiznOzCgymL5KC54cY"
VERIFY_SERVER = "www.google.com"

# Configuration for the testrunner

PID = 'dipp:1898'
label = '81' 
address = '193.30.112.98'
port = '9280'
