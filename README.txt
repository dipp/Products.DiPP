Overview

    Connect Plone to the fedora repository

Requirements

    Tested with Zope 2.7 and Plone 2.5
    
Installation

	Note: after reinstalling the DiPP product version 2.4 the configuration has
	for fedora has to be manually adjusted, i.e. pid and label must be specified
	on the fedora tool itself, not in the root properties. Otherwise new articles 
	can not be uploaded.

Changes
	
	DiPP 2.4 (2010-06-22)
	
		* include the tools PloneFedora2DiPP2 and PloneFedora2DiPP3 replacing
		  two seperate products. PloneFedora2DiPP3 is automatically installed
		
		* finally removing root properties GAP_CONTAINER and label. These are
		  replaces by PID and label configurable directly in the fedora tool
		  
		* Editing of FedoraDocuments simplified, less templates needed
		
		* FedoraMultimedia fetches content/datastream directly from fedora, not
		  via webservice, to improve performance
		  
	DiPP 2.3.6 (2010-05-27)
	
	    * TextIndexNG3 used to index PDFs