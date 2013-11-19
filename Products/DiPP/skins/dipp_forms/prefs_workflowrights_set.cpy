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
dp.manage_changeProperties({'deadline_change':request.form['deadline_change'],
                                'actions_to_list':request.form['actions_to_list'],
                                'deadline_next_change':request.form['deadline_next_change']})

msg = "Änderungen an den Workflowrechten wurden gespeichert"

if request:
    context.plone_utils.addPortalMessage(msg)
    request.RESPONSE.redirect(request.HTTP_REFERER)
