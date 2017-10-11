metadata_properties (QDC Metadata properties)
*********************************************

einige Standardwerte für die Qualifizierten Dublin Core Metadaten.

.. _prop_journalname:

journalname
===========

.. _prop_journalname_abbr:

journalname_abbr
================

Kurzform des Journalnamens. Kann zum Beispiel in der kurzen Version der Zitierweise
angewendet werden, z.B. JOE statt Journal of Examples.

Default::

    <leer>

.. _prop_publisher:

publisher
=========

.. _prop_issn:

issn
====

.. _prop_doi_prefix:

doi_prefix
==========

Prefix für alle vergebenen DOI. DOIs bestehen aus einem internen Suffix und
einem von einem Provider wie CrossRef oder der TIB vergebenen Prefix, das
üblicherweise die Form `10.xxxx` hat. `10.5072` ist ein spezieller Testprefix.

Ohne Angabe des Prefix steht das entsprechende Feld im Metadatenformular nicht
zur Verfügung.

Default::

    <leer>


.. _prop_default_pubType:

default_pubType
===============

Default::

    article

.. _prop_default_docType:

default_docType
===============

Default::

    text

.. _prop_default_language:

default_language
================

.. _prop_available_languages:

available_languages
===================

Default::

    ger
    eng
    fra
    ita
    spa
