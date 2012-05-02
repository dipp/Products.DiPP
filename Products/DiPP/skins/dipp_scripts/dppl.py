## Script (Python) "gap_login"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=rights,lang
##title=
##

# -*- coding: utf-8 -*-
request  = container.REQUEST
RESPONSE = request.RESPONSE

if rights == 'DPPL':
    details = {'en'  : 'Digital Peer Publishing License',
               'de'  : 'Digital Peer Publishing Lizenz',
               'url' : {'de':'http://www.dipp.nrw.de/lizenzen/dppl/dppl/DPPL_v2_de_06-2004.html',
                        'en':'http://www.dipp.nrw.de/lizenzen/dppl/dppl/DPPL_v2_en_06-2004.html'}
              }
elif rights == 'mDPPL':
    details = {'en'  : 'modular Digital Peer Publishing License',
               'de'  : 'modularen Digital Peer Publishing Lizenz',
               'url' : {'de':'http://www.dipp.nrw.de/lizenzen/dppl/mdppl/m-DPPL_v1_de_11-2004.html',
                        'en':'http://www.dipp.nrw.de/lizenzen/dppl/mdppl/m-DPPL_v1_de_11-2004.html'}
               }
elif rights == 'fDPPL':
    details = {'en'  : 'free Digital Peer Publishing License',
               'de'  : 'freien Digital Peer Publishing Lizenz',
               'url' : {'de':'http://www.dipp.nrw.de/lizenzen/dppl/fdppl/f-DPPL_v1_de_11-2004.html',
                        'en':'http://www.dipp.nrw.de/lizenzen/dppl/fdppl/f-DPPL_v1_de_11-2004.html'}
              }
else:
    details = {'en': rights,
               'de': rights,
               'url' : {'de':'no url given',
                        'en':'no url given'}
               }
return details
