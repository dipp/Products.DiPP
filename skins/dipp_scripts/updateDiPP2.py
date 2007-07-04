## Controller Python Script "register"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=self,password='password', confirm='confirm', came_from_prefs=None
##title=Register a User
##
from ZODB.POSException import ConflictError

REQUEST=context.REQUEST

mhost = context.MailHost

portal_registration=context.portal_registration
site_properties=context.portal_properties.site_properties

username = REQUEST['username']
