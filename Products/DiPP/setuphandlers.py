import logging
from Products.CMFCore.utils import getToolByName
from Products.DiPP import HAS_PLONE30
from Products.DiPP.config import INDEXES as NEW_INDEXES
PROFILE_ID = 'profile-DiPP:install'

def add_catalog_indexes(context, logger=None):
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger('DiPP')

    # Run the catalog.xml step as that may have defined new metadata
    # columns.  We could instead add <depends name="catalog"/> to
    # the registration of our import step in zcml, but doing it in
    # code makes this method usable as upgrade step as well.  Note that
    # this silently does nothing when there is no catalog.xml, so it                                                                                  
    # is quite safe.
    setup = getToolByName(context, 'portal_setup')
    if HAS_PLONE30:
        setup.runImportStepFromProfile(PROFILE_ID, 'catalog')
    else:
        setup.setImportContext(PROFILE_ID)
        setup.runImportStep('catalog')
        setup.setImportContext('profile-CMFPlone:plone')

    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()
    
    indexables = []
    for name, meta_type in NEW_INDEXES:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)

def add_RolesToPlugIn(context, logger=None):
    """
    From Products/CMFPlone/setuphandlers.py 
    XXX This is horrible.. need to switch PlonePAS to a GenericSetup
    based install so this doesn't need to happen.

    Have to manually register the roles from the 'rolemap' step
    with the roles plug-in.
    """
    uf = getToolByName(context, 'acl_users')
    rmanager = uf.portal_role_manager
    roles = ('Autor', 'Gastherausgeber', 'Herausgeber', 'Redakteur', 'Peer')
    existing = rmanager.listRoleIds()
    for role in roles:
        if role not in existing:
            rmanager.addRole(role)
            logger.info("Added role %s.", role)
        else:
            logger.info("Role %s exists. Skipping step.", role)
 

def import_various(context):
    """Import step for configuration that is not handled in xml files.
    """
    # Only run step if a flag file is present
    if context.readDataFile('is_dipp.txt') is None:
        return
    logger = context.getLogger('DiPP')
    site = context.getSite()
    add_catalog_indexes(site, logger)
    add_RolesToPlugIn(site, logger)
