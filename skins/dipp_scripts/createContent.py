##Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, aObject_type, aParent_id, aPid, aDsid, aLabel
##title=
##

from Products.PythonScripts.standard import html_quote
from Products.CMFCore.utils import getToolByName

"""
  code from checkForNewPIDs-Script
"""
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
fedora = getToolByName(self, 'fedora')

try:
   tempDir = getattr(portal,'tmp')
except:
    raise Exception, "the requested tempFolder does not exist"

try:
    document = getattr(tempDir, aParent_id)
except:
    raise Exception, "the requested Document does not exist"

try:
    id = aLabel
    PID = aPid
    DsID = aDsid
    objType = aObject_type
    #state = 'hide'
    
    if aLabel == 'index_html':
        qdc = fedora.getQualifiedDCMetadata(document.PID)
        title = qdc['title'][0]['value']
    elif aLabel == 'toc_html':
        title = 'Table of Contents' 
    else:
        title = aLabel
    
    if objType == 'FedoraDocument':
        contentObj = document.invokeFactory(objType,id=id,title=title,PID=PID,DsID=DsID,body=fedora.access(PID=PID,DsID=DsID,Date=None)['stream'])
    else:
        contentObj = document.invokeFactory(objType,id=id,title=title,PID=PID,DsID=DsID)
    contentDocument = getattr(document, id)
    #contentDocument.portal_workflow.doActionFor(contentDocument, state, comment='')
except:
    raise Exception, "could not create Content Object"

return contentDocument.absolute_url()
