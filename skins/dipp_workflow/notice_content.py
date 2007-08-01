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
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE
oftool   = container.portal_openflow
#mtool    = context.portal_membership
portal_url  = getToolByName(self, 'portal_url')

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

dp = self.portal_properties.dipp_properties
if lang.lower() == "de":
    mail = dp.author_notice_de
elif lang.lower() == "en":
    mail= dp.author_notice_en
else:
    mail = "no mail template found for Language\n   "
    mail+= lang


journal = self.portal_properties.title
email_from_name = self.portal_properties.email_from_name
next_workitem_id = str(int(workitem_id) + 1)
next_step = portal_url()
next_step += "/pub_imprimatur_form"
next_step += "?instance_id=" + instance_id
next_step += "&workitem_id=" + next_workitem_id
next_step += "&process_id=Publishing&activity_id=imprimatur"



body = mail % {
    "fullname":fullname,
    "login":workitem.autor,
    "title":workitem.titel,
    "deadline":str(workitem.deadline_next),
    "url":context.worklist.absolute_url(),
    "journal":journal,
    "from":email_from_name,
    "next_step":next_step
    }

return body
