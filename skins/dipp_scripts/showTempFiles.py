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

tempFiles  = 'tmp'

try:
    tmp = getattr(container,tempFiles)
except:
    raise Exception, "Directory 'fedora_tmp' does not exist!"

list = []
for x in tmp.contentValues('FedoraArticle'):
    if x.PID.split(':')[0] == "temp":
        list.append({'PID':x.PID,'url':x.absolute_url(),'date':x.ModificationDate(),'title':x.title})


return list
