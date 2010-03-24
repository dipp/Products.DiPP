##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

classifactions = [
    {'id':'swd', 'title':'SWD (Schlagwortnormdatei)', 'url':'http://www.bsz-bw.de/cgi-bin/oswd-suche.pl'},
    {'id':'SWD', 'title':"Schlagwort Normdatei", 'url':'http://www.bsz-bw.de/cgi-bin/oswd-suche.pl'},
    {'id':'LCSH ', 'title':"Library of Congress Subject Headings",'url':'http://authorities.loc.gov'},
    {'id':'MeSH', 'title':"Medical Subject Headings", 'url':'http://www.nlm.nih.gov/mesh/meshhome.html'},
    {'id':'DDC', 'title':"Dewey Decimal Classification", 'url':'http://www.oclc.org/dewey/versions/webdewey/default.htm'},
    {'id':'DDC (de)', 'title':"DDC, Deutsche Version", 'url':'http://www.ddc-deutsch.de'},
    {'id':'LCC ', 'title':"Library of Congress Classification", 'url':'http://www.loc.gov/catdir/cpso/lcco/lcco.html'},
    {'id':'UDC', 'title':"Universal Decimal Classification", 'url':'http://www.udcc.org/outline/outline.htm'},
    {'id':'RVK','title':"Regensburger Verbundklassifikation",'url':'http://www.bibliothek.uni-regensburg.de/rvko_neu/'},
    {'id':'BK', 'title':"Basis-Klassifikation", 'url':'http://www.gbv.de/vgm/info/mitglieder/02Verbund/01Erschliessung/02Richtlinien/05Basisklassifikation/index'},
    {'id':'PACS', 'title':"Physics and Astronomy Classification Scheme", 'url':'http://publish.aps.org/PACS/'},
    {'id':'MSC','title':"2000 Mathematics Subject Classification", 'url':'http://www.ams.org/msc/'}
]
return classifactions
