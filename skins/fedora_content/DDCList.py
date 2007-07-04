##script (Python) "sdf"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=name,DDC
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE


Sachgruppen = {
    ''   :'--- wählen Sie eine DDC Sachgrupe ---',
    '000':'Informatik, Informationswissenschaft, allgemeine Werke',
    '004':' Informatik',
    '010':' Bibliografien',
    '020':' Bibliotheks- und Informationswissenschaft',
    '030':' Enzyklopädien',
    '050':' Zeitschriften, fortlaufende Sammelwerke',
    '060':' Organisationen, Museumswissenschaft',
    '070':' Nachrichtenmedien, Journalismus, Verlagswesen',
    '080':' Allgemeine Sammelwerke',
    '090':' Handschriften, seltene Bücher',
    '100':'Philosophie und Psychologie',
    '130':' Parapsychologie, Okkultismus',
    '150':' Psychologie',
    '200':'Religion',
    '220':' Bibel',
    '230':' Theologie, Christentum',
    '290':' Andere Religionen',
    '300':'Sozialwissenschaften',
    '310':' Statistik',
    '320':' Politik',
    '330':' Wirtschaft',
    '340':' Recht',
    '350':' Öffentliche Verwaltung',
    '355':' Militär',
    '360':' Soziale Probleme, Sozialarbeit',
    '370':' Erziehung, Schul- und Bildungswesen',
    '380':' Handel, Kommunikation, Verkehr',
    '390':' Ethnologie',
    '400':'Sprache',
    '420':' Englisch',
    '430':' Deutsch',
    '439':' Andere germanische Sprachen',
    '440':' Französisch, romanische Sprachen allgemein',
    '450':' Italienisch, Rumänisch, Rätoromanisch',
    '460':' Spanisch, Portugiesisch',
    '470':' Latein',
    '480':' Griechisch',
    '490':' Andere Sprachen',
    '500':'Naturwissenschaften und Mathematik',
    '510':' Mathematik',
    '520':' Astronomie, Kartographie',
    '530':' Physik',
    '540':' Chemie',
    '550':' Geowissenschaften',
    '560':' Paläontologie',
    '570':' Biowissenschaften, Biologie',
    '580':' Pflanzen (Botanik)',
    '590':' Tiere (Zoologie)',
    '600':'Technik, Medizin, angewandte Wissenschaften',
    '610':' Medizin, Gesundheit',
    '620':' Ingenieurwissenschaften',
    '630':' Landwirtschaft, Veterinärmedizin',
    '640':' Hauswirtschaft',
    '650':' Management',
    '660':' Technische Chemie',
    '670':' Industrielle Fertigung',
    '690':' Hausbau, Bauhandwerk',
    '700':'Künste und Unterhaltung',
    '710':' Landschaftsgestaltung, Raumplanung',
    '720':' Architektur',
    '730':' Plastik, Numismatik, Keramik, Metallkunst',
    '740':' Zeichnung, Kunsthandwerk',
    '741.5':' Comics, Cartoons, Karikaturen',
    '750':' Malerei',
    '760':' Grafische Verfahren, Drucke',
    '770':' Fotografie, Computerkunst',
    '780':' Musik',
    '790':' Freizeitgestaltung, Darstellende Kunst',
    '791':' Öffentliche Darbietungen, Film, Rundfunk',
    '792':' Theater, Tanz',
    '793':' Spiel',
    '796':' Sport',
    '800':'Literatur',
    '810':' Englische Literatur Amerikas',
    '820':' Englische Literatur',
    '830':' Deutsche Literatur',
    '839':' Literatur in anderen germanischen Sprachen',
    '840':' Französische Literatur',
    '850':' Italienische, rumänische, rätoromanische Literatur',
    '860':' Spanische und portugiesische Literatur',
    '870':' Lateinische Literatur',
    '880':' Griechische Literatur',
    '890':' Literatur in anderen Sprachen',
    '900':'Geschichte und Geografie',
    '910':' Geografie, Reisen',
    '914.3':' Landeskunde Deutschlands',
    '920':' Biografie, Genealogie, Heraldik',
    '930':' Alte Geschichte, Archäologie',
    '940':' Geschichte Europas',
    '943':' Geschichte Deutschlands',
    '950':' Geschichte Asiens',
    '960':' Geschichte Afrikas',
    '970':' Geschichte Nordamerikas',
    '980':' Geschichte Südamerikas',
    '990':' Geschichte der übrigen Welt'
}


keys = Sachgruppen.keys()
keys.sort()
#print DDC
print '<select name="' + name + '">'

for Sachgruppe in keys:
    if Sachgruppe == DDC:
        selected = ' selected="selected"'
    else:
        selected = ''
    print '  <option value="' + Sachgruppe + '"' + selected + '>' + Sachgruppe + ' ' + Sachgruppen[Sachgruppe] + '</option>\n'

print '</select>'

return printed
