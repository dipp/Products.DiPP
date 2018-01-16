# -*- coding: utf-8 -*-
"""
 Install and Uninstall script for this product
 $Id$
"""

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes
from zExceptions import NotFound, BadRequest
from StringIO import StringIO
from Products.DiPP import dippworkflow_globals
from Products.DiPP.config import PROJECTNAME, DEPENDENCIES, VOCABULARIES, TOOLS
from Products.DiPP.defaults import *
from Products.DiPP.mail_templates import *
from Products.DiPP.Extensions.utils import *
from Products.DiPP import HAS_PLONE30

SITE_NAME = PROJECTNAME


def install_properties(self, out, site_id=SITE_NAME):
    """Installation eine Propertysheets für DiPP-spezifische Variablen."""
    site = getSite(self, site_id)

    if not hasattr(site.portal_properties, 'dipp_properties'):
        site.portal_properties.addPropertySheet('dipp_properties', 'DiPP properties')

    props = site.portal_properties.dipp_properties
    site.portal_properties.navtree_properties.manage_changeProperties({'idsNotToList': ('Members', 'tmp', 'ext', 'fedora_tmp')})
    site.portal_memberdata.manage_changeProperties({'wysiwyg_editor': WYSIWYG_EDITOR})

    dipp_properties = (
        ('deadline_max', 'int', DEADLINE_MAX) ,
        ('deadline_default', 'int', DEADLINE_DEFAULT),
        ('deadline_red', 'int', DEADLINE_RED),
        ('deadline_yellow', 'int', DEADLINE_YELLOW),
        ('deadline_no', 'date', '1970/01/01 12:00:00 GMT+1'),
        ('deadline_change', 'lines', ('Herausgeber',)),
        ('deadline_next_change', 'lines', ('Herausgeber', 'Redakteur')),
        ('deadline_red_email_de', 'text', "Bitte umgehend den Artikel bearbeiten\n\nmfg"),
        ('deadline_red_email_en', 'text', "Bitte umgehend den Artikel bearbeiten\n\nmfg"),
        ('deadline_yellow_email_de', 'text', "Bitte an die Bearbeitung des Artikels denken!\n\nmfg"),
        ('deadline_yellow_email_en', 'text', "Bitte an die Bearbeitung des Artikels denken!\n\nmfg"),
        ('defaultLanguage', 'string', "de"),
        ('roles_not_to_list', 'lines', ('Manager', 'Owner', 'Reviewer', 'Member')),
        ('actions_to_list', 'lines', ('Call Application', 'Self Assign', 'Assign', 'Unassign')),
        ('workflow_actions', 'lines', ('Call Application', 'Self Assign', 'Assign', 'Unassign', 'Suspend', 'Resume', 'Fallout', 'Fallin', 'End Fallin', 'Activate', 'Inactive', 'Complete', 'Forward')),
        ('copy_of_reminder', 'lines', ('',)),
        ('author_notice_de', 'text', AUTHOR_NOTICE_DE),
        ('author_notice_en', 'text', AUTHOR_NOTICE_EN),
        ('ISSN', 'string', ''),
        ('articleTypes', 'lines', ''),
        ('label', 'string', ''),
        ('rssFeeds', 'lines', ''),
        ('floatingtoc_enabled', 'boolean', ''),
        ('floatingtoc_onload', 'boolean', ''),
        ('alertEmailAddresses', 'lines', ALERT_EMAIL_ADDRESSES),
        ('alertEmailText', 'text', ALERT_EMAIL_TEXT),
        ('citation_format', 'text', CITATION_FORMAT),
        ('issue_date_format', 'string', ISSUE_DATE_FORMAT),
        ('default_article_view', 'string', ''),
        ('short_citation_format', 'text', SHORT_CITATION_FORMAT),
        ('show_recommended_citation', 'boolean', True),
        ('show_classified_subjects', 'boolean', False),
        ('show_review_history', 'boolean', False),
        ('initials_only', 'boolean', True),
        ('firstnamefirst', 'boolean', False),
        ('initials_period', 'boolean', False),
        ('comma_separated', 'boolean', False),
        ('last_author_suffix', 'string', ''),
        ('articles_in_portlet', 'boolean', True),
        ('authors_in_portlet', 'boolean', True),
        ('allow_persistent_discussion', 'boolean', False),
        ('volume_show_covers', 'boolean', False),
        ('issue_show_abstracts', 'boolean', False),
        ('issue_show_pdf_link', 'boolean', False),
        ('issue_show_full_abstracts', 'boolean', False),
        ('issue_show_short_citation', 'boolean', False),
        ('issue_sort_on', 'string', 'getObjPositionInParent'),
        ('issue_sort_order', 'string', 'ascending'),
        ('discussion_time', 'int', 0),
        ('fedora_time_format', 'string', '%Y-%m-%dT%H:%M:%SZ'),
        ('issue_date_format', 'string', ''),
        ('recent_articles_range', 'int', 30),
        ('hide_current_issue', 'boolean', False),
        ('deepest_toc_level', 'int', 6),
        ('awstats_id', 'string', ''),
        ('enable_ebookey', 'boolean', False),
    )

    for prop_id, prop_type, prop_value in dipp_properties:
        if not hasattr(props, prop_id):
            props._setProperty(prop_id, prop_value, prop_type)

    print >> out, "DiPP-Properties installed"

    if not hasattr(self.portal_properties, 'dippreview_properties'):
        self.portal_properties.addPropertySheet('dippreview_properties', 'DiPPReview properties')

    props = self.portal_properties.dippreview_properties

    dippreview_properties = (
        ('submission_counter',                    'int',    0),
        ('submission_prefix',                     'string', 'dipp'),
        ('max_review_time',                       'float',  70),
        ('review_time',                           'float',  42),
        ('min_reviewers',                         'int',    2),
        ('friendly_reminder_times',               'lines',  (3, 7, 14)),
        ('deadline_reminder_times',               'lines',  (7, 2)),
        ('due_reminder_times',                    'lines',  (1, 4, 10)),
        ('abstract_length',                       'int',    2000),
        ('manuscript_mimetypes',                  'lines',  ('application/rtf', 'application/pdf')),
        ('additional_manuscript_files',           'boolean', True),
        ('supplementary_mimetypes',               'lines',  ('application/rtf', 'application/pdf')),
        ('votes',                                 'lines',  ('accept', 'accept with remarks', 'reject')),
        ('email_header', 'text', EMAIL_HEADER),
        ('email_footer', 'text', EMAIL_FOOTER),
        ('submit_pr_sectioneditor_subject', 'string', SUBMIT_PR_SECTIONEDITOR_SUBJECT),
        ('submit_pr_sectioneditor_mail', 'text', SUBMIT_PR_SECTIONEDITOR_MAIL),
        ('submit_pr_author_subject', 'string', SUBMIT_PR_AUTHOR_SUBJECT),
        ('submit_pr_author_mail', 'text', SUBMIT_PR_AUTHOR_MAIL),
        ('submitreview_pr_sectioneditor_subject', 'string', SUBMITREVIEW_PR_SECTIONEDITOR_SUBJECT),
        ('submitreview_pr_sectioneditor_mail', 'text', SUBMITREVIEW_PR_SECTIONEDITOR_MAIL),
        ('submitreview_pr_reviewer_subject', 'string', SUBMITREVIEW_PR_REVIEWER_SUBJECT),
        ('submitreview_pr_reviewer_mail', 'text', SUBMITREVIEW_PR_REVIEWER_MAIL),
        ('requestrevision_pr_author_subject', 'string', REQUESTREVISION_PR_AUTHOR_SUBJECT),
        ('requestrevision_pr_author_mail', 'text', REQUESTREVISION_PR_AUTHOR_MAIL),
        ('reject_pr_reviewer_subject', 'string', REJECT_PR_REVIEWER_SUBJECT),
        ('reject_pr_reviewer_mail', 'text', REJECT_PR_REVIEWER_MAIL),
        ('reject_pr_author_subject', 'string', REJECT_PR_AUTHOR_SUBJECT),
        ('reject_pr_author_mail', 'text', REJECT_PR_AUTHOR_MAIL),
        ('invite_pr_reviewer_subject', 'string', INVITE_PR_REVIEWER_SUBJECT),
        ('invite_pr_reviewer_mail', 'text', INVITE_PR_REVIEWER_MAIL),
        ('friendly_reminder_pr_reviewer_subject', 'string', FRIENDLY_REMINDER_PR_REVIEWER_SUBJECT),
        ('friendly_reminder_pr_reviewer_mail', 'text', FRIENDLY_REMINDER_PR_REVIEWER_MAIL),
        ('due_reminder_pr_sectioneditor_subject', 'string', DUE_REMINDER_PR_SECTIONEDITOR_SUBJECT),
        ('due_reminder_pr_sectioneditor_mail', 'text', DUE_REMINDER_PR_SECTIONEDITOR_MAIL),
        ('due_reminder_pr_reviewer_subject', 'string', DUE_REMINDER_PR_REVIEWER_SUBJECT),
        ('due_reminder_pr_reviewer_mail', 'text', DUE_REMINDER_PR_REVIEWER_MAIL),
        ('deskreject_pr_author_subject', 'string', DESKREJECT_PR_AUTHOR_SUBJECT),
        ('deskreject_pr_author_mail', 'text', DESKREJECT_PR_AUTHOR_MAIL),
        ('decline_pr_sectioneditor_subject', 'string', DECLINE_PR_SECTIONEDITOR_SUBJECT),
        ('decline_pr_sectioneditor_mail', 'text', DECLINE_PR_SECTIONEDITOR_MAIL),
        ('deadline_reminder_pr_sectioneditor_subject', 'string', DEADLINE_REMINDER_PR_SECTIONEDITOR_SUBJECT),
        ('deadline_reminder_pr_sectioneditor_mail', 'text', DEADLINE_REMINDER_PR_SECTIONEDITOR_MAIL),
        ('deadline_reminder_pr_reviewer_subject', 'string', DEADLINE_REMINDER_PR_REVIEWER_SUBJECT),
        ('deadline_reminder_pr_reviewer_mail', 'text', DEADLINE_REMINDER_PR_REVIEWER_MAIL),
        ('accept_pr_sectioneditor_subject', 'string', ACCEPT_PR_SECTIONEDITOR_SUBJECT),
        ('accept_pr_sectioneditor_mail', 'text', ACCEPT_PR_SECTIONEDITOR_MAIL),
        ('accept_pr_reviewer_subject', 'string', ACCEPT_PR_REVIEWER_SUBJECT),
        ('accept_pr_reviewer_mail', 'text', ACCEPT_PR_REVIEWER_MAIL),
        ('accept_pr_author_subject', 'string', ACCEPT_PR_AUTHOR_SUBJECT),
        ('accept_pr_author_mail', 'text', ACCEPT_PR_AUTHOR_MAIL)
    )

    for prop_id, prop_type, prop_value in dippreview_properties:
        if not hasattr(props, prop_id):
            props._setProperty(prop_id, prop_value, prop_type)
    print >> out, "DiPP-Review Properties installed"

    props = self.portal_properties.site_properties

    site_properties = (
        ('analytics_id', 'int', None),
        ('analytics_server', 'string', ''),
    )
    for prop_id, prop_type, prop_value in site_properties:
        if not hasattr(props, prop_id):
            props._setProperty(prop_id, prop_value, prop_type)
    print >> out, "Site Properties installed"


