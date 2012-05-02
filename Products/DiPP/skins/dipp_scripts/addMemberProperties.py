##Script (Python) "addMemberProperties"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE


if not hasattr(self.portal_properties, 'member_properties'):
    self.portal_properties.addPropertySheet('member_properties', 'Extended member properties')

member_props= (
    ('academictitle_visible','boolean',True),
    ('academictitle_required','boolean',False),
    ('givenname_visible','boolean',True),
    ('givenname_required','boolean',False),
    ('surname_visible','boolean',True),
    ('surname_required','boolean',False),
    ('organization_visible','boolean',True),
    ('organization_required','boolean',False),
    ('postaladdress_visible','boolean',True),
    ('postaladdress_required','boolean',False),
    ('postalcode_visible','boolean',True),
    ('postalcode_required','boolean',False),
    ('phone_visible','boolean',True),
    ('phone_required','boolean',False),
    ('location_visible','boolean',True),
    ('location_required','boolean',False),
)

props = self.portal_properties.member_properties

for prop_id, prop_type, prop_value in member_props:
    if not hasattr(props, prop_id):
        #props._setProperty(prop_id, prop_value, prop_type)
        props.manage_addProperty(id = prop_id, value = prop_value, type =  prop_type)
