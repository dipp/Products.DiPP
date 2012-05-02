##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name,pubType
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE


types = {
    'article': 'Zeitschriftenartikel (default)',
    'report' : 'Bericht',
    'paper'  : 'Paper',
    'conf-proceeding' :' Tagungs- und Konferenzbeitrag',
    'lecture'    :' Vorlesung'
}


keys = types.keys()
keys.sort()
#print DDC
print '<select name="' + name + '">'

for type in keys:
    if type == pubType:
        selected = ' selected="selected"'
    else:
        selected = ''
    print '  <option value="' + type + '"' + selected + '> ' + types[type] + '</option>\n'

print '</select>'

return printed
