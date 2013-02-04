## Script (Python) "prefs_deadlines_set"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

from Products.CMFCore.utils import getToolByName
translate = context.translate

request  = container.REQUEST
RESPONSE = request.RESPONSE

portal_url = getToolByName(context, 'portal_url')
portal = portal_url.getPortalObject()

dp = portal.portal_properties.dipp_properties
dp.manage_changeProperties({'deadline_max':request.form['deadline_max'],
                            'deadline_default':request.form['deadline_default'],
                            'deadline_yellow':request.form['deadline_yellow'],
                            'deadline_red':request.form['deadline_red']})

msg = translate('settings_saved', domain='dipp')

context.plone_utils.addPortalMessage(msg)
if request:
     request.RESPONSE.redirect(request.HTTP_REFERER)
