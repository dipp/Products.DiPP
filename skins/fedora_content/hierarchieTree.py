## Script (Python) "simple_tree"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Standard Tree
##
REQUEST = context.REQUEST

results = container.portal_catalog(portal_type='FedoraHierarchie',sort_on='Date', sort_order="reverse");

existingPIDs = []


for x in results:
    url = x.getURL()
    pid = x.getObject().PID
    tmp = x.getObject().tmp
    if not tmp:
        existingPIDs.append({'PID':pid,'URL':url})

return existingPIDs
#return printed