def configure_workflow(self, out, site_id=SITE_NAME):
    """Einrichten und Konfigurieren des Publikationsworkflows."""
    print >> out, "  Configuring the workflow."
    site = getSite(self, site_id)
    reftool = getToolByName(site, 'portal_openflow')

    # Set Reflow Process Definition
    process_id = 'Publishing'

    # Creates the PD object
    reftool.addProcess(
        process_id,
        title='DiPP Workflow',
        description='Digital Peer Publishing',
        BeginEnd=1
    )

    p = getattr(reftool, process_id)
    p.addActivity(id='initialize',
                  split_mode='and',
                  join_mode='and',
                  description='Artikel anlegen',
                  application='pub_initialize_form',
                  finish_mode=1)
    reftool.addApplication('pub_initialize_form', '../pub_initialize_form')

    p.addActivity(id = 'bearbeiten',
                  split_mode = 'and',
                  join_mode = 'xor',
                  description = 'Artikeldateien bearbeiten',
                  application = 'pub_edit_form',
                  finish_mode = 1)
    reftool.addApplication('pub_edit_form', '../pub_edit_form')

    p.addActivity(id = 'begutachten',
                  split_mode = 'xor',
                  join_mode = 'xor',
                  description = 'Artikeldateien begutachten',
                  application = 'pub_check_form',
                  finish_mode = 1)
    reftool.addApplication('pub_check_form', '../pub_check_form')

    p.addActivity(id = 'freischalten',
                  split_mode = 'and',
                  join_mode = 'and',
                  description = 'Artikel freigeben',
                  application = 'pub_publish_form',
                  finish_mode = 1)
    reftool.addApplication('pub_publish_form', '../pub_publish_form')

    p.addActivity(id = 'imprimatur',
                  split_mode = 'and',
                  join_mode = 'and',
                  description = 'Imprimatur des Autors',
                  application = 'pub_imprimatur_form',
                  auto_push_mode = 1,
                  push_application = 'route_to_author',
                  finish_mode = 1)
    reftool.addApplication('pub_imprimatur_form', '../pub_imprimatur_form')
    reftool.addApplication('route_to_author', 'route_to_author')

    p.addActivity(id = 'anschreiben',
                  split_mode = 'and',
                  join_mode = 'and',
                  description = 'Autor Anschreiben',
                  application = 'pub_notice_form',
                  finish_mode = 1)
    reftool.addApplication('pub_notice_form', '../pub_notice_form')

    p.addActivity(id = 'absegnen',
                  split_mode = 'and',
                  join_mode = 'and',
                  description = 'Segen des Gastherausgebers',
                  application = 'pub_approve_form',
                  finish_mode = 1)
    reftool.addApplication('pub_approve_form', '../pub_approve_form')

    # Edit the Begin and End activities
    begin = getattr(p,'Begin')
    begin.edit(split_mode = 'and', join_mode = 'and', kind = 'dummy')
    end = getattr(p,'End')
    end.edit(split_mode = 'and', join_mode = 'and', kind = 'dummy')

    # Creates Transitions
    p.addTransition(id = 'Begin_initialize',
                    From = 'Begin',
                    To = 'initialize')

    p.addTransition(id = 'initialize_bearbeiten',
                    From = 'initialize',
                    To = 'bearbeiten')

    p.addTransition(id = 'bearbeiten_begutachten',
                    From = 'bearbeiten',
                    To = 'begutachten')

    p.addTransition(id = 'begutachten_bearbeiten',
                    From = 'begutachten',
                    To = 'bearbeiten',
                    condition = 'python:not here.formalOK')

    p.addTransition(id = 'imprimatur_begutachten',
                    From = 'imprimatur',
                    To = 'begutachten')

    p.addTransition(id = 'begutachten_freischalten',
                    From = 'begutachten',
                    To = 'freischalten',
                    condition = 'python:here.formalOK and here.autorOK and here.gastHrsgOK')

    p.addTransition(id = 'freischalten_end',
                    From = 'freischalten',
                    To = 'End')

    p.addTransition(id = 'begutachten_anschreiben',
                    From = 'begutachten',
                    To = 'anschreiben',
                    condition = 'python:here.formalOK and not here.autorOK')

    p.addTransition(id = 'anschreiben_imprimatur',
                    From = 'anschreiben',
                    To = 'imprimatur')

    p.addTransition(id = 'begutachten_absegnen',
                    From = 'begutachten',
                    To = 'absegnen',
                    condition = 'python:here.formalOK and here.autorOK and not here.gastHrsgOK')

    p.addTransition(id = 'absegnen_begutschten',
                    From = 'absegnen',
                    To = 'begutachten')

    print >> out, "Added Transitions\n"

    # Set Pull or Push permissions on the activities
    reftool[process_id]['bearbeiten'].editPushPermissionsRoles(['Manager', 'Herausgeber'])
    reftool[process_id]['bearbeiten'].editPullPermissionsRoles(['Manager', 'Redakteur'])
    reftool[process_id]['begutachten'].editPullPermissionsRoles(['Manager', 'Herausgeber'])
    reftool[process_id]['freischalten'].editPullPermissionsRoles(['Manager', 'Herausgeber'])
    reftool[process_id]['imprimatur'].editPushPermissionsRoles(['Manager', 'Herausgeber'])
    reftool[process_id]['imprimatur'].editPullPermissionsRoles(['Manager', 'Autor'])
    reftool[process_id]['anschreiben'].editPullPermissionsRoles(['Manager', 'Herausgeber'])
    reftool[process_id]['absegnen'].editPushPermissionsRoles(['Manager', 'Herausgeber'])
    reftool[process_id]['absegnen'].editPullPermissionsRoles(['Manager', 'Gastherausgeber'])

    print >> out, 'Set Pull or Push permissions\n'

    print >> out,'DiPP Workflow Setup Done\n Finished\n'


    portal_actions = getToolByName(site, 'portal_actions')

    portal_actions.addAction(
                id = 'Submit',
                name = 'Submit',
                action = 'string: ${portal_url}/submitemail_form',
                condition = '',
                permission = '',
                category = 'portal_tabs',
                visible = 1)

    portal_actions.addAction(
                id = 'authors',
                name = 'Authors',
                action = 'string: ${portal_url}/authors',
                condition = '',
                permission = '',
                category = 'portal_tabs',
                visible = 1)

    portal_actions.addAction(
                id = 'currentissue',
                name = 'Current issue',
                action = 'string: ${portal_url}/currentissue',
                condition = '',
                permission = '',
                category = 'portal_tabs',
                visible = 1)

