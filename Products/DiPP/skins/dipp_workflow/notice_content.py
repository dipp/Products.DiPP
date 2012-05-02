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
mtool    = context.portal_membership
portal_url  = getToolByName(self, 'portal_url')
dp = self.portal_properties.dipp_properties

instance, workitem = oftool.getInstanceAndWorkitem(instance_id, workitem_id)

PID = workitem.PID
autor     = workitem.autor
member    = mtool.getMemberById(autor)
fullname = member.getProperty('fullname', '')
email = member.getProperty('email', '')
lang = member.getProperty('language', 'en')


if lang.lower() == "de":
    mail = dp.author_notice_de
elif lang.lower() == "en":
    mail= dp.author_notice_en
elif lang.lower() == "":
    mail= dp.author_notice_en
else:
    mail = "no mail template found for Language\n   "
    mail+= lang


results = context.portal_catalog.searchResults(
    getPID = PID,
    Language='all'
)

if results:
    title = results[0].Title
else:
    title = PID


journal = self.portal_properties.title()
email_from_name = self.portal_properties.email_from_name
next_workitem_id = str(int(workitem_id) + 1)
next_step = "%s/pub_imprimatur_form?instance_id=%s&workitem_id=%s&process_id=Publishing&activity_id=imprimatur" % (portal_url(), instance_id, next_workitem_id)

body = mail % {
    "fullname":fullname,
    "login":workitem.autor,
    "title":title,
    "deadline":str(workitem.deadline_next),
    "url":context.worklist.absolute_url(),
    "journal":journal,
    "from":email_from_name,
    "next_step":next_step
    }

return body
