## Script (Python) "docTypeList"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name,docType
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE


types = {
    'text'      :'Text (default)',
    'image'     :'Bilder',
    'multimedia':'Multimediadateien',
    'data'      :'Daten'
}


keys = types.keys()
#keys.sort()
#print DDC
print '<select name="' + name + '">'

for type in keys:
    if type == docType:
        selected = ' selected="selected"'
    else:
        selected = ''
    print '  <option value="' + type + '"' + selected + '> ' + types[type] + '</option>\n'

print '</select>'

return printed

