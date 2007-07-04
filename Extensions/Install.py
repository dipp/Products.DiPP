# -*- coding: utf-8 -*-
"""
 id: install
 title: Install DiPP workflow *optional*
 module name: DiPP.Install
 function name: install

 $Author: dippadm $
 $Revision: 1.7 $
 $Date: 2006/06/08 06:40:46 $
 $Id: Install.py,v 1.7 2006/06/08 06:40:46 dippadm Exp $

"""

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.DiPP import dippworkflow_globals
from Products.DiPP.config import PROJECTNAME, SKIN_NAMES, STYLESHEETS
from Products.DiPP.defaults import *
from Products.DiPP.Extensions.utils import *
from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes
from StringIO import StringIO


SITE_NAME = PROJECTNAME

def install_plone(self, out, site_id=SITE_NAME):
    """ add a Plone site to the Zope root and install a few Products """

    print >> out, "  Adding Plone site."
    self.manage_addProduct['CMFPlone'].manage_addSite(
            site_id,
            custom_policy = 'Default Plone')
    site = getSite(self, site_id)
    """
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'installReflow',
        'Installation Reflow',
        'CMFOpenflow.Install',
        'install')
    site.installReflow()
    """
    #I18NLayer und PLT per quickinstaller installieren!
    """
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'installI18N',
        'Installation I18N',
        'I18NLayer.Install',
        'install')
    site.installI18N()

    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'installPLT',
        'Installation PLT',
        'PloneLanguageTool.Install',
        'install')
    site.installPLT()
    """

    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'installCMFBoard',
        'Installation CMFBoard',
        'CMFBoard.Install',
        'install')
    site.installCMFBoard()
    
    site.invokeFactory('Folder','tmp')

def install_properties(self, out, site_id=SITE_NAME):
    """ Installation eine Propertysheets für DiPP-spezifische Variablen """

    site = getSite(self, site_id)
    if not hasattr(site.portal_properties, 'dipp_properties'):
        site.portal_properties.addPropertySheet('dipp_properties', 'DiPP properties')

    props = site.portal_properties.dipp_properties    
    site.portal_properties.navtree_properties.manage_changeProperties({'idsNotToList':('Members','tmp','ext','fedora_tmp')})
    site.portal_memberdata.manage_changeProperties({'wysiwyg_editor':'Epoz'})


    dipp_properties = (
        ('mysql_host','string','localhost'),
        ('mysql_user','string',''),
        ('mysql_passwd','string',''),
        ('mysql_table','string',''),
        ('mysql_db','string','dipp'),
        ('deadline_max','int',DEADLINE_MAX),
        ('deadline_default','int',DEADLINE_DEFAULT),
        ('deadline_red','int',DEADLINE_RED),
        ('deadline_yellow','int',DEADLINE_YELLOW),
        ('fedora_tmp','string','fedora'),
        ('ISSN','string',''),
        ('ldap_ou','string',''),
        ('ldap_server','string',''),
        ('container_id','string',''),
        ('articleTypes','lines',''),
        ('label','string',''),
        ('rssFeeds','lines',''),
        ('floatingtoc_enabled','boolean',''),
        ('floatingtoc_onload','boolean',''),
        ('alertEmailAddresses','lines',ALERT_EMAIL_ADDRESSES),
        ('alertEmailText','text',ALERT_EMAIL_TEXT),
    )

    for prop_id, prop_type, prop_value in dipp_properties:
        if not hasattr(props, prop_id):
            props._setProperty(prop_id, prop_value, prop_type)
    
    print >> out, "  DiPP-Properties installed"


