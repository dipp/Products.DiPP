README.txt
==========

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
    * elementtree
    * bibliograph.core
    * dipp.tools >= 0.4
    * dipp.dipp2
    * dipp.fedora2 >= 2.2
    * dipp.dipp3 >= 3.3.1
    * ZSI

our own Modules

    * dipp.tools

        * argparse

    * dipp.dipp3
       
        * argparse
        * dipp.tools
        * elementtree
        * bibliograph.core
        * ZSI

    * dipp.dipp2
        
        * ZSI

    * dipp.fedora2

        * dipp.dipp3

    * ZSI

        * PyXML

    * dipp.datacite

    * dipp.awstats

Installation
------------

The Python modules are installed by running::

    easy_install -f http://alkyoneus.hbz-nrw.de/dist -U <Python Module Name>

for each module. dipp.dipp3 and ZSI are automatically pulled in as dependency of dipp.fedora2
    
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
        
