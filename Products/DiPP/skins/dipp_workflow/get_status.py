## Script (Python) "get_status"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=instance_id
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE
oftool = container.portal_openflow
instance = getattr(oftool,instance_id)
return instance
