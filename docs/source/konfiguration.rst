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
    einige Standardwerte für die Qualifizierten Dublin Core Metadaten.

 


dipp_properties (DiPP properties)
---------------------------------

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

    The eJournal %(journal)s is pleased to inform you, that we have just published
    a new article.
    The full text can be found here: %(url)s

Zur Verfügung stehende Platzhalter

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

Im bibliographischen Zitat: Sollen bei den Autoren nur die Initialen angezeigt werden
statt des ausgeschriebenen Vornamens:

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

articles_in_portlet
^^^^^^^^^^^^^^^^^^^

Im Portlet "Current Issue": Sollen die Artikel aufgelistet werden? Sonst
escheint nur ein Link auf die Ausgabe, evtl. mit Bild.

Default::

    True

authors_in_portlet
^^^^^^^^^^^^^^^^^^

Im Portlet "Current Issue": Sollen auch die Autoren gelistet werden?

Default::

    True


allow_persistent_discussion
^^^^^^^^^^^^^^^^^^^^^^^^^^^
volume_show_covers
^^^^^^^^^^^^^^^^^^
issue_show_abstracts
^^^^^^^^^^^^^^^^^^^^
issue_show_pdf_link
^^^^^^^^^^^^^^^^^^^
issue_show_full_abstracts
^^^^^^^^^^^^^^^^^^^^^^^^^
issue_show_short_citation
^^^^^^^^^^^^^^^^^^^^^^^^^
issue_sort_on
^^^^^^^^^^^^^
issue_sort_order
^^^^^^^^^^^^^^^^
discussion_time
^^^^^^^^^^^^^^^
fedora_time_format
^^^^^^^^^^^^^^^^^^
issue_date_format
^^^^^^^^^^^^^^^^^
recent_articles_range 
^^^^^^^^^^^^^^^^^^^^^

dippreview_properties (DiPPReview properties)
---------------------------------------------


member_properties (Extended member properties)
----------------------------------------------

metadata_properties (QDC Metadata properties)
---------------------------------------------
