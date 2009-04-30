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
    
    qdc = fedora.getQualifiedDCMetadata(document.PID)
    
    if aLabel == 'index_html':
        id = 'fulltext'
        title = qdc['title'][0]['value']
        document.manage_addProperty(id='default_page', value=id, type='string')
    elif aLabel == 'toc_html':
        title = 'Table of Contents' 
    else:
        title = aLabel
    
    if  id[-3:].lower() == 'xml':
        objType = 'FedoraXML'
    
    stream = fedora.access(PID=PID,DsID=DsID,Date=None)['stream']
    MIMEType = fedora.access(PID=PID,DsID=DsID,Date=None)['MIMEType']
    if objType in ('FedoraDocument','FedoraXML'):
        contentObj = document.invokeFactory(objType,id=id,title=title,PID=PID,DsID=DsID,body=stream,format=MIMEType)
    else:
        contentObj = document.invokeFactory(objType,id=id,title=title,PID=PID,DsID=DsID)
        
    contentDocument = getattr(document, id)
except:
    raise Exception, "could not create Content Object"

return contentDocument.absolute_url()
