import logging
from Products.CMFCore.utils import getToolByName

logger = logging.getLogger("DiPP")

def createFedoraDatastream(obj, event):
    """ when a document is not converted but added manually via the "add article"
        menu, it does not have PID and DsID. This method takes care of creating a
        a digital object for the page.
    """

    fedora = getToolByName(obj, 'fedora')
    article = obj.getParentNode()
    PID = fedora.getContentModel(PID=article.PID, Type='HTML')
    logger.info("article %s, content %s" % (article.PID, PID) )
    
    MIMEType = "text/html"
    Label = obj.id
    Location = article.absolute_url() + "/dummy.html"
    if Location.startswith('https'):
        Location = Location.replace('https','http',1)
    
    try:
        DsID = obj.DsID
    except AttributeError:
        DsID = False

        
    if not DsID:
        DsID = fedora.addDatastream(None,PID,Label,MIMEType,Location,"M","","","A")
        logger.info("id %s: new DsID %s, PID %s" % (obj.id, DsID, PID) )
        obj.setPID(PID)
        obj.setDsID(DsID)

    obj.reindexObject()

def createFedoraContainer(obj, event):
    """add a hierarchical object to fedora and write the PID back to the Plone object
    """

    fedora = getToolByName(obj, 'fedora')
    portal = getToolByName(obj, 'portal_url').getPortalObject()
    parent = obj.getParentNode()
    if parent == portal:
        isChildOf = fedora.PID
    else:
        isChildOf = parent.PID
    #MetaType = obj.MetaType
    MetaType = "volume"
    #title = obj.title
    title = "Vol Titel"
    id = obj.id
    AbsoluteURL = obj.absolute_url()
    
    if not obj.PID:
        PID = fedora.createNewContainer(isChildOf, MetaType, title, id, AbsoluteURL)
        msg = "PID %s, isChildOf %s, MetaType %s, title %s, id %s, AbsoluteURL %s" % (PID, isChildOf, MetaType, title, id, AbsoluteURL)
        logger.info(msg)
        obj.setPID(PID)
    obj.reindexObject()

