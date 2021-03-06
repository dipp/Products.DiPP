dipp_properties (DiPP properties)
*********************************

enthält Konfigurationen, die das Erscheinungsbild von Ausgaben und
Artikeln beeinflussen.

.. toctree::
   :maxdepth: 2


.. _prop_issn:

ISSN
====

Die *International Standard Serial Number*. Kann mit erscheinen der ersten Artikel
bei der Deutschen Nationalbibliothek beantragt werden.

.. _prop_alertEmailAddresses:

alertEmailAddresses
===================
Eine Liste mit E-Mail Adressen, die bei Veröffentlichung eines Artikel
benachrichtigt werden.

Default::

    dipp@hbz-nrw.de

.. _prop_alertEmailText:

alertEmailText
==============
Text dieser Email::

    Das Journal "%(journal)s" hat einen neuen Artikel veröffentlicht:
    %(citation)s

    URL: %(url)s
    DataCite XML: %(url)s/metadata/datacite


Zur Verfügung stehende Platzhalter:

========= =======================================
Name      Bedeutung
========= =======================================
journal   Name des journals
url       URL des Artikels
citation  Bibliographischen Zitat des Artikels
========= =======================================


citation_format
===============
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
=====================
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
journal_shortname  Abkürzung des Journals, siehe :ref:`prop_journalname_abbr`
volume             Jahrgang
issue              Ausgabe
startpage          erste Seite (bei PDF)
endpage            letzte Seite (bei PDF)
year               Jahreszahl, wird aus den Datum der Veröffentlich extrahiert
issuedate          Datum der Veröffentlichung
urn                Der URN
================== ============================================================


.. _prop_issue_date_format:

issue_date_format
=================

Formatierung des Ausgabendatums in Listen aller Ausgaben. http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

Default::

    %b %Y


.. _hide_current_issue:

hide_current_issue
==================

Bestimmt, ob die aktuelle Ausgabe im all_issues Template angezeigt werden soll. Bei Verwendung eines currentissue
Links kann das evtl. sinnvoll sein.

Default::

    False


show_recommended_citation
=========================
Soll unterhalb des Artikels das bibliographische Zitat angezeigt werden?

Default::

    True

show_classified_subjects
========================
Sollen im Artikelkopf die normierten Schlagworte angezeigt werden?

Default::

    False

show_review_history
===================
Sollen im Artikelkopf die Daten für Einreichung und Annahme angezeigt werden?

Default::

    False

initials_only
=============
Im bibliographischen Zitat: Sollen bei den Autoren nur die Initialen angezeigt
werden statt des ausgeschriebenen Vornamens:

Default::

    False

firstnamefirst
==============
Im bibliographischen Zitat: Sollen erst die Vornamen angezeigt werden?

Default::

    False

initials_period
===============
Im bibl. Zitat: Sollen ein Punkt hinter die Initialen?

Default::

    False

comma_separated
===============
Im bibl. Zitat: wenn der Vorname nach dem Nachnamen kommt (firstnamefirst =
false), sollen sie durch ein Komma getrennt werden:

Default::

    False

last_author_suffix
==================
Im  bibl. Zitat: wenn der letzte Autor z.B. durch ein 'und' abgetrennt werden
soll.

Default::

    <leer>

.. _prop_articles_in_portlet:

articles_in_portlet
===================
Im Portlet "Current Issue": Sollen die Artikel aufgelistet werden? Sonst
escheint nur ein Link auf die Ausgabe, evtl. mit Bild.

Default::

    True

.. _prop_authors_in_portlet:

authors_in_portlet
==================
Im Portlet "Current Issue": Sollen auch die Autoren gelistet werden?

Default::

    True


.. _allow_persistent_discussion:

allow_persistent_discussion
===========================
Wenn True, wird unterhalb eines Artikels eine Liste mit Kommentaren und ein Link
zum Einreichen eines eigenen Kommentares eingeblendet. Kommentare sind
ihrerseits wieder begutachtete Artikel.

Default::

   False


.. _prop_volume_show_covers:

volume_show_covers
==================
Wenn True, werden auf der Inhaltsseite der Jahrgänge die Titelseiten der
Ausgaben angezeigt, soweit vorhanden.

Default::

   False

