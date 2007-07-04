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

PID     = context.REQUEST.get('PID', None)

"""
# check for PID in fedora
if context.fedoraSearch('PID','has',PID) == 'FALSE' :
    state.setError('PID', 'PID does not exist in Fedora database', new_status='failure')


# check for PID in plone
results = container.portal_catalog(portal_type='FedoraHierarchie');

existingPIDs = []

for x in results:
    url = x.getURL()
    pid = x[1]
    existingPIDs.append(pid)


if PID in existingPIDs:
    msg  = "There exists already on Object with this PID at"
          
    state.setError('PID',msg , new_status='failure')

"""

if state.getErrors():
    state.set(portal_status_message='Bitte die angezeigten Fehler korrigieren!')
     
return state


