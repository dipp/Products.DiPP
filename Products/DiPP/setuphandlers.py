import logging
from Products.CMFCore.utils import getToolByName

def add_catalog_indexes(context, logger=None):
    logger.info("Test setuphandler")

def import_various(context):
    """Import step for configuration that is not handled in xml files.
    """
    # Only run step if a flag file is present
    #if context.readDataFile('your_package-default.txt') is None:
    #    return
    logger = context.getLogger('your.package')
    site = context.getSite()
    add_catalog_indexes(site, logger)