issue_show_abstracts
====================
Wenn True, werden auf der Inhaltsseite der Ausgaben die verfügbaren Abstracts
der Artikel verlinkt.

Default::

   False

issue_show_full_abstracts
=========================
Wenn True, werden auf der Inhaltsseite der Ausgaben die Abstracts in voller
Länge angezeigt.

Default::

   False

issue_show_pdf_link
===================
Wenn True, werden auf der Inhaltsseite der Ausgaben vorhandene PDFs direkt
verlinkt.

Default::

   False

issue_show_short_citation
=========================
Wenn True, werden auf der Inhaltsseite der Ausgaben zu den Artikeln das
bibligraphische Zitat in Kurzform angezeigt, siehe
:ref:`prop_short_citation_format`

Default::

   False

issue_sort_on
=============
Bestimmt auf der Inhaltsseite der Ausgaben, wonach die Artikelliste sortiert
werden soll. Möglich sind alle sortierbaren Attribute der Artikel, z.B.
getIssue, getIssueDate, getVolume, getObjPositionInParent. Letzteres ermöglicht
eine manuelle Sortierung, die Reihenfolge im Elternorder (Ausgabe) übernommen
wird.

Default::

   getObjPositionInParent

issue_sort_order
================
Aufsteigende (ascending) oder absteigende (reverse) Sortierung der Artikel

Default::

   ascending

discussion_time
===============
(wird nicht verwendet)

fedora_time_format
==================
String um die Fedorazeitstempel im ZMI lesbarer anzuzeigen. Sollte eigentlich
niemals geändert werden müssen.

Default::

   %Y-%m-%dT%H:%M:%SZ

issue_date_format
=================
Wenn nicht leer, wird das Datum auf der Ausgabenseite mit dem hier angegebenen
String formatiert. Wenn leer, wird auch kein Datum angezeigt.

Default::

   <leer>

.. _prop_recent_articles_range:

recent_articles_range
=====================
Alter (in Tagen) des ältesten Artikels der durch das recent_article Template
angezeigt werden soll.

Default::

   30


.. _prop_deepest_toc_level:

deepest_toc_level
=================

Die niedrigste Überschriftenebene, die im  :ref:`portlet_autotoc` Inhaltsverzeichnis (TOC) des Artikels noch
angezeigt werden soll. Es ist zu beachten, dass die erste Ebene h2 ist. Um die
ersten drei Ebenen anzuzegen, muss der Wert auf 4 gesetzt werden. Der globale Wert
kann auf für einen einelnen Artikel überschrieben werden, wenn im ZMI eine entsprechend
benannte Property angelegt wird. Das TOC wird aktualisiert, wenn vom Artikel eine neue
Version angelegt wird.

Default::

    6

.. _prop_awstats_id:

awstats_id
==========

Wenn der Name der AWStats Konfigurationsdatei "awstats.ejournal.conf" lautet, ist die
awstats_id "ejournal" Daraus ergeben sich dann die geparsten Logfiles zu z.B
"awstats112011.ejournal.txt" Daraus werden dann die Zugriffstatistiken einzelner Artikel
bzw. Artikeldateien generiert.

Default::

   <leer>


.. _enable_ebookey:

enable_ebookey
==============

Zeige unter Volltext einen Link zur per `ebookey <https://github.com/Raul-Vasi/ebookey>`_ erzeugten epub-Version des Artikeln.

Default::

    False


.. _orcid_cli:

orcid_cli
=========


.. _twitter_username:

twitter_username
================

Benutzername bei twitter, ohne führendes @:

Default::

    <leer>



.. _sharing_image:

sharing_image
=============

Name des Bildes, das für Twittercards bzw. OpenGraph verwendet werden soll. das
Bild muss separat z.B. im custom-Ordner abgelegt werden. Wenn nichts angegeben
wird, wird das Logo der Website verwendet (logoName).

Default::

    <leer>


.. _thumby_url:

thumby_url
==========

URL des Thumbnailer Webservices `Thumby <https://github.com/hbz/thumby>`_

Default::

    https://api.edoweb-test.hbz-nrw.de/tools/thumby


.. _thumby_size:

thumby_size
===========

Größe des Thumbnails in px.

Default::

    https://api.edoweb-test.hbz-nrw.de/tools/thumby
