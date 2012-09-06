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

Default::

    %(authors)s (%(year)s). %(title)s. %(journal)s, Vol. %(volume)s. (%(urn)s)


short_citation_format
^^^^^^^^^^^^^^^^^^^^^

Default::

    %(journal)s, Vol. %(volume)s, Iss. %(issue)s

show_recommended_citation
^^^^^^^^^^^^^^^^^^^^^^^^^
show_classified_subjects
^^^^^^^^^^^^^^^^^^^^^^^^
show_review_history
^^^^^^^^^^^^^^^^^^^
initials_only
^^^^^^^^^^^^^
firstnamefirst
^^^^^^^^^^^^^^
initials_period
^^^^^^^^^^^^^^^
comma_separated
^^^^^^^^^^^^^^^
last_author_suffix
^^^^^^^^^^^^^^^^^^
articles_in_portlet
^^^^^^^^^^^^^^^^^^^
authors_in_portlet
^^^^^^^^^^^^^^^^^^
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
