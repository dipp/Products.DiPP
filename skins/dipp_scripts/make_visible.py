## Script (Python) "uploadFile"
##title=Upload Article
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# -*- coding: utf-8 -*-
request  = container.REQUEST
RESPONSE =  request.RESPONSE

new_context = context.portal_factory.doCreate(context)
tempFiles  = 'fedora_tmp'
tempID     = 'dippadm1112707883.44.rtf'

try:
    tmp = getattr(container,tempFiles)
except:
    raise Exception, "Directory 'fedora_tmp' does not exist!"

obj=getattr(tmp,tempID)
portal_workflow=obj.portal_workflow
wfcontext = context

wfcontext = new_context.portal_workflow.doActionFor( obj,'show',comment='Make visible for conversion' )
Location  = obj.absolute_url()

print Location
return printed
