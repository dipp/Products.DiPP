Product.DiPP
============

Connect Plone to the fedora repository
Tested with Zope 2.7 and Plone 2.5
    
Dependencies
------------

The following Plone products are required:

* CMFOpenflow
* TextIndexNG3
* ATVocabularyManager
* LinguaPlone
* PloneLanguageTool
    
Python Modules

* setuptools

* dipp.tools

  * argparse
  * lxml==2.3.5
  * BeautifulSoup==3.2.1
  
* dipp.dipp3
   
  * argparse
  * dipp.tools>=0.5.1
  * elementtree
  * bibliograph.core
  * dipp.fedora2
  * ZSI>=2.0.1

* dipp.fedora2

  * ZSI>=2.0.1

* ZSI>=2.0.1

  * PyXML >= 0.8.3

* dipp.datacite
* dipp.awstats

Installation
------------

The Python modules are installed by running:

.. code-block:: bash

    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v bibliograph.core
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v PyXML
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v ZSI
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v dipp.tools
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v dipp.fedora2
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v elementtree
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v dipp.dipp3
    $ easy_install -f https://alkyoneus.hbz-nrw.de/dist -v dipp.datacite

    
Configuration
-------------

The configuration has to be done in both the filesystem and Zope.
The two configuration files: 

`/files/etc/dipp3.cfg`:  

.. code-block:: ini

    [webservice]
    address: http://127.0.0.1:9180/dipp3/services/dipp
    timeout: 120

`/files/etc/fedora2.cfg`:

.. code-block:: ini

    [webservice]
    address: 193.30.112.98
    port: 9280
    login: fedoraAdmin
    password: topsecret

set Server IP and port on the fedora Tool in the zmi
        
