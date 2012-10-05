Artikelkonvertierung
####################

Grundlage für eine erfolgreiche Artikelkonvertierung ist die korrekte Verwendung
der Formatvorlage. Wichtig sind vor allem die Formate für den  Kopf des Artikels,
der die Metadaten enthält. Anhand der Namen der Absatzformate identifiziert die
Konvertierungsoftware  den Titel, die Autoren, den Abstract, etc. Danach wird eine
Überschrift erster Ordung benötigt, um den eigentliche  Artikeltext von den Metadaten
zu trennen.

.. attention::
   Ein Absatz mit dem Absatzformat "Überschrift 1" ist zwingend vorgeschrieben.
   Er kann leer sein, muss aber existieren, da der Konverter ansonsten nicht
   erkennt, wo der eigentliche Artikel beginnt.

.. figure:: images/artikel-in-word.png
    :alt: Artikel in Word 2007

    Ein Artikel mit angewandter Formatvorlage. Entwurfsansicht mit 
    eingeblendeten Absatzformaten

Die Standardformatvorlage enthält eine Reihe von Absatzformaten, die im Artikelkopf
angewendet werden können, bzw. müssen. Die bezeichnung und die Reihenfolge ist 
wichtig, kann jedoch an die jeweiligen Bedürfnisse angepasst werden. Dafür ist 
jedoch auch eine Anpassungen der journalspezifischen XSL und XSLT Datei für die
Konvertierungssoftware notwendig.  

================== ========================================================
Name der Vorlage   Bedeutung
================== ========================================================
dippTitle          Titel der Artikels, erforderlich. 
dippSubtitle       evtl. Untertitel
dippAuthor         ein oder mehrere Autoren
Copyright          enthält nach der Konvertierun die URN
dippAbstractTitle  Überschrift für den Abstract, kann nur einmal vorkommen
dippAbstract       der Abstract selber
================== ========================================================

 
 
:guilabel:`Test Online Transformation` oder :guilabel:`weiter mit Metadaten`  
    