## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id=''

REQUEST = context.REQUEST

PID  = REQUEST.form['PID']

new_context = context.portal_factory.doCreate(context, id)
new_context.processForm()


portal_status_message = REQUEST.get('portal_status_message', 'Änderungen an der Arbeitsversion wurden gespeichert!.')

return state.set(status='success',\
                 context=new_context,\
                 portal_status_message=portal_status_message)
