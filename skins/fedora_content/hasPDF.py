##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

PDF = False
folder = context.getParentNode()
ids= folder.objectIds()
for id in ids:
    ext = id.split('.')[-1]
    if ext == 'pdf' and id != 'pdf':
        PDF = id

return PDF
