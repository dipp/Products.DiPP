# -*- coding: utf-8 -*-
# ...
# File: BibUtils.py
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#
# $Id: FedoraTool.py 2132 2010-06-04 07:08:42Z reimer $

from  elementtree.ElementTree import Element, SubElement
import elementtree.ElementTree as ET    
import datetime
from bibliograph.core.bibutils import _getCommand
from bibliograph.core.utils import _encode
from subprocess import Popen, PIPE
from DateTime import DateTime
from OFS.SimpleItem import SimpleItem
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject, getToolByName
from config import view_permission, LANGUAGES

class BibTool(UniqueObject, SimpleItem):
    """ Wrapper for Bibutils """
    
    meta_type = 'BibTool'
    id = 'bibtool'
    title = 'convert metadaformats'
    toolicon = 'skins/dipp_images/fedora.png'
    security = ClassSecurityInfo()

    def formats(self):
        """return a list of available Citation formats. Bibutils support more,
           but not the bibliograph.core Python module. 
        """
        formats = (
            ("Endnote","end"),
            ("Bibtex","bib"),
            ("Reference Manger","ris"),
            ("MESH","xml")
        )
        return formats
   
    def indent(self, elem, level=0):
        """Pretty printing of the mods xml format"""

        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
   
    def _make_mods(self,qdc,PID):
        """Create a mods xml string for use with bibutils"""
        
        mods = Element("mods")

        # Metadata from the Journal
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
        year = DateTime(bc["journalIssueDate"]).strftime('%Y')
        date.text = year
        if startpage:
            extent = SubElement(part,"extent", unit="page")
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
        uri.text = "http://nbn-resolving.org/urn/resolver.pl?" + qdc['identifierURN']
        citekey = SubElement(mods, "identifier", type="citekey")
        citekey.text = id
        return mods
    
    def convert(self, qdc, PID, target_format):
        
        mods = self._make_mods(qdc, PID)
        if target_format == 'xml':
            self.indent(mods)
            xml = ET.tostring(mods)
            result = xml
        else:
            xml = ET.tostring(mods)
            command = _getCommand('xml', target_format)
            p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
                      close_fds=False)
            (fi, fo, fe) = (p.stdin, p.stdout, p.stderr)
            fi.write(_encode(xml))
            fi.close()
            result = fo.read()
            fo.close()
            error = fe.read()
            fe.close()

        return result
