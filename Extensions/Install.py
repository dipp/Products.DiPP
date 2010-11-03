# -*- coding: utf-8 -*-
"""
 Install and Uninstall script for this product
 $Id$
"""

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.DiPP import dippworkflow_globals
from Products.DiPP.config import PROJECTNAME, SKIN_NAMES, STYLESHEETS, DEPENDENCIES, VOCABULARIES, INDEXES, TOOLS
from Products.DiPP.defaults import *
from Products.DiPP.welcome import *
from Products.DiPP.Extensions.utils import *
from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes
from zExceptions import NotFound, BadRequest
from StringIO import StringIO


SITE_NAME = PROJECTNAME


def install_properties(self, out, site_id=SITE_NAME):
    """ Installation eine Propertysheets für DiPP-spezifische Variablen """

    site = getSite(self, site_id)
    if not hasattr(site.portal_properties, 'dipp_properties'):
        site.portal_properties.addPropertySheet('dipp_properties', 'DiPP properties')

    props = site.portal_properties.dipp_properties    
    site.portal_properties.navtree_properties.manage_changeProperties({'idsNotToList':('Members','tmp','ext','fedora_tmp')})
    site.portal_memberdata.manage_changeProperties({'wysiwyg_editor':WYSIWYG_EDITOR})


    dipp_properties = (
        ('deadline_red', 'int', DEADLINE_RED),
        ('deadline_yellow', 'int', DEADLINE_YELLOW),
        ('author_notice_de','text',AUTHOR_NOTICE_DE),
        ('author_notice_en','text',AUTHOR_NOTICE_EN),
        ('fedora_tmp', 'string', 'fedora'),
        ('ISSN', 'string', ''),
        ('articleTypes', 'lines', ''),
        ('label', 'string', ''),
        ('rssFeeds', 'lines', ''),
        ('floatingtoc_enabled', 'boolean', ''),
        ('floatingtoc_onload', 'boolean', ''),
        ('alertEmailAddresses', 'lines', ALERT_EMAIL_ADDRESSES),
        ('alertEmailText', 'text', ALERT_EMAIL_TEXT),
        ('citation_format', 'text', CITATION_FORMAT),
        ('default_article_view', 'string', ''),
        ('short_citation_format', 'text', SHORT_CITATION_FORMAT),
        ('show_recommended_citation', 'boolean', True),
        ('initials_only', 'boolean', True),
        ('initials_period', 'boolean', False),
        ('comma_separated', 'boolean', False),
        ('articles_in_portlet','boolean',True),
        ('authors_in_portlet','boolean',True),
        ('allow_persistent_discussion', 'boolean', False),
        ('volume_show_covers', 'boolean', False),
        ('issue_show_abstracts', 'boolean', False),
        ('issue_show_full_abstracts', 'boolean', False),
        ('discussion_time', 'int', 0),
        ('fedora_time_format', 'string','%Y-%m-%dT%H:%M:%SZ')
    )

    for prop_id, prop_type, prop_value in dipp_properties:
        if not hasattr(props, prop_id):
            props._setProperty(prop_id, prop_value, prop_type)
    
    print >> out, "DiPP-Properties installed"

    site_properties = (
        ('deadline_max',56,'int') ,
        ('deadline_default',14,'int'), 
        ('deadline_red',3,'int'),
        ('deadline_yellow',10,'int'), 
        ('deadline_no','1970/01/01 12:00:00 GMT+1','date'),
        ('deadline_change',('Herausgeber',),'lines'),
        ('deadline_next_change',('Herausgeber', 'Redakteur'),'lines'),
        ('deadline_red_email_de',"Bitte umgehend den Artikel bearbeiten\n\nmfg",'text'),
        ('deadline_red_email_en',"Bitte umgehend den Artikel bearbeiten\n\nmfg",'text'),
        ('deadline_yellow_email_de',"Bitte an die Bearbeitung des Artikels denken!\n\nmfg",'text'),
        ('deadline_yellow_email_en',"Bitte an die Bearbeitung des Artikels denken!\n\nmfg",'text'),
        ('defaultLanguage',"de",'string'),
        ('author_notice_de',AUTHOR_NOTICE_DE,'text'),
        ('author_notice_en',AUTHOR_NOTICE_EN,'text'),
        ('roles_not_to_list',('Manager', 'Owner', 'Reviewer', 'Member'),'lines'),
        ('actions_to_list',('Call Application', 'Self Assign', 'Assign', 'Unassign'),'lines'),
        ('workflow_actions',('Call Application', 'Self Assign', 'Assign', 'Unassign', 'Suspend', 'Resume', 'Fallout', 'Fallin', 'End Fallin', 'Activate', 'Inactive', 'Complete', 'Forward'),'lines'),
        ('copy_of_reminder',('',),'lines')
    )
    
    for prop_id, prop_value, prop_type in site_properties:
        if not site.hasProperty(prop_id):
            site.manage_addProperty(id = prop_id, value = prop_value, type = prop_type)


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
    
    groups = ('Herausgeber', 'Redakteure', 'Gastherausgeber', 'Autoren','Manager')
    
    for group in groups:
        site.portal_groups.addGroup(group,(),())
        
    print >> out, "Set roles to groups"
    

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

    
    print >> out, "  Done installing subskin."