def configure_workflow(self, out, site_id=SITE_NAME):
    """ Einrichten und Konfigurieren des Publikationsworkflows"""

    print >> out, "  Configuring the workflow."
    site = getSite(self, site_id)
    reftool = getToolByName(site, 'portal_openflow')

    # Set Reflow Process Definition
    process_id = 'Publishing'

    # Creates the PD object
    reftool.addProcess(process_id,
                  title = 'DiPP Workflow',
                  description = 'Digital Peer Publishing',
                  BeginEnd = 1)

    p = getattr(reftool, process_id)
    p.addActivity(id = 'initialize',
                  split_mode = 'and',
                  join_mode = 'and',
                  description = 'Artikel anlegen',
                  application = 'pub_initialize_form',
                  finish_mode = 1)
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

    site._addRole('Redakteur')
    site._addRole('Herausgeber')
    site._addRole('Autor')
    site._addRole('Gastherausgeber')

    print >> out, "    Assigning Permissions..."
    #Rollen und ihre Rechte
    redakteur = (
        'Use OpenFlow',
        'Manage properties',
        'Add portal content',
        'Access future portal content',
        'Access inactive portal content',
        'Add Documents, Images, and Files',
        'Change Images, and Files',
        'Add Folders',
        'Add portal folders',
        'Copy or Move',
        'Fedora: Add Content',
        'Fedora: Edit Content',
        'List folder contents',
    )

    herausgeber = (
        'Use OpenFlow',
        'Manage OpenFlow',
        'Manage properties',
        'Add portal content',
        'Access future portal content',
        'Access inactive portal content',
        'Add Documents, Images, and Files',
        'Change Images, and Files',
        'Add Folders',
        'Add portal folders',
        'Copy or Move'
        'Fedora: Add Content',
        'Fedora: Edit Content',
        'List folder contents',
    )

    autor = (
        'Use OpenFlow',
        'List folder contents',
    )

    gastherausgeber = (
        'Use OpenFlow',
    )
    
    anonymous = (
        'Fedora: View Content',
    ) 
    site.manage_role('Redakteur', redakteur)
    site.manage_role('Herausgeber', herausgeber)
    site.manage_role('Autor', autor)
    site.manage_role('Gastherausgeber', gastherausgeber)
    site.manage_role('Anonymous', anonymous)

    reftool.manage_role('Redakteur', ('Manage properties',))
    reftool.manage_role('Herausgeber', ('Manage properties',))
    reftool.manage_role('Autor', ('Manage properties',))
    reftool.manage_role('Gastherausgeber', ('Manage properties',))

    site.manage_addProperty(id = 'repository',               value = '/opt/digijournals/repository', type = 'string') 
    site.manage_addProperty(id = 'deadline_max',             value = 56, type = 'int') 
    site.manage_addProperty(id = 'deadline_default',         value = 14, type = 'int') 
    site.manage_addProperty(id = 'deadline_red',             value = 3, type = 'int') 
    site.manage_addProperty(id = 'deadline_yellow',          value = 10, type = 'int') 
    site.manage_addProperty(id = 'deadline_no',              value = '1970/01/01 12:00:00 GMT+1', type = 'date')
    site.manage_addProperty(id = 'deadline_change',          value = ('Herausgeber',), type = 'lines')
    site.manage_addProperty(id = 'deadline_next_change',     value = ('Herausgeber', 'Redakteur'), type = 'lines')
    site.manage_addProperty(id = 'deadline_red_email_de',    value = "Bitte umgehend den Artikel bearbeiten\n\nmfg", type = 'text')
    site.manage_addProperty(id = 'deadline_red_email_en',    value = "Bitte umgehend den Artikel bearbeiten\n\nmfg", type = 'text')
    site.manage_addProperty(id = 'deadline_yellow_email_de', value = "Bitte an die Bearbeitung des Artikels denken!\n\nmfg", type = 'text')
    site.manage_addProperty(id = 'deadline_yellow_email_en', value = "Bitte an die Bearbeitung des Artikels denken!\n\nmfg", type = 'text')
    site.manage_addProperty(id = 'defaultLanguage',          value = "de", type = 'string')
    site.manage_addProperty(id = 'author_notice_de',         value = "Ein Artikel liegt für Sie zur Begutachtung vor!\n\nmfg", type = 'text')
    site.manage_addProperty(id = 'author_notice_en',         value = "Ein Artikel liegt für Sie zur Begutachtung vor!\n\nmfg", type = 'text')
    site.manage_addProperty(id = 'roles_not_to_list',        value = ('Manager', 'Owner', 'Reviewer', 'Member'), type = 'lines')
    site.manage_addProperty(id = 'actions_to_list',          value = ('Call Application', 'Self Assign', 'Assign', 'Unassign'), type = 'lines')
    site.manage_addProperty(id = 'workflow_actions',         value = ('Call Application', 'Self Assign', 'Assign', 'Unassign', 'Suspend', 'Resume', 'Fallout', 'Fallin', 'End Fallin', 'Activate', 'Inactive', 'Complete', 'Forward'), type = 'lines')
    site.manage_addProperty(id = 'copy_of_reminder',         value = ('',), type = 'lines')
    site.manage_addProperty(id = 'gap_container',            value = 'TestJournal', type = 'string')
    site.manage_addProperty(id = 'PID',                      value = '', type = 'string')

    site.manage_changeProperties({'right_slots':''})
    left_slots = (
        'here/portlet_dippnav/macros/portlet',
        'here/portlet_status/macros/portlet',
        'here/portlet_toc/macros/portlet',
        'here/portlet_navigation/macros/portlet'
    )

    site.manage_changeProperties({'left_slots':left_slots})

    portal_actions = getToolByName(site, 'portal_actions')
    """
    portal_actions.addAction(
                id = 'worklist',
                name = 'my worklist',
                action = 'string: ${portal_url}/worklist',
                condition = '',
                permission = 'Use OpenFlow',
                category = 'user',
                visible = 1)

    portal_actions.addAction(
                id = 'all_worklists',
                name = 'all worklist',
                action = 'string: ${portal_url}/all_worklists',
                condition = '',
                permission = 'Manage OpenFlow',
                category = 'user',
                visible = 1)

    portal_actions.addAction(
                id = 'dipp_control_panel',
                name = 'dipp control panel',
                action = 'string: ${portal_url}/dipp_control_panel',
                condition = '',
                permission = 'Manage OpenFlow',
                category = 'user',
                visible  = 1)

    portal_actions.addAction(
                id = 'reminder',
                name = 'Mahnmail',
                action = 'string: ${portal_url}/ext/reminder',
                condition = '',
                permission = 'Manage OpenFlow',
                category = 'portal_tabs',
                visible = 0)
    """            
    portal_actions.addAction(
                id = 'Submit',
                name = 'Submit',
                action = 'string: ${portal_url}/submitemail_form',
                condition = '',
                permission = '',
                category = 'portal_tabs',
                visible = 1)
 

                
