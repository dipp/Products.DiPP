## Script (Python) "notice_content"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self,instance_id, workitem_id
##title=
##
# actor, 
request  = container.REQUEST
RESPONSE = request.RESPONSE
oftool   = container.portal_openflow
#mtool    = context.portal_membership

instance, workitem = oftool.getInstanceAndWorkitem(instance_id, workitem_id)

autor     = workitem.autor
titel     = instance.titel
#member    = mtool.getMemberById(autor)
#fullname  = member.fullname
#email     = member.email

member   = context.ext.getMember(autor)

fullname = member['cn']
email    = member['mail']
lang     = member['preferredLanguage']
if lang.lower() == "de":
    mail = self.portal_properties.author_notice_de
    anrede = "Sehr geehrte(r) "
elif lang.lower() == "en":
    mail= self.portal_properties.author_notice_en
    anrede = "Dear "
else:
    mail = "no mail template found for Language\n   "
    mail+= lang

baseUrl  = context.worklist.absolute_url()
# email body
body  = anrede + fullname + ' ,\n\n'
body += mail
body += "\n\n"
body += context.article_info(instance_id,workitem_id)


return body
