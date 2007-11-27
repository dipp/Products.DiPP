## Script (Python) "fedoramultimedia_view"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Edit content
##

from Products.CMFCore.utils import getToolByName

REQUEST = context.REQUEST
RESPONSE = REQUEST.RESPONSE
fedora = getToolByName(context, 'fedora')

PID = context.PID
DsID = context.DsID

file =  fedora.accessImage(PID,DsID,None)

if REQUEST.URL.split('/')[-1] == 'fedoramultimedia_view':
    print "<html><head></head><body>"
    print "<img src='../" + context.id  + "' />"
    print "</body></html>"
    return printed
else:
    filename = REQUEST.URL.split('/')[-1]
    ext = filename.split('.')[-1]
    if ext == 'pdf':
        RESPONSE.setHeader('Content-Type', 'application/pdf')
        return file
    if ext in ('jpg','jpeg'):
        RESPONSE.setHeader('Content-Type', 'image/jpg')
        return file
    if ext == 'gif':
        RESPONSE.setHeader('Content-Type', 'image/gif')
        return file
    if ext == 'png':
        RESPONSE.setHeader('Content-Type', 'image/png')
        return file
    if ext == 'wmv':
        return file
    if ext == 'rtf':
        RESPONSE.setHeader('Content-Type', 'application/rtf')
        return file
    else:
        return file

