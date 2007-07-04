## Script (Python) "setPath"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Pfad zum temporären repository
##
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE
try:
	path = request.pfad
except:
	path = container.portal_properties.repository
return path
