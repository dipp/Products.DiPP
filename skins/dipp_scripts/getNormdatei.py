##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name
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
    'pacs':'PACS (Physics and Astronomy Classification Scheme)'
}

return Normdateien[name]
