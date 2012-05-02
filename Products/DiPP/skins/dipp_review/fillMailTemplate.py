## Script (Python) "fillMailTemplate"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self, mail_template_id="", recipient="", link_agreed="", link_declined="", link_unavailable=""
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(self, 'portal_url')
portal = portal_url.getPortalObject()
wf_tool = portal.portal_workflow
mship = self.portal_membership
props = self.portal_properties.dippreview_properties
template = self.portal_properties.dippreview_properties.getProperty(mail_template_id)
footer = self.portal_properties.dippreview_properties.getProperty("email_footer")

to_email = portal.email_from_address
to_name = mship.getMemberInfo(recipient)['fullname']
from_email = portal.email_from_address
from_name = portal.email_from_name
journal = portal.title
submission_id = self.id
manuscript_url = self.absolute_url()
manuscript_title = self.title
manuscript_abstract = self.manuscript_abstract
user = mship.getAuthenticatedMember()
actor_name = user.getProperty('fullname',None)
max_review_time = str(props.max_review_time)
body = template % {
    'from_name':from_name,
    'to_name':to_name,
    'journal': journal,
    'max_review_time': max_review_time,
    'submission_id':submission_id,
    'manuscript_url':manuscript_url,
    'manuscript_title':manuscript_title,
    'manuscript_abstract':manuscript_abstract,
    'actor_name':actor_name,
    'link_agreed':link_agreed,
    'link_declined':link_declined,
    'link_unavailable':link_unavailable,
    'max_review_time':max_review_time
    }

return body + "\n" + footer
