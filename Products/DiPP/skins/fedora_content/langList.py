##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name,lang
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

Languages = {
    ''   :'--- Sprache ---',
    'ger':'Deutsch',
    'eng':'Englisch',
    'fra':'Französisch',
    'spa':'Spanisch',
    'ita':'Italienisch'
}

keys = Languages.keys()

print '<select name="' + name + '">'

for Language in keys:
    if lang == Language:
        selected = ' selected="selected"'
    else:
        selected = ''
    print '  <option value="' + Language + '"' + selected + '>' + Languages[Language] + '</option>\n'

print '</select>'

return printed
