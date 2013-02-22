Changelog
=========

DiPP 2.11 (not yet released)
    * moved all DiPP relavant properties from the ZMI root to 
      dipp_properties. Running moveProps.py script is required
    * deadline code moved to a tool, ext-Folder with external methods 
      is now obsolete and can be deleted
    * some permission fixed for CMFOpenflow
    * easier to go back to a previous version of a datastream
    * fixed abstract encoding in rss feed

DiPP 2.10 (2012-10-12)
    * added Sphinx based documentation
    * proper use of interfaces
    * ContentTypes moved to content folder
    * generic profiles  for most installations
    * event subscriber
    * use of Products.DiPP nested namespace for propper "eggification"
    * Fedora server configuration taken from dipp.fedora2 module, no 
      extra configuration in Plone
    * lots of code cleanup and docstrings

DiPP 2.9.9 (2012-04-19)
    * added PID resolver
    
DiPP 2.9.8 (2012-04-04)
    * fixed problems with link_translations_form
        
DiPP 2.9.7 (2012-04-02)
    * Fixed some problem with versioning of XML streams

DiPP 2.9.7 (2012-04-02)
    * unreleased    

DiPP 2.9.5 (2012-03-12)
    * Publishing (openflow) workflow: fixed permission problems and error
      in imprimatur mail
    * recommendet citation: order first and lastname
    * roles and persmissions as generic setup

DiPP 2.9.5 (2012-03-13)
    * unreleased 

DiPP 2.9.4 (2012-01-19)
    * fileupload not limited to pdf or jpg, not so strict check of MIME Type
    * ISSN search via aquisition, thus more flexible with multiple ISSNs 

DiPP 2.9.3 (2011-10-20)
    * fixed type error when adding files to submission
    * default title in metadata
    * new login_succes page with rolebased links
    * pdf automatically declared as fulltext when pdf only publishing

DiPP 2.9.2 (2011-10-11)
    * more flexible bibliographic citation (APA style possible)
    * short bibl. citation on issue index page

DiPP 2.9.1 (2011-10-10)
    * SpecialIssue from DiPPContent included, Dependency from DiPPContent
      removed. Should be deinstalled before reinstalling DIPP
    * pdf link on issue index page

DiPP 2.9 (2011-09-28)
    * Merged with DiPPReview
    * more than one ISSN possible
    * Better support for classified subjects, JEL added
    * Zählpixel in HTML and in PDF-Icon (document_actions)

DiPP 2.8.1 (2011-07-20)
    * neutral language first in first workflow step, help texts
    * fixed: paper does not appear in worklist, when authorname has strange
      characters

DiPP 2.8 (2011-07-18)
    * IssueDate as DateIndex. Remove getIssueDate before Installation  to force
      recreation of index. reindex
    * jquery UI, used for DiPPReviews overlay effects
    * dipp_sections tool, will soon replace vocabularybased section, since
      it integrates in LinguaPlone

DiPP 2.7.2 (2011-06-29)
    * Fedora2DiPP3 tool folderish. Articles for storing in the repository
      are temporarily kept here insteat in fedora_tmp folder
    * Enhanced translation of articles: i.e. english and german version can
      be in the same folder, not necessarily the translated parent folder
    * advanced search even more enhanced
    * GND Connection included, but not activated
    * created, modified and valid dates replaced with published, submitted
      (needs still some fix for reading back)

DiPP 2.7.1 (2011-04-21)
    * articlesearch shows short bibligraphic citation
    * Licence defaults to englisch, when other language than en or de is
      selected

DiPP 2.7 (2011-04-18)
    * new dependency: python egg dipp.tools
    * After Install: call synchronize Skript to put the URN into plones catalog
    * fedoratool shows status of URN
    * fixed some problems when indexing pdfs
    * new main_template for workflow related pages. only left column is
      visible and not modified by left_slot
    * new articlesearch_form, not active yet
    * feeds und search in robots.txt disabled for performance reasons
    * new template for recent article with section drilldown (logistics)
    * normalized rtf filenames, upload of files with strange filenames now
      possible
    * zlog replaced with logger

DiPP 2.6.4 (2011-03-23)
    * fixed broken pdf link in html version of article
    * adding new keywords when uploading articles fixed

DiPP 2.6.3 (2011-03-22)
    * "titel" attribute (ZMI) of workflow instance removes to prevent trouble
      with special characters
    * add basis for a "DiPPManagementTool" which allows checking and 
      installing of products in all journals of a zopeinstance

DiPP 2.6.2 (2011-03-10)
    * portlet for ISSN 
    * recent_articles shows only articles of the last 30 days (configurable)
    * Metadata: keywords as checkboxes to allow easier selection 
    * minor i18n and css corrections
    * bypass webservice when uploading rtf. This might solve the timeout
      problems  

DiPP 2.6.1 (2011-02-24)
    * edit journal sections in the Metadataform   

DiPP 2.6 (2011-02-24)
    * adding pagenumbers also in the metadata form possible
    * Metadata form: finally a cancel button plus a few refined translations
    * Colored Differences between version of an article

DiPP 2.5.5 (2011-02-14)
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
      items articleobject has been deleted. Needs the PID to be catalogued. Using
      with plone 2.0 requires manuell adding of PID index

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
      replaces by PID and label configurable directly in the fedora tool.  For new
      Installations t has to be done manually, for upgrades from Version <2.4 a
      script mig23to24 is provided
    * Editing of FedoraDocuments simplified, less templates needed FedoraMultimedia
    * fetches content/datastream directly from fedora, not
      via webservice, to improve performance

DiPP 2.3.6 (2010-05-27)
    * TextIndexNG3 used to index PDFs (requires reindexing of portal_catalog
      and converting existing indexes, see Products Readme)