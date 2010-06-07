import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Products.PloneTestCase import PloneTestCase
from Products.CMFCore.utils import getToolByName
from Products.PloneFedora2DiPP3.config import TOOLNAME

PloneTestCase.installProduct('PloneFedora2DiPP3')
PloneTestCase.installProduct('ATVocabularyManager')
PloneTestCase.installProduct('CMFOpenflow')
PloneTestCase.installProduct('DiPPContent')
PloneTestCase.installProduct('LinguaPlone')
PloneTestCase.installProduct('PloneLanguageTool')
PloneTestCase.installProduct('TextIndexNG3')
PloneTestCase.installProduct('DiPP')
#PloneTestCase.setupPloneSite(products=('DiPP',))
PloneTestCase.setupPloneSite()


class TestMetadata(PloneTestCase.PloneTestCase):
    PID = 'dipp:1898'
    label = '81' 
    address = '193.30.112.98'
    port = '9280'

    def afterSetUp(self):
        self.portal.manage_addProduct['PloneFedora2DiPP3'].manage_addTool('PloneFedora2DiPP3')
        self.tool = getToolByName(self.portal, 'fedora')
    
    def testSetFedoraSettings(self):
        self.setRoles(['Manager'])
        self.tool.manage_setFedoraSettings(self.PID, self.label, self.address, self.port, None)
        self.assertEquals(self.tool.PID, self.PID)
    
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMetadata))
    return suite

if __name__ == '__main__':
    framework()
