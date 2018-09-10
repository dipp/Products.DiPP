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

* dipp.dipp3>=3.9

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
Install Python 2.4

.. code-block:: bash

    $ wget https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tar.bz2

Edit Modules/Setup.dist at about line 206 to enable `SSL Support`_:

.. code-block:: bash

    # Socket module helper for socket(2)
    _socket socketmodule.c

    # Socket module helper for SSL support; you must comment out the other
    # socket line above, and possibly edit the SSL variable:
    #SSL=/usr/local/ssl
    SSL=/usr
    _ssl _ssl.c \
    -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
    -L$(SSL)/lib -lssl -lcrypto




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

Installation of `Setupools`_ by dowloading the sourcecode. The old method via ez_setup
seems not work anymore:

.. code-block:: bash

    $ wget https://github.com/pypa/setuptools/archive/0.6.tar.gz

Installation of `Virtualenv`_ Version 1.7.2. That is the latest version that still works
with  Python 2.4

.. code-block:: bash

        $ wget https://files.pythonhosted.org/packages/16/86/7b88d35d0a353ec70e42aa37fd8b0bd1c643419c80f022ffaafa4d6449f0/virtualenv-1.7.2.tar.gz

Configuration
-------------

The configuration has to be done in both the filesystem and Zope.
The two configuration files:

`/files/etc/dipp3.cfg`:

.. code-block:: ini

    [webservice]
    address: http://alkyoneus.hbz-nrw.de:9180/dipp3/services/dipp
    timeout: 120

`/files/etc/fedora2.cfg`:

.. code-block:: ini

    [webservice]
    address: pythia.hbz-nrw.de
    port: 9280
    login: fedoraAdmin
    password: topsecret

Set Serveraddress and port on the fedora Tool in the ZMI


.. _SSL Support: https://techglimpse.com/install-python-openssl-support-tutorial/
.. _Setuptools: https://github.com/pypa/setuptools
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/
