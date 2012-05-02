##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

academicTitles = ('','Dr.', 'Prof.', 'Prof. Dr.')
return academicTitles