def install_groups_and_roles(self, out, site_id=SITE_NAME):

    print >> out, "Configuring groups"
    site = getSite(self, site_id)
    groups = ('Herausgeber', 'Redakteure', 'Gastherausgeber', 'Autoren', 'Manager', 'peerreviewer', 'sectioneditors')

    for group in groups:
        site.portal_groups.addGroup(group,(),())

    site.portal_groups.editGroup('Autoren', ['Peer'])

    roles =('pr_Author', 'pr_EditorInChief', 'pr_GuestEditor', 'pr_Reviewer', 'pr_ReviewerInvited', 'pr_SectionEditor')

    for role in roles:
        site._addRole(role)

    # permissions in OpenFlow
    reftool = getToolByName(site, 'portal_openflow')
    for role in ['Redakteur','Herausgeber', 'Autor', 'Gastherausgeber', 'Peer']:
        reftool.manage_role(role, ('Manage properties',))


    print >> out, "Set roles to groups"


def getSite(self, site_id):
    """Get a handle on the portal site."""
    return self


def install_metadataproperties(self, out):
    """Available metadata and default values."""

    if not hasattr(self.portal_properties, 'metadata_properties'):
        self.portal_properties.addPropertySheet('metadata_properties', 'QDC Metadata properties')

    props = self.portal_properties.metadata_properties

    metadata_props = (
        ('journalname', 'string', ''),
        ('journalname_abbr', 'string', ''),
        ('publisher', 'string', ''),
        ('issn', 'string', ''),
        ('doi_prefix', 'string', ''),
        ('default_pubType', 'string', 'article'),
        ('default_docType', 'string', 'text'),
        ('default_language', 'string', DEFAULT_LANGUAGE),
        ('available_languages', 'lines', AVAILABLE_LANGUAGES)
    )

    for prop_id, prop_type, prop_value in metadata_props:
        if not hasattr(props, prop_id):
            props.manage_addProperty(id=prop_id, value=prop_value, type=prop_type)


