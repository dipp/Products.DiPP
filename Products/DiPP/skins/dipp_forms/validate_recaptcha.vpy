## Controller Python Script "validate_recaptcha"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=recaptcha_challenge_field='', recaptcha_response_field=''
##title=validates the Registration of a User

# -*- coding: utf-8 -*-

request  = container.REQUEST
from Products.CMFCore.utils import getToolByName

utils = getToolByName(context, 'Utils')

def missing(field):
    state.setError(field, 'This field is required, please provide some information.', 'input_required')

if not recaptcha_response_field:
    missing('recaptcha')

ip = utils.get_ip(request)

two_words = False
if recaptcha_response_field:
    words = recaptcha_response_field.split()
    if len(words) != 2:
        state.setError('recaptcha', 'Bitte geben Sie exakt zwei Worte ein', 'input_required')
    else:
        two_words = True

if two_words:
    is_valid, error_code = utils.validate_recaptcha(recaptcha_challenge_field, recaptcha_response_field, ip)
    if not is_valid:
        state.setError('recaptcha', 'Versuchen Sie es noch einmal.', 'input_required')

if state.getErrors():
    return state.set(status='failure', 
        portal_status_message='Please correct the indicated errors.'
        )
else:
    return state
