## Script (Python) "fedoradocument_newversion"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST

translate = context.translate
articlePID = context.getParentNode().PID

fedora = getToolByName(self, 'fedora')
PID  = REQUEST.form['PID']
DsID = REQUEST.form['DsID']
MIMEType = REQUEST.form['MIMEType']
LogMessage = REQUEST.form['LogMessage']
Label = REQUEST.form['Label']
Location =  context.absolute_url() + "/getPrivateContent"
if Location.startswith('https'):
    Location = Location.replace('https','http',1)
DsState = "A"
tempID = ""

fedora.modifyDatastreamByReference(REQUEST,PID,DsID,Label,LogMessage,Location,DsState,MIMEType,tempID)
fedora.setModified(articlePID)

msg = "Neue Version in Fedora gespeichert! Es ist evtl. ein Reload nötig, um die neue Version in der Übersicht anzuzeigen!"
# msg = translate('new-datastream-version', domain='dipp')
context.plone_utils.addPortalMessage(msg)
return state.set(status='success')
