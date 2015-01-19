Portlets
########


.. _portlet_toc:

Inhaltsverzeichnis ``portlet_toc``
**********************************

Stellt das das generierte Inhaltsverzeichnis *toc_html* dar. 
Das Inhaltsverzeichnis wird bei der Konvertierung einmalig automatisch generiert
und nicht aktualisiert, wenn z.B. ein Tippfehler im HTML korrigiert wird.
Wird nur bei Artikeln eingeblendet.

.. _portlet_autotoc:

Automatisches Inhaltsverzeichnis ``portlet_autotoc``
****************************************************

Bindet das mit jeder Versionierung des Artikels aktualisierte Inhaltsverzeichnis
ein. Zur Konfiguration siehe :ref:`prop_deepest_toc_level`


.. _portlet_currentissue:

Aktuelle Ausgabe ``portlet_currentissue``
*****************************************

Eine Auflistung der Artikel der aktuellen Ausgabe. Wenn der Ausgabe ein Titelbild
beigefügt wurde, wird dieses verkleinert dargestellt. Auch eine Sortierung nach
Sektionen wird vorgenommen. Weitere Konfiguration ist durch folgende Properties
möglich: :ref:`prop_articles_in_portlet`, :ref:`prop_authors_in_portlet`.

.. _portlet_dippnav:

DiPP Navigation ``portlet_dippnav``
***********************************

Kleine navigation mit Links zur "Editoral Toolbox", dem Plone Setup und dem
sog. "Website Manager", der nicht anderes ist als die Inhaltsansicht der
obersten Verzeichnisebene.  


.. _portlet_editorialtoolbox:

Editorial Toolbopx ``portlet_editorialtoolbox``
***********************************************

Siehe eigene Seite: :ref:`editorial_toolbox`.

.. _portlet_feeds:

Feeds ``portlet_feeds``
***********************

Dieses Portlet enthält eine Liste der verfügbaren :term:`RSS`-Feeds. Ein Feed
mit allen veröffentlichen Artikeln steht immer zur Verfügung, wenn die Artikel 
noch in einzelne Sektionen eingeordnet werden, stehen auch seperate Feeds hierfür
zum abonnieren bereit.


.. _portlet_issn:

ISSN ``portlet_issn``
*********************

Ein Portlet, das einfach  nur die ISSN-Nummer wiedergibt. Sie muss in
den dipp_properties angegeben werden, siehe :ref:`prop_issn`.

.. _portlet_newsletter:

Newsletter ``portlet_newsletter``
*********************************

Ein Portlet, das eine Anmeldemaske für einen Newsletter anbietet. Erfordert die 
Installation und Konfiguration des PloneGazette Produktes.

.. _portlet_recentarticles:

Aktuelle Artikel ``portlet_recentarticles``
*******************************************

Chronologische Aufzählung der letzten fünf Artikel, Sektionen und
:ref:`prop_authors_in_portlet` werden ausgewertet. 

.. _portlet_search:

Suche ``portlet_search``
************************

Alternative Positionierung der Suchmaske.

