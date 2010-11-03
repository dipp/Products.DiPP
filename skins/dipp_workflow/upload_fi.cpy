##script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

from Products.CMFCore.utils import getToolByName
from zLOG import LOG, INFO

request  = context.REQUEST

fedora = getToolByName(self, 'fedora')

file         = request['file']
JournalPID   = request['journalPID']

tempFiles    = 'fedora_tmp'
try:
    tmp = getattr(container,tempFiles)
except:
    raise Exception, "Directory %s  does not exist!" % tempFiles

filename = file.filename

title = file.filename
tempID = fedora.getTempID(request)
try:
    tmp.manage_addFolder(id=tempID, title=tempID)
    folder = getattr(tmp, tempID)
    folder.manage_addFile(id=filename, file=file, title=title)
except:
    raise Exception, "file couldn't be created"

obj=getattr(folder,filename) 

# make sure tempID is visible and thus reachable for the converter
new_context = context.portal_factory.doCreate(context)

Location = obj.absolute_url()                                                              
if Location.startswith('https'):
    Location = Location.replace('https','http',1)

LOG('DiPP File Location', INFO, Location )

MIMEType = obj.content_type
size     = obj.size

convertible = ('application/rtf', 
    'application/msword', 
    'application/octet-stream',
    'text/rtf',
    'text/xml')
    
targetFormat = ['']

if MIMEType in  convertible:
    targetFormat.append("html")

formButton = request.get('form.button.testconvert', None)
if formButton != None :
    storageType = 'temporary'
else:
    storageType = 'permanent'

#state.set(form.submitted='1')

state.set(status=storageType,
    bc_journalTitle=request['bc_journalTitle'],
    journalPID=JournalPID,
    title_value=request['title_value'],
    title_lang=request['title_lang'],
    storageType=storageType,
    targetFormat=targetFormat,
    Location=Location)

# Always make sure to return the ControllerState object
return state
