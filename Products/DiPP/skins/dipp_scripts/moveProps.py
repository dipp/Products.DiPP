## Script (Python) "moveProps"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
response = request.RESPONSE

portal_url = getToolByName(context, 'portal_url')
site     = portal_url.getPortalObject()

dprops = site.portal_properties.dipp_properties    

site_properties = (
    ('deadline_max',56,'int') ,
    ('deadline_default',14,'int'), 
    ('deadline_red',3,'int'),
    ('deadline_yellow',10,'int'), 
    ('deadline_no','1970/01/01 12:00:00 GMT+1','date'),
    ('deadline_change',('Herausgeber',),'lines'),
    ('deadline_next_change',('Herausgeber', 'Redakteur'),'lines'),
    ('deadline_red_email_de',"Bitte umgehend den Artikel bearbeiten\n\nmfg",'text'),
    ('deadline_red_email_en',"Bitte umgehend den Artikel bearbeiten\n\nmfg",'text'),
    ('deadline_yellow_email_de',"Bitte an die Bearbeitung des Artikels denken!\n\nmfg",'text'),
    ('deadline_yellow_email_en',"Bitte an die Bearbeitung des Artikels denken!\n\nmfg",'text'),
    ('defaultLanguage',"de",'string'),
    ('roles_not_to_list',('Manager', 'Owner', 'Reviewer', 'Member'),'lines'),
    ('actions_to_list',('Call Application', 'Self Assign', 'Assign', 'Unassign'),'lines'),
    ('workflow_actions',('Call Application', 'Self Assign', 'Assign', 'Unassign', 'Suspend', 'Resume', 'Fallout', 'Fallin', 'End Fallin', 'Activate', 'Inactive', 'Complete', 'Forward'),'lines'),
    ('copy_of_reminder',('',),'lines')
)

for prop_id, prop_value, prop_type in site_properties:
    if  not dprops.hasProperty(prop_id):
        if  site.hasProperty(prop_id):
            existing_value = site.getProperty(prop_id)
            dprops.manage_addProperty(id = prop_id, value = existing_value, type = prop_type)
            site.manage_delProperties([prop_id])
            print "Property %s moved " % (prop_id)
        else:
            dprops.manage_addProperty(id = prop_id, value = prop_value, type = prop_type)
            print "Property %s added" % prop_id
    else:
        print "Property %s exists" % prop_id
        

return printed
