## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##


REQUEST = context.REQUEST
PID = REQUEST['PID']

childOf = "dipp:40"

results = container.portal_catalog(portal_type='FedoraHierarchie');

existingPIDs = []

id = "test"
#id = PID.replace(':','_')

for x in results:
    url = x.getURL()
    pid = x[1]
    existingPIDs.append(pid)
    if pid == childOf:
        print x.getObject()
        print x.getURL()
        print x[0]
        x.getObject().invokeFactory('FedoraArticle',id,PID=PID)

return printed

    
