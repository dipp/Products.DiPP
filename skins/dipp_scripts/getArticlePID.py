## Script (Python) "pub_modify_instance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

request     = container.REQUEST
RESPONSE    = request.RESPONSE

return self.id
