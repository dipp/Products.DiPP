##script (Python) "upload_cms"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

from Products.CMFCore.utils import getToolByName

request  = context.REQUEST

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
fedora = getToolByName(self, 'fedora')
utils = context.plone_utils

file         = request['file']
JournalPID   = request['journalPID']

tempFiles    = 'fedora'

try:
    tmp = getattr(container,tempFiles)
except:
    raise Exception, "Directory %s does not exist!" % tempFiles

filename = file.filename
normalized = utils.normalizeString(filename)

title = file.filename
tempID = fedora.getTempID(request)

try:
    tmp.manage_addFolder(id=tempID, title=title)
    folder = getattr(tmp, tempID)
    folder.manage_addFile(id=normalized, file=file, title=title)
except:
    raise Exception, "file couldn't be created"

obj=getattr(folder,normalized) 

# make sure tempID is visible and thus reachable for the converter
new_context = context.portal_factory.doCreate(context)

Location = obj.absolute_url()                                                              
if Location.startswith('https'):
    Location = Location.replace('https','http',1)

#context.plone_log
#LOG('DiPP File Location', INFO, Location )

MIMEType = obj.content_type
size     = obj.size

convertible = ('application/rtf', 
    'application/msword', 
    'text/rtf',
    'text/xml')
    
targetFormat = []

if MIMEType in convertible:
    targetFormat.append("html")
else:
    targetFormat.append("")


formButton = request.get('form.button.testconvert', None)

if formButton != None :
    storageType = 'temporary'
else:
    storageType = 'permanent'

state.set(status=storageType,
    journalPID=JournalPID,
    title_value=request['title_value'],
    title_lang=request['title_lang'],
    storageType=storageType,
    targetFormat=targetFormat,
    Location=Location)
    
# Always make sure to return the ControllerState object
return state
