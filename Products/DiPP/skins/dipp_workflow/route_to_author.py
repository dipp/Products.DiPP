## Script (Python) "route_to_author"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=instance_id,workitem_id,process_id,activity_id
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE
oftool = container.portal_openflow
instance, workitem = oftool.getInstanceAndWorkitem(instance_id, workitem_id)

actor = workitem.autor

return actor
