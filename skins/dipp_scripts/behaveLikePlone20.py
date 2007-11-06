## Script (Python) "behaveLikePlone20"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
"""
set a few properties to make the new Plone-2.1 instance behabe like
the old Plone-2.0
"""

np = context.portal_properties.navtree_properties
sp = context.portal_properties.site_properties
md = context.portal_memberdata

try:
    np.manage_changeProperties(enable_wf_state_filtering=True)
    np.manage_changeProperties(wf_states_to_show=('published'))
    print "Return to Plone 2.0.4 navigation"
except:
    print "Could not return to Plone 2.0.4 navigation"

try:
    sp.manage_changeProperties(disable_folder_sections=True)
    print "turn off the folders in the horizontal bar"
except:
    print "could not turn off the folders in the horizontal bar"

try:
    sp.manage_changeProperties(allowAnonymousViewAbout=False)
    print "turn off document_byline for anonymous users"
except:
    print "could not turn off document_byline for anonymous users"

try:
    sp.manage_changeProperties(visible_ids=True)
    md.manage_changeProperties(visible_ids=True)
    print "turn on visible_ids for anonymous users"
except:
    print "Could not turn on visible_ids for anonymous users"

return printed