def install_subskins(self, out, skin_names=SKIN_NAMES, globals=dippworkflow_globals, site_id=SITE_NAME):
    """Installation von Subskins"""

    print >> out, "  Installing subskin."
    site = getSite(self, site_id)
    #site = self
    skinstool = getToolByName(site, 'portal_skins')
    for skin_name in skin_names:
        if skin_name not in skinstool.objectIds():
            print >> out, "    Adding directory view for dipp"
            addDirectoryViews(skinstool, 'skins', globals)

        for skinName in skinstool.getSkinSelections():
            path = skinstool.getSkinPath(skinName)
            path = [i.strip() for i in  path.split(',')]
            try:
                if skin_name not in path:
                    path.insert(path.index('custom') +1, skin_name)
            except ValueError:
                if skin_name not in path:
                    path.append(skin_name)

            path = ','.join(path)
            skinstool.addSkinSelection( skinName, path)

    skinstool.manage_properties(default_skin='Plone Tableless')
    
    print >> out, "  Done installing subskin."


def getSite(self, site_id):
    """ get a handle on the portal site"""

    #return getattr(self, site_id)
    return self
    
def install_extMethods(self, out, site_id=SITE_NAME):

    """ Installation von externen Methoden, sollte durch ein Tool ersetzt werden"""

    site = getSite(self, site_id)
    site.manage_addFolder('ext','Externe Methoden')
    site.manage_addFolder('fedora_tmp','Temporäre Fedoraobjekte')
    site.manage_addFolder('tmp','Temporäre Artikel')
    
    ext = getattr(site,'ext')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'listDir',
        'list directory content',
        'DiPP.listDir',
        'listDir')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'deadline_date',
        '',
        'DiPP.deadlines',
        'deadline_date')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'deadline_delay',
        '',
        'DiPP.deadlines',
        'deadline_delay')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'deadline_time',
        '',
        'DiPP.deadlines',
        'deadline_time')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'addArticle',
        '',
        'DiPP.add_article',
        'add_article')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'reminder',
        '',
        'DiPP.reminder',
        'reminder')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'membersOfGroup',
        '',
        'DiPP.ldap',
        'membersOfGroup')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'getMember',
        '',
        'DiPP.ldap',
        'member')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'usersAssignableTo',
        '',
        'DiPP.ldap',
        'usersAssignableTo')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'get_comments',
        '',
        'DiPP.history',
        'getComments')
    ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'history_insert',
        '',
        'DiPP.history',
        'insert')
   
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'LDAPAddEntry',
        'Benutzer in LDAP ergänzen',
        'DiPP.ldap',
        'addEntry')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'LDAPAuth',
        'An LDAPServer authentifizieren',
        'DiPP.ldap',
        'auth')
                         
                         
