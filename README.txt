Overview

    Connect Plone to the fedora repository

Requirements

    Tested with Zope 2.7 and Plone 2.5
    
Installation

	Note: Before installing DiPP product version 2.4, the fedora tool has to be
    deleted from the ZMI. After reinstalling  the configuration
	for fedora has to be manually adjusted, i.e. pid and label must be specified
	on the fedora tool itself, not in the root properties. Otherwise new articles 
	can not be uploaded. 

Changes
    
    DiPP 2.4.5 (2010-07-28)

        * worklist makes ist easer to spot workitems which can be deleted because the
          items articleobject has been deleted. Needs the PID to be catalogued. Using with
          plone 2.0 requires manuell adding of PID index

    DiPP 2.4.4 (2010-07-23)

        * icons for metadata/citation and fulltext pdf as document_action implemented
        
        * author page: in a case a contributor also has an account, the profile is shown

    DiPP 2.4.3 (2010-07-12)
		
		* new alphabetic list of authors, grouped by initial
        
		* cleanup and minor bugfixes
	
    DiPP 2.4.2 (2010-06-30)
	
		* Bugfixes: corrected use of volume/issue in COinS
		
    DiPP 2.4.1 (2010-06-29)

        * COinS/Zotero support added, requires python module openurl
        
        * worklist: show PID of the article, user 'dippadm' can now        
          easily delete workitems from the list. 
          
        * nicer abstract_view
	
    DiPP 2.4 (2010-06-22)
	
		* include the tools PloneFedora2DiPP2 and PloneFedora2DiPP3 replacing
		  two seperate products. PloneFedora2DiPP3 is automatically installed
          
		* finally removing root properties GAP_CONTAINER and label. These are
		  replaces by PID and label configurable directly in the fedora tool. 
          For new Installations t has to be done manually, for upgrades from Version <2.4
          a script mig23to24 is provided
          
		* Editing of FedoraDocuments simplified, less templates needed
        
		* FedoraMultimedia fetches content/datastream directly from fedora, not
		  via webservice, to improve performance
		  
    DiPP 2.3.6 (2010-05-27)
	
	    * TextIndexNG3 used to index PDFs (requires reindexing of portal_catalog
          and converting existing indexes, see Products Readme)