def install_dependencies(self,out,site_id=SITE_NAME):
    """Try to install dependencies to other products"""

    print >> out, "Dependency %s:" % str(len(DEPENDENCIES))
    site = getSite(self, site_id)
    quickinstaller = site.portal_quickinstaller
    for dependency in DEPENDENCIES:
        print >> out, "Installing dependency %s:" % dependency
        quickinstaller.installProduct(dependency)
        get_transaction().commit(1)


def create_vocabularies(self, out, site_id=SITE_NAME):
    """Create required vocabularies."""

    site = getSite(self, site_id)
    atvm = site.portal_vocabularies
    for type, name, description, title in VOCABULARIES:
        if not hasattr(atvm, name):
            atvm.invokeFactory(type, name, title=title, description=description, sortMethod='getObjPositionInParent')
            vocab = atvm.getVocabularyByName(name)
            print >> out, vocab
            key = 'no-section'
            value = 'No section'
            if vocab.id == 'journal-sections' and not hasattr(vocab, key):
                vocab.invokeFactory('SimpleVocabularyTerm', key)
                vocab[key].setTitle(value)
                vocab[key].reindexObject()
            vocab.reindexObject()

            print >> out, "created vocabulary %s" % title
        else:
            print >> out, "vocabulary %s exists" % title


