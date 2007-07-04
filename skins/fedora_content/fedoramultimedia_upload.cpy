## Controller Python Script "fedoramultimedia_upload"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Edit content
##
## Warnings:
##  Prints, but never reads 'printed' variable.
##
#RESPONSE    = request.RESPONSE
from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE

portal_url = getToolByName(self, 'portal_url')
fedora = getToolByName(self, 'fedora')
portal = portal_url.getPortalObject()

articlePID   = REQUEST.form['articlePID']
file  = REQUEST.form['file']

HTML_PID       = fedora.getContentModel(PID=articlePID,Type='HTML')
MULTIMEDIA_PID = fedora.getContentModel(PID=articlePID,Type='Multimedia')
NATIVE_PID     = fedora.getContentModel(PID=articlePID,Type='Native')
OTHER_PID      = fedora.getContentModel(PID=articlePID,Type='Other')
PDF_PID        = fedora.getContentModel(PID=articlePID,Type='PDF')
XML_PID        = fedora.getContentModel(PID=articlePID,Type='XML')
#PDF_PID = 'sd'
map = {
    'jpg': MULTIMEDIA_PID,
    'png': MULTIMEDIA_PID,
    'gif': MULTIMEDIA_PID,
    'pdf': PDF_PID,
    'xml': XML_PID
}

print 'pdf',PDF_PID
print 'xml',XML_PID
print 'mm',MULTIMEDIA_PID

title= file.filename

EXTENSION = title.split('.')[-1]
print EXTENSION
try:
    PID = map[EXTENSION]
except:
    PID = OTHER_PID


print 'PID',PID

try:
    tempDir = getattr(portal,'fedora_tmp')
except:
    portal.invokeFactory('Folder','fedora_tmp')
    tempDir = getattr(portal,'fedora_tmp')

tempID = fedora.getTempID(REQUEST)
newId  = tempDir.invokeFactory(id=tempID,type_name='File',file=file,title=title)
obj=getattr(tempDir,tempID) 

Label    = obj.title
MIMEType = obj.content_type
Location = obj.absolute_url()
size     = obj.size

url  = 'fedoramultimedia_add'
url += '?PID=' + PID
url += '&Label=' + Label
url += '&Location=' + Location
url += '&MIMEType=' + MIMEType


RESPONSE.redirect(url)
#print url
#return printed

