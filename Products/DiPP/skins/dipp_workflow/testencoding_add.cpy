##script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

REQUEST = context.REQUEST


if REQUEST.form.has_key('form.button.Save'):
    title = REQUEST.get('title', None).encode("utf-8")
    context.plone_log('Title input: ' + title)
    
    portal_status_message = REQUEST.get('portal_status_message', 'title ' + title)


return state.set(status='success',\
    portal_status_message=portal_status_message,\
    title			           = REQUEST.get('title',None)
)
