## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self
##

from zLOG import LOG, INFO

REQUEST = context.REQUEST
RESPONSE =  REQUEST.RESPONSE

file  = REQUEST.form['File_file']

if file.filename.split("\\")  > 1:
    filename = file.filename.split("\\")[-1]
else:
    filename = file.filename

if not REQUEST.form['title']:
    title = filename
else:
    title = REQUEST.form['title']

state.set(filename=filename)
REQUEST.form['title'] = title
return context.content_edit_impl(state, id)