def install_tools(self, out, site_id=SITE_NAME):
    """install tools"""

    site = getSite(self, site_id)
    for tool in TOOLS:
        try:
            site.manage_addProduct[PROJECTNAME].manage_addTool(tool)
        except BadRequest:
            # if an instance with the same name already exists this error will
            # be swallowed. Zope raises in an unelegant manner a 'Bad Request' error
            pass


def install_profiles(self, out, site_id=SITE_NAME):

    site = getSite(self, site_id)
    setup_tool = getToolByName(site, 'portal_setup')
    if HAS_PLONE30:
        setup_tool.runAllImportStepsFromProfile('profile-DiPP:install')
    else:
        setup_tool.setImportContext('profile-DiPP:install')
        setup_tool.runAllImportSteps()
        setup_tool.setImportContext('profile-CMFPlone:plone')
    print >> out, "Ran all import steps."


def uninstall_profiles(self, out, site_id=SITE_NAME):

    site = getSite(self, site_id)
    setup_tool = getToolByName(site, 'portal_setup')
    if HAS_PLONE30:
        pass
    else:
        setup_tool.setImportContext('profile-DiPP:uninstall')
        setup_tool.runAllImportSteps()
        setup_tool.setImportContext('profile-CMFPlone:plone')
    print >> out, "Ran all uninstall steps."


def install(self):
    """ install a dipp instance"""
    out = StringIO()

    if not HAS_PLONE30:
        install_dependencies(self, out)
        reftool = getToolByName(self, 'portal_openflow')
        process_id = 'Publishing'
        if not hasattr(reftool, process_id):
            configure_workflow(self, out)
        else:
            print >> out, "Keeping existingworkflow"

    install_properties(self, out)
    install_metadataproperties(self, out)
    install_profiles(self, out)
    install_groups_and_roles(self, out)
    install_tools(self, out)
    create_vocabularies(self, out)

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()


def uninstall(self, site_id=SITE_NAME):
    """Uninstall the DiPP Product.

    * Root properties are not removed
    * Member properties are not removed
    """
    out = StringIO()
    site = getSite(self, site_id)

    # remove configlet
    portal_conf = getToolByName(self, 'portal_controlpanel')
    portal_conf.unregisterConfiglet('dipp_configuration')

    # uninstall_profiles(self,out)

    return out.getvalue()
