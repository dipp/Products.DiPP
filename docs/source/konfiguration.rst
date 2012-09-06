Konfiguration
=============

Die meisten Einstellungen werden in sogenannten Plone Property Sheets
gespeichert.  Diese findet man unter :menuselection:`ZMI -->
portal_properties`.  Vier Sheets sind relevant für das Publikationssystem:
 	
dipp_properties (DiPP properties): 
    enthält Konfigurationen, die das Erscheinungsbild von Ausgaben und Artikeln
    beeinflussen.

dippreview_properties (DiPPReview properties): 
    enthält Konfigurationen für den Peer Review (Fristen, Anzahl Gutachter,
    ...)

member_properties (Extended member properties): 
    enthält Konfigurationen für das Anmeldeformular, d.h. welche Daten sind
    erforderlich bzw. sollen überhaupt angezeigt werde.

metadata_properties (QDC Metadata properties): 
    einige Standardwerte für di Qualifizierten Dublin Core Metadaten.

 


dipp_properties (DiPP properties)
---------------------------------

.. _prop_alertEmailAddresses:

alertEmailAddresses
^^^^^^^^^^^^^^^^^^^

Eine Liste mit E-Mail Adressen, die bei VerÃ¶ffentlichung eines Artikel
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