def install_fedoraExtMethods(self, out, site_id=SITE_NAME):
    """ Installation von externen Methoden für den Fedorazugriff, sollte durch ein Tool ersetzt werden"""

    site = getSite(self, site_id)
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraAccess',
        'Zugriff auf Fedora Texte',
        'DiPP.fedoraOverSOAP',
        'access')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraAccessImage',
        'Zugriff auf Fedora Images',
        'DiPP.fedoraOverSOAP',
        'accessImage')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraAddDatastream',
        'Neuen Datenstrom hinzufügen',
        'DiPP.fedoraOverSOAP',
        'addDatastream')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraContent',
        'hollt den Content einer PID',
        'DiPP.fedoraOverSOAP',
        'getContentModel')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraCreateNewArticle',
        'einen neuen Artikel anlegen',
        'DiPP.fedoraOverSOAP',
        'createNewArticle')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraCreateNewContainer',
        'Neues Hierarchieelement anlegen',
        'DiPP.fedoraOverSOAP',
        'createNewContainer')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraGetQDC',
        'holt die qualifizierten DC Daten',
        'DiPP.fedoraOverSOAP',
        'getQualifiedDCMetadata')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraGetdatastreams',
        'alle Datenströme eines digitalen Objektes',
        'DiPP.fedoraOverSOAP',
        'getDatastreams')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraModifyDatastreamByReference',
        'neue Version eines Datebstroms anlegen',
        'DiPP.fedoraOverSOAP',
        'modifyDatastreamByReference')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraModifyObject',
        'Status eines digitalen Objektes ändern',
        'DiPP.fedoraOverSOAP',
        'modifyObject')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraSearch',
        'Suchen in Fedora',
        'DiPP.fedoraOverSOAP',
        'search')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraSetQDC',
        'modifiziert Qualified DC Metadaten einer PID',
        'DiPP.fedoraOverSOAP',
        'setQualifiedDCMetadata')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'fedoraSetURL',
        'modifiziert URL einer PID',
        'DiPP.fedoraOverSOAP',
        'setURL')
    site.manage_addProduct['ExternalMethod'].manage_addExternalMethod(
        'getTempID',
        'generiert temporäre id zum zwischenspeichern',
        'DiPP.fedoraOverSOAP',
        'getTempID')

