##script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

from Products.CMFCore.utils import getToolByName

request  = context.REQUEST

fedora = getToolByName(self, 'fedora')

file         = request['file']
JournalPID   = request['journalPID']

tempFiles    = 'fedora_tmp'
try:
    tmp = getattr(container,tempFiles)
except:
    raise Exception, "Directory 'fedora_tmp' does not exist!"

filename = file.filename

title = file.filename
extension = title.split('.')[-1]
tempID = fedora.getTempID(request) + '.' + extension
try:
    #tmp.invokeFactory(id=tempID,type_name='File',file=file,title=title)
    tmp.manage_addFile(id=tempID, file=file, title=title)
except:
    raise Exception, "file couldn't created"
obj=getattr(tmp,tempID) 

#make sure tempID is visible and thus reachable for the converter
new_context = context.portal_factory.doCreate(context)

Location = obj.absolute_url()                                                                
MIMEType = obj.content_type
size     = obj.size

targetFormat = ['']
if MIMEType == 'application/rtf' or MIMEType == 'application/msword' or MIMEType == 'application/octet-stream' or MIMEType == 'text/rtf' or MIMEType == 'text/xml':
    targetFormat.append("html")

formButton = request.get('form.button.testconvert', None)
if formButton != None :
    storageType = 'temporary'
else:
    storageType = 'permanent'

#state.set(form.submitted='1')
state.set(status=storageType)
state.set(bc_journalTitle=request['bc_journalTitle'])
state.set(journalPID=JournalPID)
state.set(title_value=request['title_value'])
state.set(title_lang=request['title_lang'])
state.set(storageType=storageType)
state.set(targetFormat=targetFormat)
state.set(Location=Location)
# Always make sure to return the ControllerState object
return state
