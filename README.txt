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
	
	Version 2.7 required a "synchronize" run, since the urn is now in the portal_catalog

Configuration

    Some Parameters in portal_properties/dipp_properties:
    
    show_recommended_citation -- Toggles the paragraph holding the recommended 
    citation on and off
    
    initials_only -- Firstnames only as initials
    
    initials_period -- Period after initial on or off
    
    comma_separated -- comma between authors first and lastname
    
    citation_format -- formatting string, 
    defaults to %(authors)s (%(year)s). %(title)s. %(journal)s, Vol. %(volume)s. (%(urn)s)
    
    short_citation_format -- %(journal)s, Vol. %(volume)s, Iss. %(issue)s. Used in Feeds
    
    issue_show_abstracts -- Show only first  160 charakters of abstract in issue view (search_results_description_length
	)
    
    issue_show_full_abstracts -- Show full word of abstract in issue view
	
    articles_in_portlet -- latest issue portlet: show section only or include articles
    
    authors_in_portlet -- latest issue portlet: include authors
    
    volume_show_covers -- show issue covers in volume
    
    recent_articles_range -- age of oldest article to include in recent_article
    