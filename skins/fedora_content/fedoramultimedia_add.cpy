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
#RESPONSE    = request.RESPONSE
from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE
portal_url = getToolByName(self, 'portal_url')
fedora = getToolByName(self, 'fedora')
portal = portal_url.getPortalObject()


PID      = REQUEST.form['PID']
Label    = REQUEST.form['Label']
MIMEType = REQUEST.form['MIMEType']
Location = REQUEST.form['Location']

id = Label
title=Label

DsID = fedora.addDatastream(REQUEST,PID,Label,MIMEType,Location,"M","","","A")
context.invokeFactory('FedoraMultimedia',id=id,title=title,PID=PID,DsID=DsID)

backto= context.absolute_url() + "/folder_contents"
#print PID
#print DsID
#print backto
#return printed

RESPONSE.redirect(backto)
"""
new_context = context.portal_factory.doCreate(context, id)
new_context.processForm()
portal_status_message = REQUEST.get('portal_status_message', 'Änderungen an der Arbeitsversion wurden gespeichert!.')
return state.set(status='success',\
                 context=new_context,\
                 portal_status_message=portal_status_message)
"""

