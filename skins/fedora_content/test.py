## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name, value, i
##title=
##


REQUEST = context.REQUEST
try:
    if REQUEST.form.has_key(name):
        return REQUEST.form[name][i]
    else:
        return value
except:
    return None

    
