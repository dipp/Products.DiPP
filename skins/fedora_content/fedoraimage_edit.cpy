## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

#RESPONSE    = request.RESPONSE
from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST
portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()

PID   = REQUEST.form['PID']
DsID  = REQUEST.form['DsID']
Image = REQUEST.form['Image']

def upload():
    try:
        tempDir = getattr(portal,'fedora_tmp')
    except:
        portal.invokeFactory('Folder','fedora_tmp')
        tempDir = getattr(portal,'fedora_tmp')

    title = Image.filename                                                                           
    tempID = context.getTempID(REQUEST)
    newId = tempDir.invokeFactory(id=tempID,type_name='File',file=Image,title=title)
    obj=getattr(tempDir,tempID) 

    Label    = obj.title
    MIMEType = obj.content_type
    Location = obj.absolute_url()
    size     = obj.size
    return {'Location': Location, 'MIMEType':MIMEType, 'Label':Label}


if DsID == '':
    ds = upload()
    Location = ds['Location']
    MIMEType = ds['MIMEType']
    Label    = ds['Label']
#    REQUEST.form['DsID'] = context.fedoraAddDatastream(self,REQUEST,PID,Label,MIMEType,Location,"M","","","A")
    REQUEST.form['DsID'] = "DS1"
#    REQUEST.form['DsID'] = Location



new_context = context.portal_factory.doCreate(context, id)
new_context.processForm()


portal_status_message = REQUEST.get('portal_status_message', 'Änderungen an der Arbeitsversion wurden gespeichert!.')

return state.set(status='success',\
                 context=new_context,\
                 portal_status_message=portal_status_message)
