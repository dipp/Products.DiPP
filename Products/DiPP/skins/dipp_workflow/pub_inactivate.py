## Script (Python) "pub_modify_instance"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName

request     = container.REQUEST
RESPONSE    = request.RESPONSE
oftool      = container.portal_openflow

instance_id = request.form['instance_id']
workitem_id = request.form['workitem_id']

instance, workitem = oftool.getInstanceAndWorkitem(instance_id, workitem_id)

oftool.inactivateWorkitem(instance_id=instance_id,workitem_id=workitem_id)
msg = "Schritt abgebrochen!"
RESPONSE.redirect('%s/worklist' % context.absolute_url() + '?portal_status_message=' + msg)
