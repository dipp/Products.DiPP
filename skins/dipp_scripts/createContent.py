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
default_article_view = portal.portal_properties.dipp_properties.default_article_view

try:
   tempDir = getattr(portal,'tmp')
except:
    raise Exception, "the requested tempFolder does not exist"

try:
    article = getattr(tempDir, aParent_id)
except:
    raise Exception, "the requested article does not exist"

id = aLabel
PID = aPid
DsID = aDsid
objType = aObject_type

qdc = fedora.getQualifiedDCMetadata(article.PID)

if aLabel == 'index_html':
    id = 'fulltext'
    title = qdc['title'][0]['value']
    if default_article_view != "":
        article.manage_addProperty(id='layout', value=default_article_view, type='string')
    else:
        article.manage_addProperty(id='default_page', value=id, type='string')
elif aLabel == 'toc_html':
    title = 'Table of Contents' 
else:
    title = aLabel

if  id[-3:].lower() == 'xml':
    objType = 'FedoraXML'

# fetch the object from fedora without using the webservice
fobject = fedora.accessByFedoraURL(PID=PID,DsID=DsID,Date=None)
stream = fobject['stream']
MIMEType = fobject['MIMEType']

if objType in ('FedoraDocument','FedoraXML'):
    contentObj = article.invokeFactory(objType,id=id,title=title,PID=PID,DsID=DsID,body=stream,format=MIMEType)
else:
    contentObj = article.invokeFactory(objType,id=id,title=title,PID=PID,DsID=DsID)
    
contentDocument = getattr(article, id)

return contentDocument.absolute_url()
