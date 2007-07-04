## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self


from Products.CMFCore.utils import getToolByName
REQUEST = context.REQUEST

urltool = getToolByName(context, "portal_url")
fedora = getToolByName(self, 'fedora')
portal = urltool.getPortalObject()

PID = REQUEST.form['PID']
id = REQUEST.form['id']
title  = REQUEST.form['title']
isChildOf  = REQUEST.form['isChildOf']
parentURL = REQUEST.form['parentURL']
MetaType  = REQUEST.form['MetaType']

if PID == '':
    description = "Eine Fedora Hierarchie"
    text = "Dies ist die Startseite der neu angelegten FedoraHierarchie. Unter 'Bearbeiten' können Sie den Inhalt dieser Seite anpassen."
    self.invokeFactory('Document',id='index_html',title=title,description=description,text=text,text_format="html")
    self.manage_addProperty(id="tmp", value=False, type='boolean')
    AbsoluteURL = parentURL + "/" + id
    #PID = fedora.createNewContainer(isChildOf, MetaType, title, id, parentURL + '/' + id)
    PID = fedora.createNewContainer(isChildOf, MetaType, title, id, AbsoluteURL)
    REQUEST.form['PID'] = PID

new_context = context.portal_factory.doCreate(context, id)
new_context.processForm()


portal_status_message = REQUEST.get('portal_status_message', 'Hierarchie wurde geändert')

return state.set(status='success',\
                 context=new_context,\
                 portal_status_message=portal_status_message)
