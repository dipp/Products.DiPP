## Script (Python) "uploadFile"
##title=Upload Article
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

# -*- coding: utf-8 -*-
#from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE =  request.RESPONSE


file         = request['file']

tempFiles    = 'fedora_tmp'
try:
    tmp = getattr(container,tempFiles)
except:
    raise Exception, "Directory 'fedora_tmp' does not exist!"


filename = file.filename

title = file.filename
extension = title.split('.')[-1]
tempID = context.getTempID(request) + '.' + extension
tmp.invokeFactory(id=tempID,type_name='File',file=file,title=title)
obj=getattr(tmp,tempID) 

#make sure tempID is visible and thus reachable for the converter
new_context = context.portal_factory.doCreate(context)
try:
    obj=getattr(tmp,tempID)
    portal_workflow=obj.portal_workflow
    wfcontext = context
    #wfcontext = new_context.portal_workflow .doActionFor(obj,'show',comment='Make visible for conversion' )
except:
    raise Exception, "Status couldn't be changed to visible"

Location = obj.absolute_url()                                                                
MIMEType = obj.content_type
size     = obj.size

request.set('params',request.form)
return state


    
