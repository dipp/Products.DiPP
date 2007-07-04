## Script (Python) "content_edit"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self

#RESPONSE    = request.RESPONSE
REQUEST = context.REQUEST

PID   = REQUEST.form['PID']
DsID  = REQUEST.form['DsID']
body  = REQUEST.form['body'].decode('utf-8')
id    = REQUEST.form['id']
params = REQUEST.form
articlePID = self.getParentNode().PID
cPID = context.fedoraContent(PID=articlePID,Type='HTML')

#tempFiles    = 'fedora_tmp'
#try:
#    tmp = getattr(container,tempFiles)
#except:
#    raise Exception, "Directory 'fedora_tmp' does not exist!"



#if DsID == '' and PID == '':
#    PID = cPID
#    Label = id
#    Location = self.portal_url() + "/dummy.html"
#    REQUEST.form['DsID'] = context.fedoraAddDatastream(self,REQUEST,PID,Label,"text/html",Location,"M","","","A")
#    REQUEST.form['PID'] = PID    

#if body == "":
#    REQUEST.form['body'] = context.fedoraAccess(PID,DsID,Date=None)['stream']

#new_context = context.portal_factory.doCreate(context, id)
#new_context.processForm()


portal_status_message = REQUEST.get('portal_status_message', 'Konvertierung wird durchgeführt.')
Location = self.absolute_url() + "/body"
JournalPID = params['JournalPID']
newPID = context.fedoraCreateNewArticle(JournalPID, JournalPID, params, Location)
print Location
print articlePID
print 'NEW',newPID
return printed

#return state.set(status='success',\
#                 context=new_context,\
#                 portal_status_message=portal_status_message)
