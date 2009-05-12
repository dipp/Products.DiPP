## Controller Python Script "fedoramultimedia_add"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##title=Edit content
##
from Products.CMFCore.utils import getToolByName
from zLOG import LOG, INFO

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
portal_url = getToolByName(self, 'portal_url')
fedora = getToolByName(self, 'fedora')
portal = portal_url.getPortalObject()

articlePID = self.getParentNode().PID
args = state.getKwargs()
filename = getattr(self.File, 'filename', None)
MIMEType = self.File.get_content_type()

EXTENSION = MIMEType.split("/")[-1].lower() 

HTML_PID       = fedora.getContentModel(PID=articlePID,Type='HTML')
MULTIMEDIA_PID = fedora.getContentModel(PID=articlePID,Type='Multimedia')
NATIVE_PID     = fedora.getContentModel(PID=articlePID,Type='Native')
OTHER_PID      = fedora.getContentModel(PID=articlePID,Type='Other')
PDF_PID        = fedora.getContentModel(PID=articlePID,Type='PDF')
XML_PID        = fedora.getContentModel(PID=articlePID,Type='XML')

map = {
    'jpg': MULTIMEDIA_PID,
    'jpeg': MULTIMEDIA_PID,
    'png': MULTIMEDIA_PID,
    'gif': MULTIMEDIA_PID,
    'pdf': PDF_PID,
    'xml': XML_PID
}

PID = self.PID
DsID = self.DsID
LOG('DiPP', INFO, "fedoramultimedia_add: %s/%s" % (PID, DsID))

try:
    PID = map[EXTENSION]
except:
    PID = OTHER_PID

Location = self.absolute_url() + "/File"
Label = filename

if DsID == "":
    DsID = fedora.addDatastream(REQUEST,PID,Label,MIMEType,Location,"M","","","A")
    portal_status_message = "Saved new datastream."
else:
    LogMessage = "New Version"
    tempID = ""
    DsState = "A"
    fedora.modifyDatastreamByReference(REQUEST,PID,DsID,Label,LogMessage,Location,DsState,MIMEType,tempID)
    portal_status_message = "Saved new version."

LOG('DiPP', INFO, "fedoramultimedia_add: %s/%s at %s" % (PID, DsID, Location))

self.setId(Label)
self.setPID(PID)
self.setDsID(DsID)

return state.set(Location='Location',\
                 PID='PID',\
                 DsID='DsId',\
                 Label='Label',\
                 status='success',\
                 portal_status_message=portal_status_message)
