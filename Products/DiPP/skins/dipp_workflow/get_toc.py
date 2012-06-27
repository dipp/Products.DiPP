## Script (Python) "get_toc"
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

# if an article contains a Table of content in toc_html
# return its PID/DsID, otherwise False

try:
    toc = getattr(context,'toc_html')
    ids = {'PID':toc.PID,'DsID':toc.DsID}
    return ids
except:
    return False
