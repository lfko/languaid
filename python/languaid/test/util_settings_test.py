'''
    Created on Dec 28, 2018

    @author: fb
    @summary: 
    @see: languaid.core.util.settings.py
'''
import unittest
from python.languaid.core.util.settings import Settings


class UtilCoreSettingsTest(unittest.TestCase):
    """
    """
    
    def testGetValue(self):
        """ 
            @summary: 
        """
        appSet = Settings()
        appSet.getValue('', '')
        

if __name__ == "__main__": 
    unittest.main()
