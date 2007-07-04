## Controller Python Script "validate_memberdata"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=givenname='',surname='',organization='', postaladdress='',postalcode='',location='',phone='',country=''
##title=validates the extended Memberdata

properties = context.portal_properties.member_properties

def missing(field):
    state.setError(field, 'This field is required, please provide some information.', 'input_required')

#if not academictitle and properties.academictitle_required:
#    missing('academictitle')

if not givenname and properties.givenname_required:
    missing('givenname')

if not surname and properties.surname_required:
    missing('surname')

if not organization and properties.organization_required:
    missing('organization')

if not postaladdress and properties.postaladdress_required:
    missing('postaladdress')

if not postalcode and properties.postalcode_required:
    missing('postalcode')

if not phone and properties.phone_required:
    missing('phone')

if not location and properties.location_required:
    missing('location')


if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')
else:
    return state.set(portal_status_message='You have been registered.')
