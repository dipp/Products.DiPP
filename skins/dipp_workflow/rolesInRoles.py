## Script (Python) "rolesInRoles"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=roles
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

userRoles = container.REQUEST.AUTHENTICATED_USER.getRoles()

hasRole = "False"

for role in userRoles:
	if role in roles:
		hasRole = "True"
	else:
		pass

return hasRole