def install_types(self, out, site_id=SITE_NAME):
    """Registrierungen der neuen Objekte """

    site = getSite(self, SITE_NAME)
    installTypes(site, out,
                 listTypes(PROJECTNAME),
                 PROJECTNAME)

    # Register FedoraFolder
    props = site.portal_properties.site_properties
    tabs = getattr(props, 'use_folder_tabs')
    contents = getattr(props, 'use_folder_contents')
    
    if 'FedoraHierarchie' not in tabs:
        newtabs = list(tabs)
        newtabs.append('FedoraHierarchie')
        props._updateProperty('use_folder_tabs', newtabs)
        
    if 'FedoraHierarchie' not in contents:
        newcontents = list(contents)
        newcontents.append('FedoraHierarchie')
        props._updateProperty('use_folder_contents', newcontents)

    if 'FedoraArticle' not in tabs:
        newtabs = list(tabs)
        newtabs.append('FedoraArticle')
        props._updateProperty('use_folder_tabs', newtabs)
        
    if 'FedoraArticle' not in contents:
        newcontents = list(contents)
        newcontents.append('FedoraArticle')
        props._updateProperty('use_folder_contents', newcontents)

def install_configlet(self,out):
    try:
        cp=self.portal_controlpanel
        cp.addAction(id='dipp_configuration',
                     name='DiPP configuration',
                     action='string:${portal_url}/prefs_deadlines_form',
                     permission='Manage portal',
                     category='Products',
                     appId='DiPP',
                     imageUrl='dipp_icon.gif',
                     description='Configure DiPP Publicationsystem')
    except:
        pass
        
def install_css(self,out):
    """register the stylesheets"""
    registerResources(self, out, 'portal_css', STYLESHEETS)

def install_memberproperties(self,out):
    """add some memberproperties"""
    md = self.portal_memberdata
    md.manage_addProperty(id = 'academictitle', value = '', type = 'string')
    md.manage_addProperty(id = 'givenname', value = '', type = 'string')
    md.manage_addProperty(id = 'surname', value = '', type = 'string')
    md.manage_addProperty(id = 'organization', value = '', type = 'string')
    md.manage_addProperty(id = 'postaladdress', value = '', type = 'string')
    md.manage_addProperty(id = 'postalcode', value = '', type = 'string')
    md.manage_addProperty(id = 'phone', value = '', type = 'string')

    if not hasattr(self.portal_properties, 'member_properties'):
        self.portal_properties.addPropertySheet('member_properties', 'Extended member properties')

    member_props= (
        ('academictitle_visible','boolean',True),
        ('academictitle_required','boolean',False),
        ('givenname_visible','boolean',True),
        ('givenname_required','boolean',False),
        ('surname_visible','boolean',True),
        ('surname_required','boolean',False),
        ('organization_visible','boolean',True),
        ('organization_required','boolean',False),
        ('postaladdress_visible','boolean',True),
        ('postaladdress_required','boolean',False),
        ('postalcode_visible','boolean',True),
        ('postalcode_required','boolean',False),
        ('phone_visible','boolean',True),
        ('phone_required','boolean',False),
        ('location_visible','boolean',True),
        ('location_required','boolean',False),
    )

    props = self.portal_properties.member_properties

    for prop_id, prop_type, prop_value in member_props:
        if not hasattr(props, prop_id):
            #props._setProperty(prop_id, prop_value, prop_type)
            props.manage_addProperty(id = prop_id, value = prop_value, type =  prop_type)
    
def install(self):
    """ install a dipp instance"""
    out = StringIO()

    #install_plone(self, out)
    install_properties(self, out)
    install_memberproperties(self, out)
    install_subskins(self, out)
    install_extMethods(self, out)
    #install_fedoraExtMethods(self, out)
    install_types(self, out)
    install_css(self,out)
    install_configlet(self, out)
    configure_workflow(self, out)

    
    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()

