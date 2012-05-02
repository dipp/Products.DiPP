import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Products.PloneTestCase import PloneTestCase
from Products.CMFCore.utils import getToolByName
from Products.DiPP.config import PID, label, address, port

PloneTestCase.installProduct('ATVocabularyManager')
PloneTestCase.installProduct('CMFOpenflow')
PloneTestCase.installProduct('DiPPContent')
PloneTestCase.installProduct('LinguaPlone')
PloneTestCase.installProduct('PloneLanguageTool')
PloneTestCase.installProduct('TextIndexNG3')
PloneTestCase.installProduct('DiPP')
PloneTestCase.setupPloneSite(products=('DiPP',))


class TestMetadata(PloneTestCase.PloneTestCase):

    PID = PID
    label = label
    address = address
    port = port
    
    def afterSetUp(self):
        #self.portal.manage_addProduct['DiPP'].manage_addTool('Fedora2DiPP3')
        self.tool = getToolByName(self.portal, 'fedora')
        self.typestool = getToolByName(self.portal, 'portal_types')
    
    def testSetFedoraPID(self):
        self.setRoles(['Manager'])
        self.tool.manage_setFedoraSettings(self.PID, None, None, None, None)
        self.assertEquals(self.tool.PID, self.PID)
        
    def testSetFedoraLabel(self):
        self.setRoles(['Manager'])
        self.tool.manage_setFedoraSettings(None, self.label,  None, None, None)
        self.assertEquals(self.tool.label, self.label)

    def testSetFedoraAddress(self):
        self.setRoles(['Manager'])
        self.tool.manage_setFedoraSettings(None, None,  self.address, None, None)
        self.assertEquals(self.tool.address, self.address)

    def testSetFedoraPort(self):
        self.setRoles(['Manager'])
        self.tool.manage_setFedoraSettings(None, None, None, self.port, None)
        self.assertEquals(self.tool.port, self.port)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMetadata))
    return suite

if __name__ == '__main__':
    framework()
