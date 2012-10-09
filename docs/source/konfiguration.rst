Konfiguration
=============

Die meisten Einstellungen werden in sogenannten Plone Property Sheets
gespeichert.  Diese findet man unter
:menuselection:`ZMI --> portal_properties`.  Vier Sheets sind relevant für das
Publikationssystem:
 
dipp_properties (DiPP properties): 
    enthält Konfigurationen, die das Erscheinungsbild von Ausgaben und
    Artikeln beeinflussen.

dippreview_properties (DiPPReview properties): 
    enthält Konfigurationen für den Peer Review (Fristen, Anzahl Gutachter,
    ...)

member_properties (Extended member properties): 
    enthält Konfigurationen für das Anmeldeformular, d.h. welche Daten sind
    erforderlich bzw. sollen überhaupt angezeigt werde.

metadata_properties (QDC Metadata properties): 
    einige Standardwerte für die Qualifizierten Dublin Core Metadaten.

 


dipp_properties (DiPP properties)
---------------------------------


.. _prop_issn:

ISSN
^^^^

Die *International Standard Serial Number*. Kann mit erscheinen der ersten Artikel
bei der Deutschen Nationalbibliothek beantragt werden.

.. _prop_alertEmailAddresses:

alertEmailAddresses
^^^^^^^^^^^^^^^^^^^
Eine Liste mit E-Mail Adressen, die bei Veröffentlichung eines Artikel
benachrichtigt werden.

Default::

    dipp@hbz-nrw.de

.. _prop_alertEmailText:

alertEmailText
^^^^^^^^^^^^^^
Text dieser Email::

    Dear Ladies and Gentlemen,

    The eJournal %(journal)s is pleased to inform you, that we have just
    published a new article.
    The full text can be found here: %(url)s

Zur Verfügung stehende Platzhalter:

======== =================
Name     Bedeutung
======== =================
journal  Name des journals
url      URL des Artikels
======== =================


citation_format
^^^^^^^^^^^^^^^
String, der zum Formatieren der empfolenen Zitierweise verwendet wird, wie sie
unter dem Artikel bzw. auf der Seite mit den Metadaten zu dinen ist.

Default::

    %(authors)s (%(year)s). %(title)s. %(journal)s, Vol. %(volume)s. (%(urn)s)

Zur Verfügung stehende Platzhalter:

========== ============================================================
Name       Bedeutung
========== ============================================================
authors    Liste der Autoren, kann durch weitere Parameter detailierter
           formatiert werden
title      Titel des Artikels
journal    Name des Journals
volume     Jahrgang
issue      Ausgabe
startpage  erste Seite (bei PDF)
endpage    letzte Seite (bei PDF)
year       Jahreszahl, wird aus den Datum der Veröffentlich extrahiert
date       Datum der Veröffentlichung
id         die PID ohne des Prefix 'dipp:'
urn        Der URN
========== ============================================================

.. _prop_short_citation_format:

short_citation_format
^^^^^^^^^^^^^^^^^^^^^
String, der zum Formatieren der verkürzten Zitierweise verwendet wird. Wird aus
den Metadaten erzeugt, die auch im Plone Katalog indexiert sind und keinen
Aufruf von Fedora erfordern. Kann z.B. auf den Inhaltsverzeichnissen oder den
Feeds verwendet werden.

Default::

    %(journal)s, Vol. %(volume)s, Iss. %(issue)s

Zur Verfügung stehende Platzhalter:

================== ============================================================
Name               Bedeutung
================== ============================================================
journal            Name des Journals
journal_shortname  Abkürzung des Journals
volume             Jahrgang
issue              Ausgabe
startpage          erste Seite (bei PDF)
endpage            letzte Seite (bei PDF)
year               Jahreszahl, wird aus den Datum der Veröffentlich extrahiert
issuedate          Datum der Veröffentlichung
urn                Der URN
================== ============================================================

show_recommended_citation
^^^^^^^^^^^^^^^^^^^^^^^^^
Soll unterhalb des Artikels das bibliographische Zitat angezeigt werden?

Default::

    True

show_classified_subjects
^^^^^^^^^^^^^^^^^^^^^^^^
Sollen im Artikelkopf die normierten Schlagworte angezeigt werden?

Default::

    False

show_review_history
^^^^^^^^^^^^^^^^^^^
Sollen im Artikelkopf die Daten für Einreichung und Annahme angezeigt werden?

Default::

    False
    
initials_only
^^^^^^^^^^^^^
Im bibliographischen Zitat: Sollen bei den Autoren nur die Initialen angezeigt
werden statt des ausgeschriebenen Vornamens:

