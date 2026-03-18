Content Types
#############

Alle Inhaltstypen basieren auf dem Archetype Framework.

Artikel
*******

Ein Artikel ist ein Ordner vom Typ FedoraArtikel, der die einzelnen Bestandteile
wie Texte, Bilder und Zusatzmaterialien aufnimmt.

.. autoclass:: Products.DiPP.content.fedoraarticle.FedoraArticle
    :members: indexableContent, syncMetadata, getPublishedArticles,
              getFulltextPdf, linkTranslations

.. autoclass:: Products.DiPP.content.fedoradocument.FedoraDocument
    :members: make_working_copy 

.. autoclass:: Products.DiPP.content.fedoramultimedia.FedoraMultimedia
    :members: reindex_article, at_post_create_script, at_post_edit_script, indexableContent, index_html, preview, getTypeOfList

.. autoclass:: Products.DiPP.content.fedoraxml.FedoraXML


Hierarchische Objekte
*********************

.. autoclass:: Products.DiPP.content.fedorahierarchie.FedoraHierarchie
   :members: at_post_create_script, migrate

.. autoclass:: Products.DiPP.content.volume.Volume
   :members: at_post_create_script

.. autoclass:: Products.DiPP.content.issue.Issue
   :members: at_post_create_script

.. autoclass:: Products.DiPP.content.specialissue.SpecialIssue
   :members: getSubjects