def getSite(self, site_id):
    """ get a handle on the portal site"""

    #return getattr(self, site_id)
    return self
    
def install_extMethods(self, out, site_id=SITE_NAME):
    """ Installation von externen Methoden, sollte durch ein Tool ersetzt werden"""

    site = getSite(self, site_id)
    folders = ()
    try:
        ext = getattr(site,'ext')
    except:
        site.manage_addFolder('ext','Externe Methoden')
        ext = getattr(site,'ext')

    methods = (
        ('listDir', 'list directory content', 'DiPP.listDir', 'listDir'),
        ('deadline_date', '', 'DiPP.deadlines', 'deadline_date'),
        ('deadline_delay', '', 'DiPP.deadlines', 'deadline_delay'),
        ('deadline_time', '', 'DiPP.deadlines', 'deadline_time'),
        ('reminder', '', 'DiPP.reminder', 'reminder'),
    )
    for id, title, module, function in methods:
        if not hasattr(ext, id):
            ext.manage_addProduct['ExternalMethod'].manage_addExternalMethod(id, title, module, function)
    
    #if not hasattr(site, 'fedora_tmp'):
    #    site.manage_addFolder('fedora_tmp','Temporäre Fedoraobjekte')
    #if not hasattr(site, 'tmp'):
    #    site.manage_addFolder('tmp','Temporäre Artikel')

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
    types = getattr(props, 'default_page_types')
    typesUseViewActionInListings = getattr(props, 'typesUseViewActionInListings')

    if 'FedoraMultimedia' not in typesUseViewActionInListings:
        newviewtypes = list(typesUseViewActionInListings)
        newviewtypes.append('FedoraMultimedia')
        props._updateProperty('typesUseViewActionInListings',newviewtypes)
           
    if 'FedoraDocument' not in types:
        newtypes = list(types)
        newtypes.append('FedoraDocument')
        props._updateProperty('default_page_types', newtypes)
    
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

    pai = getToolByName(site, 'portal_actionicons')
    
    action_icons = (
        ('plone', 'citation', 'citation_icon.gif', 'Citation and Metadata', 0),
        ('plone', 'fulltextpdf', 'pdf_icon.gif', 'Fulltext PDF', 0),
    )
    for category, action_id, icon_url, title, priority in action_icons:
        try:
            pai.addActionIcon(category, action_id, icon_url, title, priority)
        except:
            print >> out, "Action icon for %s already exists" % action_id
    
        
    # pai.manage_addActionIcon('plone', 'citation', 'citation_icon.gif', 'Citation and Metadata', 0, None)
    # pai.manage_addActionIcon('plone', 'fulltextpdf', 'pdf_icon.png', 'Get Fulltext as PDF', 0, None)


def install_configlet(self,out):
    """register the configlet"""
    portal_conf=getToolByName(self,'portal_controlpanel')
    portal_conf.registerConfiglet( 'dipp_configuration'
           , 'DiPP Configuration'      
           , 'string:${portal_url}/prefs_mailtemplates_form' 
           , ''                 # a condition   
           , 'Manage portal'    # access permission
           , 'Products'         # section to which the configlet should be added: 
                                #(Plone,Products,Members) 
           , 1                  # visibility
           , PROJECTNAME                                        
           , 'dipp_icon.gif'    # icon in control_panel  
           , 'Configuration of the DiPP Publicationsystem'
           , None
                                 )

    
def install_css(self,out):
    """register the stylesheets"""
    registerResources(self, out, 'portal_css', STYLESHEETS)

def install_metadataproperties(self,out):
    """available metadata and default values"""
    
    if not hasattr(self.portal_properties, 'metadata_properties'):
        self.portal_properties.addPropertySheet('metadata_properties', 'QDC Metadata properties')
    
    props = self.portal_properties.metadata_properties
    
    metadata_props= (
        ('journalname', 'string', ''),
        ('journalname_abbr', 'string', ''),
        ('default_language', 'string', DEFAULT_LANGUAGE),
        ('available_languages', 'lines', AVAILABLE_LANGUAGES)
    )
    
    for prop_id, prop_type, prop_value in metadata_props:
        if not hasattr(props, prop_id):
            props.manage_addProperty(id=prop_id, value=prop_value, type=prop_type)

