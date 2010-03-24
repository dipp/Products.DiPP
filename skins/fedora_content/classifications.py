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

Normdateien = [
   {'id':'swd','title':'SWD (Schlagwortnormdatei)','url':'http://www.bsz-bw.de/cgi-bin/oswd-suche.pl'},
]
#    'lcsh':'LCSH (Library of Congress Subject Headings)',
#    'mesh':'MeSH (Medical Subject Headings)',
#    'ddc' :'DDC (Dewey Decimal Classification)',
#    'lcc' :'LCC (Library of Congress Classification)',
#    'udc' :'UDC (Universal Decimal Classification)',
#    'rvk' :'RVK (Regensburger Verbundklassifikation)',
#    'bk'  :'BK (Basis-Klassifikation)',
#    'pacs':'PACS (Physics and Astronomy Classification Scheme)',
#    'msc' :'MSC (Mathematics Subject Classification)'
#]

return Normdateien
