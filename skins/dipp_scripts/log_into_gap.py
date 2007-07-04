## Script (Python) "gap_login"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
request  = container.REQUEST
RESPONSE = request.RESPONSE


GAP_URL      = "http://www.gapdev.de"
ACTION       = "login"
SHOW         = "new_document"
USERNAME     = request.form['username']
PASSWORD     = request.form['password']
CONTAINER_ID = self.portal_properties.dipp_properties.container_id
LDAP_OU      = self.portal_properties.dipp_properties.ldap_ou
AUTH_DOMAIN  = "LDAP:DIPP_NRW_" + LDAP_OU.upper()
url  = ""
url += GAP_URL
url += "/index.php"
url += "?action=" + ACTION
url += "&show=" + SHOW
url += "&login[username]=" + USERNAME
url += "&login[password]=" + PASSWORD
url += "&login[auth_domain]=" + AUTH_DOMAIN
url += "&container_id=" + CONTAINER_ID


RESPONSE.redirect(url)
#return member
