README.txt
==========

    Connect Plone to the fedora repository

Requirements

    Tested with Zope 2.7 and Plone 2.5
    
Dependencies

    The following Plone products are required:

        CMFOpenflow
        TextIndexNG3
        ATVocabularyManager
        LinguaPlone
        PloneLanguageTool
    
    Python Modules
        bibliograph.core
        setuptools
        dipp.tools
        dipp.dipp2
        
        dipp.fedora2 >= 2.2
        └─dipp.dipp3 >= 3.2
          └─ZSI

Installation

    Running 
    easy_install -f http://alkyoneus.hbz-nrw.de/dist <Python Module Name>
    
Configuration

    set Server IP and port on the fedora Tool in the zmi
        