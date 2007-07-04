## Script (Python) "fedoramultimedia_view"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Edit content
##
#RESPONSE    = request.RESPONSE
REQUEST = context.REQUEST
RESPONSE    = REQUEST.RESPONSE

PID = context.PID
DsID = context.DsID
url  = "http://themis:9080/fedora/get/"
url += PID
url += "/fedora-system:3/getItem?itemID="
url += DsID

file =  context.fedoraAccessImage(PID,DsID,None)
#return bild

if REQUEST.URL.split('/')[-1] == 'fedoramultimedia_view':
#    return REQUEST.URL.split('/')[-1]
    print "<html><head></head><body>"
    print "<img src='../" + context.id  + "' />"
    print "</body></html>"
    return printed
else:
    filename = REQUEST.URL.split('/')[-1]
    ext = filename.split('.')[-1]
    if ext == 'pdf':
        #RESPONSE.redirect(url)
        RESPONSE.setHeader('Content-Type', 'application/pdf')
        return file
    if ext == 'jpg':
        #RESPONSE.redirect(url)
        RESPONSE.setHeader('Content-Type', 'image/jpg')
        return file
    else:
        return file

