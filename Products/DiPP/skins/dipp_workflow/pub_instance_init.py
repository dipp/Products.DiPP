## Script (Python) "pub_instance_init"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=instance_id, workitem_id
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE
oftool = container.portal_openflow
workitem = getattr(getattr(oftool,instance_id),workitem_id)
user_name = container.REQUEST.AUTHENTICATED_USER.getUserName()

if workitem.status=='inactive' and (workitem.actor=='' or workitem.actor==user_name):
    oftool.activateWorkitem(instance_id,workitem_id,user_name)
elif workitem.status=='active' and workitem.actor==user_name:
    pass
else:
    return 0

return 1
