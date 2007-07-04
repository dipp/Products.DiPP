## Script (Python) "admin_save"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(context, 'portal_url')
portal = portal_url.getPortalObject()

dp = portal.portal_properties.dipp_properties
dp.manage_changeProperties({'defaultLanguage':request.form['defaultLanguage'],
                                'alertEmailAddresses':request.form['alertEmailAddresses'],
                                'alertEmailText':request.form['alertEmailText'],
                                'deadline_yellow_email_de':request.form['deadline_yellow_email_de'],
                                'deadline_yellow_email_en':request.form['deadline_yellow_email_en'],
                                'author_notice_de':request.form['author_notice_de'],
                                'author_notice_en':request.form['author_notice_en'],
                                'deadline_red_email_de':request.form['deadline_red_email_de'],
                                'deadline_red_email_en':request.form['deadline_red_email_en']})
portal_status_message = "Änderungen wurden gespeichert"

if request:
     request.RESPONSE.redirect(request.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
