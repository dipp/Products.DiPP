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
portal.manage_changeProperties({'deadline_max':request.form['deadline_max'],
                                'deadline_default':request.form['deadline_default'],
                                'deadline_yellow':request.form['deadline_yellow'],
                                'deadline_red':request.form['deadline_red']})
portal_status_message = "Änderungen wurden gespeichert"
#print portal_url
#print request
#return printed

if request:
     request.RESPONSE.redirect(request.HTTP_REFERER + "?portal_status_message=" + portal_status_message)
