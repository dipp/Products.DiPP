##Script (Python) "createWorkflowInstance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, aPID, aIsChildOf, aIsParentOf, aCModel, aCreator, aTitle, aSubject, aRights
##title=
##

from Products.PythonScripts.standard import html_quote
from Products.CMFCore.utils import getToolByName

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
utils = context.plone_utils

def newArticle(id,title,PID,subject,rights):
    """create a new Article container in a temporary folder """
    
    try:
       tempDir = getattr(portal,'tmp')
    except:
        raise Exception, "the requested tempFolder does not exist"
    
    try:
        tempDir.invokeFactory('FedoraArticle',id=id,title=title,PID=PID)
        document = getattr(tempDir, id)
        document.manage_addProperty(id="tmp", value=True, type='boolean')
        document.syncMetadata()
    except:
        raise Exception, "could not create Article Object"
        
    return document.absolute_url()

def newInstance(PID,creator,title,cModel,isChildOf,isParentOf):
    """Create a new workflow instance and initialize it with the needed values"""
    
    id = aPID.split(":")[-1]
    autorOK = False    
    gastHrsgOK = False    
    formalOK = False  

    dl = self.portal_properties.deadline_no
    comment = "New digital object found in Fedora!"
    instance_id = oftool.addInstance(process_id='Publishing',
                                     customer='auto',
                                     comments='added new instance',
                                     priority='3',
                                     title=id,
                                     activation=0)
    instance = oftool[instance_id]

    wi_props = ( 
        ('PID', PID, 'string'),
        ('isChildOf', isChildOf, 'lines'),
        ('isParentOf', isParentOf, 'lines'),
        ('type', cModel, 'string'),
        ('url', '', 'string'),
        ('autor', creator, 'string'),
        ('gastHrsg', '', 'string'),
        ('hierarchie', 'n/a', 'string'),
        ('autorOK', autorOK, 'boolean'),
        ('gastHrsgOK', gastHrsgOK, 'boolean'),
        ('formalOK', formalOK, 'boolean'),
        ('nachrichten', comment, 'text'),
        ('deadline', dl, 'date'),
        ('deadline_next', dl, 'date'),
        ('alert', 'green', 'string')
    )
    
    for prop_id, prop_value, prop_type in wi_props:
        if not instance.hasProperty(prop_id):
            try:
                instance.manage_addProperty(id=prop_id, value=prop_value, type=prop_type)
            except UnicodeEncodeError:
                normalized = utils.normalizeString(prop_value)
                instance.manage_addProperty(id=prop_id, value=normalized, type=prop_type)
                msg = "could not add %s, added normalized version '%s'" % (prop_value, normalized)
                self.plone_log(msg)
    
    oftool.startInstance(instance_id=instance_id)
    return instance_id

# workflow items are only created for permanent stored articles 

if aPID.split(':')[0] != 'temp':
    id = newInstance(aPID,aCreator,aTitle,aCModel,aIsChildOf,aIsParentOf) 
    url = newArticle(id,aTitle,aPID,aSubject,aRights)
    instance,workitem = oftool.getInstanceAndWorkitem(id,'0')
    instance.manage_changeProperties({'url':url})
else:
    id = aPID.replace(':','_')
    url = newArticle(id,aTitle,aPID,aSubject,aRights)

return id