Default::

    False

firstnamefirst
^^^^^^^^^^^^^^
Im bibliographischen Zitat: Sollen erst die Vornamen angezeigt werden?

Default::

    False

initials_period
^^^^^^^^^^^^^^^
Im bibl. Zitat: Sollen ein Punkt hinter die Initialen?

Default::

    False

comma_separated
^^^^^^^^^^^^^^^
Im bibl. Zitat: wenn der Vorname nach dem Nachnamen kommt (firstnamefirst =
false), sollen sie durch ein Komma getrennt werden:

Default::

    False

last_author_suffix
^^^^^^^^^^^^^^^^^^
Im  bibl. Zitat: wenn der letzte Autor z.B. durch ein 'und' abgetrennt werden
soll.

Default::

    <leer>

.. _prop_articles_in_portlet:

articles_in_portlet
^^^^^^^^^^^^^^^^^^^
Im Portlet "Current Issue": Sollen die Artikel aufgelistet werden? Sonst
escheint nur ein Link auf die Ausgabe, evtl. mit Bild.

Default::

    True

.. _prop_authors_in_portlet:

authors_in_portlet
^^^^^^^^^^^^^^^^^^
Im Portlet "Current Issue": Sollen auch die Autoren gelistet werden?

Default::

    True


allow_persistent_discussion
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Wenn True, wird unterhalb eines Artikels eine Liste mit Kommentaren und ein Link
zum Einreichen eines eigenen Kommentares eingeblendet. Kommentare sind
ihrerseits wieder begutachtete Artikel.

Default::
   
   False

 
volume_show_covers
^^^^^^^^^^^^^^^^^^
Wenn True, werden auf der Inhaltsseite der Jahrgänge die Titelseiten der
Ausgaben angezeigt, soweit vorhanden.

Default::

   False
   
issue_show_abstracts
^^^^^^^^^^^^^^^^^^^^
Wenn True, werden auf der Inhaltsseite der Ausgaben die verfügbaren Abstracts
der Artikel verlinkt.

Default::

   False

issue_show_full_abstracts
^^^^^^^^^^^^^^^^^^^^^^^^^
Wenn True, werden auf der Inhaltsseite der Ausgaben die Abstracts in voller
Länge angezeigt.

Default::

   False 

issue_show_pdf_link
^^^^^^^^^^^^^^^^^^^
Wenn True, werden auf der Inhaltsseite der Ausgaben vorhandene PDFs direkt
verlinkt.

Default::
   
   False

issue_show_short_citation
^^^^^^^^^^^^^^^^^^^^^^^^^
Wenn True, werden auf der Inhaltsseite der Ausgaben zu den Artikeln das
bibligraphische Zitat in Kurzform angezeigt, siehe
:ref:`prop_short_citation_format`  

Default::

   False

issue_sort_on
^^^^^^^^^^^^^
Bestimmt auf der Inhaltsseite der Ausgaben, wonach die Artikelliste sortiert
werden soll. Möglich sind alle sortierbaren Attribute der Artikel, z.B.
getIssue, getIssueDate, getVolume, getObjPositionInParent. Letzteres ermöglicht
eine manuelle Sortierung, die Reihenfolge im Elternorder (Ausgabe) übernommen
wird.

Default::

   getObjPositionInParent
   
issue_sort_order
^^^^^^^^^^^^^^^^
Aufsteigende (ascending) oder absteigende (reverse) Sortierung der Artikel

Default::

   ascending

discussion_time
^^^^^^^^^^^^^^^
(wird nicht verwendet)

fedora_time_format
^^^^^^^^^^^^^^^^^^
String um die Fedorazeitstempel im ZMI lesbarer anzuzeigen. Sollte eigentlich
niemals geändert werden müssen.

Default::

   %Y-%m-%dT%H:%M:%SZ

issue_date_format
^^^^^^^^^^^^^^^^^
Wenn nicht leer, wird das Datum auf der Ausgabenseite mit dem hier angegebenen
String formatiert. Wenn leer, wird auch kein Datum angezeigt.

Default::
   
   <leer>

recent_articles_range
^^^^^^^^^^^^^^^^^^^^^
Alter (in Tagen) des ältesten Artikels der durch das recent_article Template
angezeigt werden soll. 

Default::

   30
   
                     
dippreview_properties (DiPPReview properties)
---------------------------------------------

member_properties (Extended member properties)
----------------------------------------------

metadata_properties (QDC Metadata properties)
---------------------------------------------
