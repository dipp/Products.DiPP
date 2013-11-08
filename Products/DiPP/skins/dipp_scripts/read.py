## Script (Python) "read"
## taken from kupu resolveuid (thx ...)
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retrieve an object using its PID
##

from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.standard import html_quote

request = context.REQUEST
response = request.RESPONSE

PID = traverse_subpath.pop(0)
results = container.portal_catalog(portal_type='FedoraArticle', getPID="dipp:%s"%PID)

if len(results) == 0:
    return context.standard_error_message(error_type=404,
     error_message="No article found with PID dipp:%s" % PID)

if len(results) > 1:
    return context.standard_error_message(error_type=404,
     error_message="Found %s articles with the same PID. This should not happen!" % len(results))

if len(results) == 1:
    target = results[0].getURL()

if request.QUERY_STRING:
    target += '?' + request.QUERY_STRING

return response.redirect(target, status=301)

