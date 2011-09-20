##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

classifications =  {
    'swd': {'title':"Schlagwort Normdatei", 'url':'http://www.bsz-bw.de/cgi-bin/oswd-suche.pl'},
    'lcsh':{'title':"Library of Congress Subject Headings",'url':'http://authorities.loc.gov'},
    'mesh':{'title':"Medical Subject Headings", 'url':'http://www.nlm.nih.gov/mesh/meshhome.html'},
    'ddc':{'title':"Dewey Decimal Classification", 'url':'http://www.oclc.org/dewey/versions/webdewey/default.htm'},
    'lcc':{'title':"Library of Congress Classification", 'url':'http://www.loc.gov/catdir/cpso/lcco/lcco.html'},
    'udc':{'title':"Universal Decimal Classification", 'url':'http://www.udcc.org/outline/outline.htm'},
    'rvk':{'title':"Regensburger Verbundklassifikation",'url':'http://www.bibliothek.uni-regensburg.de/rvko_neu/'},
    'bk':{'title':"Basis-Klassifikation", 'url':'http://www.gbv.de/vgm/info/mitglieder/02Verbund/01Erschliessung/02Richtlinien/05Basisklassifikation/index'},
    'pacs':{'title':"Physics and Astronomy Classification Scheme", 'url':'http://publish.aps.org/PACS/'},
    'msc':{'title':"2000 Mathematics Subject Classification", 'url':'http://www.ams.org/msc/'},
    'jel':{'title':"Journal of Economic Literature", 'url':'http://www.aeaweb.org/jel/jel_class_system.php'}
}
return classifications
