##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name,norm
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

Normdateien = {
    ''    :'--- wählen Sie eine Normdatei ---',
    'swd' :'SWD (Schlagwortnormdatei)',
    'lcsh':'LCSH (Library of Congress Subject Headings)',
    'mesh':'MeSH (Medical Subject Headings)',
    'ddc' :'DDC (Dewey Decimal Classification)',
    'lcc' :'LCC (Library of Congress Classification)',
    'udc' :'UDC (Universal Decimal Classification)',
    'rvk' :'RVK (Regensburger Verbundklassifikation)',
    'bk'  :'BK (Basis-Klassifikation)',
    'pacs':'PACS (Physics and Astronomy Classification Scheme)',
    'msc' :'MSC (Mathematics Subject Classification)'
}

keys = Normdateien.keys()
keys.sort()
print '<select name="' + name + '">'

for Normdatei in keys:
    if Normdatei == norm:
        selected = 'selected="selected"'
    else:
        selected = ''
    print '  <option value="' + Normdatei + '"' + selected + '>'  + Normdateien[Normdatei] + '</option>\n'

print '</select>'
return printed
