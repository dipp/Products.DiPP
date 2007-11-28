## Script (Python) "behaveLikePlone20"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
"""
set a few properties to make the new Plone-2.1 instance behabe like
the old Plone-2.0
"""

from Products.CMFCore.utils import getToolByName
portal_url = getToolByName(self, 'portal_url')
site = portal_url.getPortalObject()


# add two folder to keep temporary files
folders = (
    ('tmp','Temporäre Artikel'),
    ('fedora_tmp','Temporäre Fedoraobjekte')
)

for folder_id, folder_title in folders:
    try:
        site.invokeFactory('Folder',id = folder_id, title = folder_title)
        print "added Folder '%s': %s" (folder_id, folder_title)
    except:
        print "could not add Folder '%s'" % folder_id


# configure the portlets
site.manage_changeProperties({'right_slots':''})
left_slots = (
    'here/portlet_dippnav/macros/portlet',
    'here/portlet_status/macros/portlet',
    'here/portlet_toc/macros/portlet',
    'here/portlet_navigation/macros/portlet'
)

site.manage_changeProperties({'left_slots':left_slots})

# set a few properties to behave a bit more like Plone 2.0
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
