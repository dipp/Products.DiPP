## Script (Python) "alphabetic_authors"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=self
##title=
##

request  = container.REQUEST
RESPONSE = request.RESPONSE
authors = self.portal_catalog.uniqueValuesFor('Contributors')
initials = 'abcdefghijklmnopqrstuvwxyz'
alphabetic_list = {}

for initial in initials:
    alphabetic_list[initial] = []
    
for author in authors:
    initial = author[0].lower() 
    if not alphabetic_list.has_key(initial):
        alphabetic_list[initial] = []
    a = alphabetic_list[initial]
    a.append(author)
    alphabetic_list[initial] = a

# print alphabetic_list.keys()
initials = alphabetic_list.keys()
initials.sort()
return alphabetic_list