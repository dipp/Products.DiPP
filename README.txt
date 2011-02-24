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

    DiPP 2.6 (2010-02-24)
    
    	* adding pagenumbers also in the metadata form possible
    	
    	* Metadata form: finally a cancel button plus a few refined translations
    	
    	* Colored Differences between version of an article
    	
    	
    DiPP 2.5.5 (2010-02-14)

        * After Install: call synchronize Skript to put the JournalIssueDate and
          Authors into plones catalog
        
        * recent articles: batched list with section support
        
        * workflow: templates as controller page templates with cancel button, 
          Title and PID on every page
        
        * my_worklist and all_worklist unified
        
        * licence is now a macro and used in mixed_view and fedoradocument_view
        
        * pdf indexed together with article folder: found pdf in search result
          now has url of articlefolder/splashpage
        
        * jQuery used to display references as tooltips 
        
	
    DiPP 2.5.4 (2010-11-29)
        
        * Fulltext with size
        
        * issue sorting (by date, by position) configurable via ZMI
        
        * DOI/URN linked with resolver
        
        * date in issue configurable

        
    DiPP 2.5.3 (2010-11-18)
	
		* default view of articles configurable (fulltext for converted articles,
		  mixed_view for pdf only publications)
		
		* better linguaplone support for FedoraArticles. Tranlations can easily
		  be linked after the conversion via the editorial toolbox
		
		* more dummy metadata for temp. conversions. Citation and metadata views
		  can be rendered now


    DiPP 2.5.2 (2010-10-22)
	
	    * Feeds as alternate content in header of some templates (icon in
	      firefox address bar)
	    
	    * Feeds optional contain a short bibliographic citation
	    
	    * portlet and dedicated template for recent articles 
	    
	    * journalIssueDate in sync with Plones effective date
	    
	    
    DiPP 2.5.1 (2010-10-08)
	
		* authors/contributors indexed and searchable
		
		* feeds: dedicated page and portlet
		
		* article template to replace the authorblurb from the docbook
		
		* minor bugfixes
	
    DiPP 2.5 (2010-09-30)
	
		* New Contenttype Issue and Volume, which are identical with
		  FedoraHierachie, just another name. Existing Issues/volumes, made with 
		  FedoraHierachies can be migrated, but don't need to.
		
		* feeds include now the abstract, which requires running of the synchronize
		  script, since the abstract stored in fedora has to be made available in the
		  FedoraArticle contenttype
		
		* Hierarchien, Issues, Volumes linguaplone aware.  

    DiPP 2.4.10 (2010-09-08)
    
    	* ZMI: fedora manage tab for articles. Currently  allows direct read 
    	  access to datastreams and versions of the xml datastreams (DC, 
    	  RELS-EXT,...) of the DiPP:article object  
    	
    DiPP 2.4.9 (2010-09-02)
    
    	* beginning support for default metadata and configurable meadata form
    	  (not complete yet, required removing fedora tool before updating. remember
    	  to add label and pid again)    	  
    	
    	* Use of PyRRS2Gen for feeds started
    	
    	* issues and volume show only content of current navigation level
    	
    	* fixed minor design flaws
    	
    DiPP 2.4.8 (2010-08-25)

		* show metadata/citation as tabs to make the page more compact
		
		* citation downloadable for better integration with Endnote, Zotero,... 
		
    DiPP 2.4.7 (2010-08-24)
    	
    	* citation formats with bibutils: Endnote, Bibtex,...
    	
    	* bibutils needs to be installed and in the path
    	
    	* bibliograph python modules are required

    DiPP 2.4.6 (2010-07-28)
    
        * direct access to fedora bypassing the webservice also for indexing pdf 
        
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
