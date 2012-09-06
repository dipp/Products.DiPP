Konfiguration
=============

Die meisten Einstellungen werden in sogenannten Plone Property Sheets
gespeichert.  Diese findet man unter :menuselection:`ZMI -->
portal_properties`.  Vier Sheets sind relevant f�r das Publikationssystem:
 	
dipp_properties (DiPP properties): 
    enth�lt Konfigurationen, die das Erscheinungsbild von Ausgaben und Artikeln
    beeinflussen.

dippreview_properties (DiPPReview properties): 
    enth�lt Konfigurationen f�r den Peer Review (Fristen, Anzahl Gutachter,
    ...)

member_properties (Extended member properties): 
    enth�lt Konfigurationen f�r das Anmeldeformular, d.h. welche Daten sind
    erforderlich bzw. sollen �berhaupt angezeigt werde.

metadata_properties (QDC Metadata properties): 
    einige Standardwerte f�r di Qualifizierten Dublin Core Metadaten.

 


dipp_properties (DiPP properties)
---------------------------------

.. _prop_alertEmailAddresses:

alertEmailAddresses
^^^^^^^^^^^^^^^^^^^

Eine Liste mit E-Mail Adressen, die bei Veröffentlichung eines Artikel
benachrichtigt werden.

.. _prop_alertEmailText:

alertEmailText
^^^^^^^^^^^^^^

Text dieser Email::

    Dear Ladies and Gentlemen,

    The eJournal %(journal)s is pleased to inform you, that we have just published
    a new article.
    The full text can be found here: %(url)s





dippreview_properties (DiPPReview properties)
---------------------------------------------
member_properties (Extended member properties)
----------------------------------------------
metadata_properties (QDC Metadata properties)
---------------------------------------------
