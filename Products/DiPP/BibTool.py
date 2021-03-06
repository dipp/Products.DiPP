# -*- coding: utf-8 -*-
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id$

from elementtree.ElementTree import Element, SubElement
import elementtree.ElementTree as ET
from bibliograph.core.bibutils import _getCommand
from bibliograph.core.utils import _encode
from subprocess import Popen, PIPE
from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from dipp.tools import urnvalidator, indent
from dipp.dipp3 import qdc2metadata
from dipp.dipp3 import defaults, qdc
import Permissions


class BibTool(UniqueObject, SimpleItem):
    """Wrapper for Bibutils."""

    meta_type = 'BibTool'
    id = 'bibtool'
    title = 'Conversion of  metadata formats'
    toolicon = 'skins/dipp_images/fedora.png'
    security = ClassSecurityInfo()

    def formats(self):
        """Return a list of available Citation formats.

        Bibutils support more, but not the bibliograph.core Python module.
        """
        return defaults.SUPPORTED_BIBUTIL_FORMATS

    def get_creator_defaults(self):
        """an empty dictionary of the default creator metadata"""
        return qdc.get_creator_defaults()

    def get_author_identifier(self):
        author_identifier = {}
        for scheme, url, name in defaults.AUTHOR_IDENTIFIER:
            author_identifier[scheme] = name
        return author_identifier

    def short_citation(self, **kwargs):
        """Return short version of the bibligraphic citation.

        Calls only plones own catalog and does not wake up Fedora. Used in feeds
        and search results.
        """
        dp = self.portal_properties.dipp_properties
        mp = self.portal_properties.metadata_properties
        citation_format = dp.short_citation_format
        journalname = mp.journalname
        journal_shortname = mp.journalname_abbr
        issuedate = kwargs.get('issuedate', None)
        year = issuedate.strftime('%Y')
        volume = kwargs.get('volume', None)
        issue = kwargs.get('issue', None)
        startpage = kwargs.get('startpage', None)
        endpage = kwargs.get('endpage', None)
        urn = kwargs.get('urn', None)

        cite = citation_format % {
            'journal': journalname,
            'journal_shortname': journal_shortname,
            'volume': volume,
            'issue': issue,
            'startpage': startpage,
            'endpage': endpage,
            'urn': urn,
            'issuedate': issuedate,
            'year': year,
        }
        return cite

    def recommended_citation(self, PID, qdc):
        """Return the full bibliographic citation.

        Used below the article an on the  metadata page. Calls both
        Fedora and Plones catalog.
        """
        dp = self.portal_properties.dipp_properties
        citation_format = dp.citation_format
        initials_only = dp.initials_only
        comma_separated = dp.comma_separated
        initials_period = dp.initials_period
        last_author_suffix = dp.last_author_suffix
        firstnamefirst = dp.firstnamefirst

        # Metadata stored only in Plone
        try:
            startpage = self.startpage
        except:
            startpage = None

        try:
            endpage = self.endpage
        except:
            endpage = None

        # Qualified Dublin Core Metadata (qdc) stored in Fedora
        authors = qdc['creatorPerson']
        titles = qdc['title']
        title = titles[0]['value']
        bibliographicCitation = qdc['bibliographicCitation'][0]
        journal = bibliographicCitation['journalTitle']
        volume = bibliographicCitation['journalVolume']
        issue = bibliographicCitation['journalIssueNumber']
        try:
            issuedate = DateTime(bibliographicCitation['journalIssueDate'])
            date = issuedate.strftime(self.portal_properties.site_properties.localTimeFormat)
            year = issuedate.strftime('%Y')
        except:
            date = "????-??-??"
            year = "????"
        # urn
        urn = qdc.get('identifierURN', None)
        urn_url = None
        if urn:
            urn_url = '<a href="https://nbn-resolving.de/%(urn)s">%(urn)s</a>' % {'urn': urn}
        # doi
        doi = qdc.get('identifierDOI', None)
        doi_url = None
        if doi:
            doi_url = '<a href="https://doi.org/%(doi)s">%(doi)s</a>' % {'doi': doi}
        id = PID.split(':')[-1]
        authors_list = ""
        period = ""
        comma = ""

        if initials_period:
            period = ". "

        if comma_separated:
            comma = ','

        author_count = len(authors)
        for idx, author in enumerate(authors):
            firstnames = author['firstName'].split()
            firstnames_initials = ""
            for firstname in firstnames:
                firstnames_initials += firstname[0] + period
            if initials_only:
                firstname = firstnames_initials.strip()
            else:
                firstname = ' '.join(firstnames)
            lastname = author['lastName']
            if author_count == 1:
                prefix = ""
                suffix = ""
            elif idx == (author_count - 1) and author_count > 1:
                prefix = last_author_suffix
                suffix = ""
            else:
                prefix = ""
                suffix = ", "

            if firstnamefirst:
                authors_list += "%s %s %s%s" % (prefix, firstname, lastname, suffix)
            else:
                authors_list += "%s %s%s %s%s" % (prefix, lastname, comma, firstname, suffix)

        cite = citation_format % {
            'authors': authors_list,
            'title': title,
            'journal': journal,
            'volume': volume,
            'issue': issue,
            'startpage': startpage,
            'endpage': endpage,
            'year': year,
            'date': date,
            'id': id,
            'doi': doi_url,
            'urn': urn_url
        }
        return cite

    def _make_mods(self, qdc, PID):
        """Create a mods xml string for use with bibutils."""
        mods = Element("mods")

        # Metadata from the Journal
        try:
            ISSN = getattr(self, 'ISSN')
        except:
            ISSN = self.portal_properties.dipp_properties.ISSN.strip()
            if ISSN == "":
                fedora = getToolByName(self, "fedora")
                jqdc = fedora.getQualifiedDCMetadata(fedora.PID)
                ISSN = jqdc['identifierISSN']

        # Metadata stored only in Plone
        try:
            startpage = self.startpage
        except:
            startpage = None

        try:
            endpage = self.endpage
        except:
            endpage = None

        # Qualified Dublin Core Metadata (qdc) stored in Fedora
        # title
        qTitles = qdc['title']
        titleInfo = SubElement(mods, "titleInfo")
        title = SubElement(titleInfo, "title")
        title.text = qTitles[0]['value']

        # authors
        for author in qdc['creatorPerson']:
            name = SubElement(mods, "name", type="personal")
            namePart = SubElement(name, "namePart", type="family")
            namePart.text = author['lastName']
            namePart = SubElement(name, "namePart", type="given")
            namePart.text = author['firstName']

        # abstract
        qAbstracts = qdc['DCTermsAbstract']
        abstract = SubElement(mods, "abstract")
        abstract.text = qAbstracts[0]['value']

        # subjects
        subject = SubElement(mods, "subject")
        for qSubject in qdc['subject']:
            topic = SubElement(subject, "topic")
            topic.text = qSubject

        # ddc
        for qDDC in qdc['DDC']:
            ddc = SubElement(mods, "classification", authority="ddc")
            ddc.text = qDDC

        # genre
        relatedItem = SubElement(mods, "relatedItem", type="host")
        genre = SubElement(relatedItem, "genre", authority="marcgt")
        genre.text = "periodical"
        genre = SubElement(relatedItem, "genre")
        genre.text = "academic journal"

        # Bibliographic Data
        bc = qdc['bibliographicCitation'][0]

        # Journaltitle
        titleInfo = SubElement(relatedItem, "titleInfo")
        title = SubElement(titleInfo, "title")
        title.text = bc['journalTitle']

        # Volume/Issue/Pagenumbers
        part = SubElement(relatedItem, "part")
        volume = SubElement(part, "detail", type="volume")
        number = SubElement(volume, "number")
        number.text = bc["journalVolume"]
        issue = SubElement(part, "detail", type="issue")
        number = SubElement(issue, "number")
        number.text = bc["journalIssueNumber"]
        date = SubElement(part, "date")
        try:
            year = DateTime(bc["journalIssueDate"]).strftime('%Y')
        except:
            year = "????"
        date.text = year
        if startpage:
            extent = SubElement(part, "extent", unit="page")
            start = SubElement(extent, "start")
            start.text = str(startpage)
            end = SubElement(extent, "end")
            end.text = str(endpage)

        # identifier
        id = qdc['creatorPerson'][0]["lastName"].lower() + str(year)
        if ISSN:
            issn = SubElement(mods, "identifier", type="issn")
            issn.text = ISSN
        urn = SubElement(mods, "identifier", type="urn")
        urn.text = qdc['identifierURN']
        if qdc['identifierDOI']:
            doi = SubElement(mods, "identifier", type="doi")
            doi.text = qdc['identifierDOI']
        uri = SubElement(mods, "identifier", type="uri")
        uri.text = "http://nbn-resolving.de/" + qdc['identifierURN']
        citekey = SubElement(mods, "identifier", type="citekey")
        citekey.text = id
        return mods

    def convert(self, qdc, PID, target_format):
        """Convert the QDC Metadata from Fedora to any format supported by bibutils.

        Uses MODS as an intermediate format.
        """
        mods = self._make_mods(qdc, PID)
        if target_format == 'xml':
            indent.indent(mods)
            xml = ET.tostring(mods, encoding='utf-8')
            result = xml
        else:
            xml = ET.tostring(mods, encoding='utf-8')
            command = _getCommand('xml', target_format)
            p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                      close_fds=False)
            (fi, fo, fe) = (p.stdin, p.stdout, p.stderr)
            # fi.write(_encode(xml))
            fi.write(xml)
            fi.close()
            result = fo.read()
            fo.close()
            error = fe.read()
            fe.close()

        return result

    def urnstatus(self, urn, url):
        """Check status of an urn with the dnb resolver"""
        status = urnvalidator.URN(urn, url)
        return status.validity, status.details

    # security.declareProtected(Permissions.MANAGE_JOURNAL, 'datacite_xml')
    def datacite_xml(self, pid, issn, publisher, pdf):
        """Return metadata in DataCite compliant  XML format."""
        metadata = qdc2metadata.MetaData(pid, issn=issn, publisher=publisher, pdf=pdf)
        return metadata.make_datacite_xml()

    #  security.declareProtected(Permissions.MANAGE_JOURNAL, 'doaj_xml')
    def doaj_xml(self, pid, issn, publisher, pdf):
        """Return metadata in DOAJ compliant  XML format."""
        metadata = qdc2metadata.MetaData(pid, issn=issn, publisher=publisher, pdf=pdf)
        return metadata.make_doaj_xml()
    
    #  security.declareProtected(Permissions.MANAGE_JOURNAL, 'epicur_xml')
    def xepicur_xml(self, pid, url, issn, publisher, pdf):
        """Return metadata in Xepicur compliant  XML format."""
        metadata = qdc2metadata.MetaData(pid, url=url, issn=issn, publisher=publisher, pdf=pdf)
        return metadata.make_xepicur_xml()


    def make_metatags(self, pid, issn, publisher, pdf, startpage, endpage):
        """Return meta tags for google scholar, facebook, twitter

        Tags are returned as HTML, so this method has to be used with 'structure'
        in pagetemplates.
        """
        dp = self.portal_properties.dipp_properties
        mp = self.portal_properties.metadata_properties

        metadata = qdc2metadata.MetaData(
            pid,
            issn=issn,
            publisher=publisher,
            pdf=pdf,
            startpage=startpage,
            endpage=endpage,
            citation_format=dp.short_citation_format,
            journal_shortname=mp.journalname_abbr
        )

        return metadata.make_metatags()
