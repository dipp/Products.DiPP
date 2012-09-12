Content Types
=============

Alle Inhaltstypen basieren auf dem Archetype Framework.

Artikel
-------

Ein Artikel ist ein Ordner vom Typ FedoraArtikel, der die einzelnen Bestandteile
wie Texte, Bilder und Zusatzmaterialien aufnimmt.

.. autoclass:: Products.DiPP.content.fedoraarticle.FedoraArticle
    :members: indexableContent, syncMetadata, getPublishedArticles,
              getFulltextPdf, linkTranslations

.. autoclass:: Products.DiPP.content.fedoradocument.FedoraDocument

.. autoclass:: Products.DiPP.content.fedoramultimedia.FedoraMultimedia

.. autoclass:: Products.DiPP.content.fedoraxml.FedoraXML


Hierarchische Objekte
---------------------

.. autoclass:: Products.DiPP.content.fedorahierarchie.FedoraHierarchie
   :members: at_post_create_script

.. autoclass:: Products.DiPP.content.volume.Volume
   :members: at_post_create_script

.. autoclass:: Products.DiPP.content.issue.Issue
   :members: at_post_create_script

.. autoclass:: Products.DiPP.content.specialissue.SpecialIssue
   :members: getSubjects

