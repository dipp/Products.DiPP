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
  * dipp.tools>=0.7.1
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

Plone 2.5.5 still requires Python 2.4, which is usually not available in the
repositories anymore and thus has to be compiled. Since each Zopeinstance should
have its own Python interpreter, we install a master python in /opt and use
virtuelenv for each Zopeinstance. Get Python:

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

Configure and compile:

.. code-block:: bash

    $ ./configure --prefix=/opt/python24
    $ make
    $ make install


Installation of `Setupools`_ by dowloading the sourcecode. The old method via ez_setup
seems not work anymore:

.. code-block:: bash

    $ wget https://github.com/pypa/setuptools/archive/0.6.tar.gz

Installation of `Virtualenv`_ Version 1.7.2. That is the latest version that still works
with  Python 2.4

.. code-block:: bash

    $ wget https://files.pythonhosted.org/packages/16/86/7b88d35d0a353ec70e42aa37fd8b0bd1c643419c80f022ffaafa4d6449f0/virtualenv-1.7.2.tar.gz
    $ tar -xzvf virtualenv-1.7.2.tar.gz
    $ cd virtualenv-1.7.2
    $ /opt/python24/bin/python setup.py install

Creating and activating a virtual envirement in /srv/zope/dipp:

.. code-block:: bash

    $ /opt/python24/bin/virtualenv /srv/zope/dipp/Python-2.4
    $ . /srv/zope/dipp/Python-2.4/bin/activate

Setting the correct encoding in site.py (~row 525):

.. code-block:: python

    # encoding = "ascii" # Default value set by _PyUnicode_Init()
    encoding = "utf-8" # 2018-10-09 Rm

Install Zope.

.. code-block:: bash

    $ ./configure --with-python=/srv/zope/dipp/Python-2.4/bin/python --prefix=/srv/zope/dipp/Zope-2.9

Dedicated User 

.. code-block:: bash

    $ useradd -M -U -s /sbin/nologin -u 60000 -d /srv/zope -c "Zope damon" zope

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



.. _SSL Support: https://techglimpse.com/install-python-openssl-support-tutorial/
.. _Setuptools: https://github.com/pypa/setuptools
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/
