## Controller Script Python "validate_privacypolicy"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=
##title=validates the form for sending feedback

from Products.CMFPlone import PloneMessageFactory as _
reg_tool = context.portal_registration

privacy = context.REQUEST.get('privacy', False)

if not privacy:
    state.setError('privacy',
                   _(u'Bitte stimmen sie der Verarbeitung ihrer Daten zu.'),
                   'privacy_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')
else:
    return state.set(portal_status_message='You have been registered.')
