#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Created on Dec 27, 2018

    @author: fb
    @summary: unit tests for noun construction/deconstruction
    @see: lfko.python.languaid.core.lang.noun.py
'''

import unittest
from python.languaid.core.lang.noun import Noun
from python.languaid.core.util.enums import Enums


class LangCoreNounTest(unittest.TestCase):

    def runTests(self):
        """
            @summary: convenient method for calling the unit test module externally
        """
        
        unittest.main()

    def testFaultTolerance(self):

        nn = Noun()
        with self.assertRaises(TypeError):
            nn.construct(None, None)
            nn.construct('', [])
            nn.construct('STRING', [])
            nn.construct('', ['STRING'])
        
    def testVerbConstruct(self):

        nn = Noun()
        self.assertEqual(nn.construct(noun='canta', args=[['number', Enums().Number.plural.name]]), 'cantalar')
        self.assertEqual(nn.construct(noun='canta', args=[['number', Enums().Number.plural.name], ['mode', Enums().NModes.possession.name, 0]]), 'cantalarım')
        self.assertEqual(nn.construct(noun='canta', args=[['mode', Enums().NModes.possession.name, 1]]), 'cantan')
        self.assertEqual(nn.construct(noun='fotoğraf makine', args=[['mode', Enums().NModes.possession.name, 2]]), 'fotoğraf makinesi')
        
        self.assertEqual(nn.construct(noun='kız', args=[['mode', Enums().NModes.possession.name, 0]]), 'kızım')
        self.assertEqual(nn.construct(noun='kız', args=[['mode', Enums().NModes.possession.name, 1]]), 'kızın')
        self.assertEqual(nn.construct(noun='kız', args=[['mode', Enums().NModes.possession.name, 2]]), 'kızı')
        self.assertEqual(nn.construct(noun='kız', args=[['mode', Enums().NModes.possession.name, 3]]), 'kızımız')
        self.assertEqual(nn.construct(noun='kız', args=[['mode', Enums().NModes.possession.name, 4]]), 'kızınız')
        self.assertEqual(nn.construct(noun='kız', args=[['mode', Enums().NModes.possession.name, 5]]), 'kızları')
        
        self.assertEqual(nn.construct(noun='otobüs', args=[['mode', Enums().NModes.possession.name, 0]]), 'otobüsüm')
        self.assertEqual(nn.construct(noun='otobüs', args=[['mode', Enums().NModes.possession.name, 1]]), 'otobüsün')
        self.assertEqual(nn.construct(noun='otobüs', args=[['mode', Enums().NModes.possession.name, 2]]), 'otobüsü')
        self.assertEqual(nn.construct(noun='otobüs', args=[['mode', Enums().NModes.possession.name, 3]]), 'otobüsümüz')
        self.assertEqual(nn.construct(noun='otobüs', args=[['mode', Enums().NModes.possession.name, 4]]), 'otobüsünüz')
        self.assertEqual(nn.construct(noun='otobüs', args=[['mode', Enums().NModes.possession.name, 5]]), 'otobüsleri')

    def testNounDeconstruct(self):

        from python.languaid.core.util.util import deconstruct
        self.assertEqual(deconstruct('otobüsleri', 'noun'), ['possession', 6])
        self.assertEqual(deconstruct('otobüsüm', 'noun'), ['possession', 1])
        self.assertEqual(deconstruct('otobüsün', 'noun'), ['possession', 2])
        self.assertEqual(deconstruct('kızımız', 'noun'), ['possession', 4])
        self.assertEqual(deconstruct('cantalarım', 'noun'), ['possession', 1, 'plural'])
        self.assertEqual(deconstruct('arabaların', 'noun'), ['possession', 2, 'plural'])
        self.assertEqual(deconstruct('arabaları', 'noun'), ['possession', 6])
        
    def tearDown(self):

        print('tests done - tearing down')


if __name__ == "__main__": 
    unittest.main()
