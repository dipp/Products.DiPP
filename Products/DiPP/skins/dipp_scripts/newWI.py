##Script (Python) "createWorkflowInstance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, PID
##title=
##

from Products.PythonScripts.standard import html_quote
from Products.CMFCore.utils import getToolByName

oftool = container.portal_openflow
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
utils = context.plone_utils

"""
This script is called via XMLRPC de.nrw.dipp.dippCore.task.TaskPloneRegister
"""

def newInstance(PID,creator,title,cModel,isChildOf,isParentOf):
    """Create a new workflow instance and initialize it with the needed values"""
    
    id = PID
    autorOK = False    
    gastHrsgOK = False    
    formalOK = False  

    dl = self.portal_properties.dipp_properties.deadline_no
    comment = "Händisch erstellte Workflowinstanz"
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
        ('autor', '', 'string'),
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


title = 'Dummy Title'
id = newInstance(PID,'dummy-creator',title,"DiPP:article","dipp:dummy","dipp:parent") 
instance,workitem = oftool.getInstanceAndWorkitem(id,'0')

try:
   tempDir = getattr(portal,'tmp')
except:
    raise Exception, "the requested tempFolder does not exist"

tempDir.invokeFactory('FedoraArticle',id=id,title=title,PID=PID)
document = getattr(tempDir, id)
document.manage_addProperty(id="tmp", value=True, type='boolean')
#document.syncMetadata()
    
return document.absolute_url()
    