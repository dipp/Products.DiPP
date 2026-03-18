site_properties
***************

Hierbeit handelt es sich um Plones Standard Propertysheet, in dem auch die allgemeiner Konfiguration
gespeichert wird. Da die Konfiguration des Trackings nicht Dipp spezifisch ist, wurde sie ebenfalls
hier hinterlegt.


.. _analytics_id:

analytics_id
============

Matomo ID der Website. Kann dem Tracking-Code in den Matomoeinstellungen entnommen werden.
Obwohl die ID immer ein ganzzahliger Wert ist, wird er hier als String hinterlegt

Default::

    <leer>


.. _analytics_server:

analytics_server
================

URL des Servers, auf dem die Matomoinstallation läuft. Im DiPP Zusammenhang wird das
aktuell alkyoneus.hbz-nrw.de/piwik oder porphyrion.hbz-nrw.de/piwik sein

Default::

    <leer>


.. _analytics_javascript:

analytics_javascript
====================

JavaScript-Tracking-Code für Matomo wird in jeder Seite über das webstats Makro eingebunden.
Das gleichnamige Pagetemplate enthält auch die javascriptfreie Trackingvariante über ein Bild.
Die Variablen %s werden durch :ref:`analytics_id` bzw :ref:`analytics_server` ersetzt.

Default::

    var _paq = _paq || [];
    /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
        var u="//%s/";
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['setSiteId', '%s']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
        g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
    })();

.. _analytics_javascript_notfound:

analytics_javascript_notfound
=============================

JavaScript-Tracking-Code für Matomo wird in jeder Seite über das webstats Makro eingebunden.
Die Variablen %s werden durch :ref:`analytics_id` bzw :ref:`analytics_server` ersetzt.
Dies ist ein `spezieller Trackingcode <https://matomo.org/faq/how-to/faq_60/>`_, der nur für 404 Seiten verwendet wird.


Default::

    var _paq = _paq || [];
    /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
    _paq.push(['setDocumentTitle',  '404/URL = ' +  encodeURIComponent(document.location.pathname+document.location.search) + '/From = ' + encodeURIComponent(document.referrer)]);
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
        var u="//%s/";
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['setSiteId', '%s']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
        g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
    })();
