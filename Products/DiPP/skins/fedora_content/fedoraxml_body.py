##script (Python) "fedoraxml_body"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

request  = container.REQUEST
response = request.RESPONSE

response.headers['Content-type'] = 'text/html; charset="utf-8'
return self.body
