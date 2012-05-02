## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST


fedora = getToolByName(self, 'fedora')
PID  = REQUEST.form['PID']
DsID = REQUEST.form['DsID']
MIMEType = REQUEST.form['MIMEType']
LogMessage = REQUEST.form['LogMessage']
Label = REQUEST.form['Label']
#Location =  context.absolute_url() + "/fedoradocument_body"
Location =  context.absolute_url()
DsState = "A"
tempID = ""

x = fedora.modifyDatastreamByReference(REQUEST,PID,DsID,Label,LogMessage,Location,DsState,MIMEType,tempID)

portal_status_message = REQUEST.get('portal_status_message', 'Neue Version in Fedora gespeichert! Es ist evtl. ein Reload nötig, um die neue Version in der Übersicht anzuzeigen!')
#portal_status_message = REQUEST.get('portal_status_message', x)


return state.set(status='success',\
                 portal_status_message=portal_status_message)
