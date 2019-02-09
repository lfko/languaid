'''
    Created on Dec 28, 2018

    @author: fb
    @summary: some basic unit tests
    @see: python.languaid.core.lang.translate
'''

import unittest
import python.languaid.core.lang.translate as tr


class LangCoreTranslateTest(unittest.TestCase):
    
    def runTests(self):
        """
            @summary: convenient method for calling the unit test module externally
        """
        
        unittest.main()
    
    def testFaultTolerance(self):
        '''
            @summary: Testing some wrong parameters
        '''
        with self.assertRaises(TypeError):
            tr.translate(None, None)
            tr.translate('', [])
            tr.translate('STRING', [])
            tr.translate('', ['STRING'])
    
        with self.assertRaises(ValueError):
            tr.translate(None, None, None)
            tr.translate('', '', '')
            tr.translate('', 'en', 'tr')
            tr.translate('word', None, None)
            tr.translate(123, False, True)
    
    def testTranslate(self):
        """ 
            @summary: Some test translations
        """
        self.assertEqual(tr.translate('apple', 'en', 'tr'), 'elma')
        self.assertEqual(tr.translate('car', 'en', 'tr'), 'araba')
        self.assertEqual(tr.translate('newspaper', 'en', 'tr'), 'gazete')
        
        self.assertEqual(tr.translate('yemek', 'tr', 'en'), 'eat')
        self.assertEqual(tr.translate('bilgisayar', 'tr', 'en'), 'computer')
        self.assertEqual(tr.translate('kullanmak', 'tr', 'en'), 'use')

    def tearDown(self):

        print('tests done - tearing down')    


if __name__ == "__main__": 
    unittest.main()
