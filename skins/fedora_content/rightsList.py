## Script (Python) "rightsList"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name,rights
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

Licences = {
    'DPPL':'Digital Peer Publishing Lizenz',
    'mDPPL':'modulare Digital Peer Publishing Lizenz',
    'fDPPL':'freie Digital Peer Publishing Lizenz'
}

keys = Licences.keys()

#print '<select name="' + name + '">'

for Licence in keys:
    if rights == Licence:
        selected = ' selected="selected"'
    else:
        selected = ''
    print '  <option value="' + Licence + '"' + selected + '>' + Licences[Licence] + '</option>\n'

#print '</select>'

return printed

