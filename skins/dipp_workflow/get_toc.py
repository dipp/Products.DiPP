## Script (Python) "get_status"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

try:
    toc = getattr(context,'toc_html')
    ids = {'PID':toc.PID,'DsID':toc.DsID}
    return ids
except:
    return "no toc"
