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
from bibliograph.core.bibutils import _getCommand
from subprocess import Popen, PIPE
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
        mods = Element("mods", ID=PID)
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

        # genre
        relatedItem = SubElement(mods, "relatedItem", type="host")
        genre = SubElement(relatedItem, "genre", authority="marcgt")
        genre.text = "periodical"
        genre = SubElement(relatedItem, "genre")
        genre.text = "academic journal"
        
        bc = qdc['bibliographicCitation'][0]
        titleInfo = SubElement(relatedItem, "titleInfo")
        title = SubElement(titleInfo, "title")
        title.text = bc['journalTitle']
        
        part = SubElement(relatedItem, "part")
        volume = SubElement(part, "detail", type="volume")
        number = SubElement(volume, "number")
        number.text = bc["journalVolume"]
        issue = SubElement(part, "detail", type="issue")
        number = SubElement(issue, "number")
        number.text = bc["journalIssueNumber"]


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
            # fi.write(_encode(data))
            fi.write(xml)
            fi.close()
            result = fo.read()
            fo.close()
            error = fe.read()
            fe.close()

        return result
