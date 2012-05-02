## Script (Python) "pub_modify_instance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

request     = container.REQUEST
RESPONSE    = request.RESPONSE

keyword = context.keyword
#keyword = context.get('keyword',None)
sort_on = context.sort_on
#sort_on = context.get('sort_on','Date')
sort_order = context.sort_order
#sort_order = context.get('sort_order','ascending')

results = context.portal_catalog.searchResults(
    Subject={'query':keyword},
    sort_on=sort_on, 
    sort_order=sort_order
)

return results