def install_memberproperties(self,out):
    """add some memberproperties"""

    md = self.portal_memberdata
    
    member_props= (
        ('academictitle','string',''),
        ('givenname','string',''),
        ('surname','string',''),
        ('organization','string',''),
        ('postaladdress','string',''),
        ('postalcode','string',''),
        ('phone','string',''),
        ('areas_of_expertise','lines',''),
    )
    
    for prop_id, prop_type, prop_value in member_props:
        if not hasattr(md, prop_id):
            md.manage_addProperty(id = prop_id, value = prop_value, type =  prop_type)

    
    if not hasattr(self.portal_properties, 'member_properties'):
        self.portal_properties.addPropertySheet('member_properties', 'Extended member properties')
    #    print >> out, "added member_properties sheet with additional attributes"
    #else:
    #    print >> out, "found member_properties, leaving it untouched"
        
    props = self.portal_properties.member_properties

    extended_member_props= (
        ('academictitle_visible','boolean',True),
        ('academictitle_required','boolean',False),
        ('givenname_visible','boolean',True),
        ('givenname_required','boolean',True),
        ('surname_visible','boolean',True),
        ('surname_required','boolean',True),
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
        ('mail_password_visible','boolean',True),
        ('areas_of_expertise','lines','')
    )


    for prop_id, prop_type, prop_value in extended_member_props:
        if not hasattr(props, prop_id):
            props.manage_addProperty(id = prop_id, value = prop_value, type =  prop_type)


def install_content(self, out, site_id=SITE_NAME):
    """install some default content"""
    site = getSite(self, site_id)
    if not hasattr(site, DEFAULT_PAGE):
        site.invokeFactory('Document',id=DEFAULT_PAGE,title=WELCOME_TITLE,description=WELCOME_DESCRIPTION,text=WELCOME_TEXT,text_format="html")

def install_dependencies(self,out,site_id=SITE_NAME):
    """Try to install dependencies to other products"""
    
    print >> out, "Dependency %s:" % str(len(DEPENDENCIES))
    site = getSite(self, site_id)
    quickinstaller = site.portal_quickinstaller
    for dependency in DEPENDENCIES:
        print >> out, "Installing dependency %s:" % dependency
        quickinstaller.installProduct(dependency) 
        get_transaction().commit(1)

def create_indexes(self,out,site_id=SITE_NAME):
    """create and reindex custom indexes"""
    
    pcat = getToolByName(self, 'portal_catalog')
    for name, type in INDEXES:
        if name not in pcat.indexes():
            pcat.manage_addIndex(name,type)
            pcat.manage_reindexIndex([name])
            print >> out, "Adding and indexing %s:" % name
        
    
def create_vocabularies(self,out,site_id=SITE_NAME):
    """create required vocabularies"""
    
    site = getSite(self, site_id)
    atvm = site.portal_vocabularies
    for type, name, description, title in VOCABULARIES:
        if not  hasattr(atvm,name):
            atvm.invokeFactory(type, name, title=title, description=description, sortMethod='getObjPositionInParent')
            vocab = atvm.getVocabularyByName(name)
            print >> out, vocab
            key = 'no-section'
            value = 'No section'
            if vocab.id == 'journal-sections' and not hasattr(vocab,key):
                vocab.invokeFactory('SimpleVocabularyTerm',key)
                vocab[key].setTitle(value)
                vocab[key].reindexObject()
            vocab.reindexObject()

            print >> out, "created vocabulary %s" % title
        else:
            print >> out, "vocabulary %s exists" % title

def install_tools(self,out,site_id=SITE_NAME):
    """install tools"""
    
    site = getSite(self, site_id)
    for tool in TOOLS:
        try:
            site.manage_addProduct[PROJECTNAME].manage_addTool(tool)
        except BadRequest:
            # if an instance with the same name already exists this error will
            # be swallowed. Zope raises in an unelegant manner a 'Bad Request' error
            pass
            


def install(self):
    """ install a dipp instance"""
    out = StringIO()
    
    install_dependencies(self,out)
    install_properties(self, out)
    install_memberproperties(self, out)
    install_metadataproperties(self,out)
    install_subskins(self, out)
    install_extMethods(self, out)
    install_types(self, out)
    install_css(self,out)
    install_configlet(self, out)
    install_content(self, out)
    install_tools(self, out)
    create_vocabularies(self, out)
    create_indexes(self, out)
    
    reftool = getToolByName(self, 'portal_openflow')
    process_id = 'Publishing'
    if not hasattr(reftool, process_id):
        configure_workflow(self, out)
    else:
        print >> out, "Keeping existingworkflow"
        

    
    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()

def uninstall(self, site_id=SITE_NAME):
    """
    * Root properties are not removed
    * Member properties are not removed
    """
    out = StringIO()
    site = getSite(self, site_id)
    
    #remove configlet 
    portal_conf=getToolByName(self,'portal_controlpanel')
    portal_conf.unregisterConfiglet('dipp_configuration')


    return out.getvalue()
