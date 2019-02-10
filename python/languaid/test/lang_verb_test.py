#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Dec 27, 2018

    @author: fb
    @summary: unit tests for verb construction/deconstruction
'''

import unittest
from python.languaid.core.util.enums import Enums
from python.languaid.core.lang.verb import Verb


class LangCoreVerbTest(unittest.TestCase):
    
    def runTests(self):
        """
            @summary: convenient method for calling the unit test module externally
        """
        unittest.main()
    
    def testVerbConstructPresent(self):

        vb = Verb()
        self.assertEqual(vb.construct('kullanmak', [['mode', Enums().VModes.negation.name], ['tense', Enums().Tenses.present.name, 5]]), 'kullanmıyorlar')
        self.assertEqual(vb.construct('yürümek', [['mode', Enums().VModes.negation.name], ['tense', Enums().Tenses.present.name, 2]]) , 'yürümüyor')
        self.assertEqual(vb.construct('okumak', [['mode', Enums().VModes.negation.name], ['tense', Enums().Tenses.present.name, 3]]) , 'okumuyoruz')
        self.assertEqual(vb.construct('söylemek', [['tense', Enums().Tenses.present.name, 4]]) , 'söylüyorsunuz')
        self.assertEqual(vb.construct('aramak', [['tense', Enums().Tenses.present.name, 5]]), 'arıyorlar')
        self.assertEqual(vb.construct('yürümek', [['tense', Enums().Tenses.present.name, 3]]), 'yürüyoruz')

    def testVerbConstructPast(self):

        vb = Verb()
        self.assertEqual(vb.construct('kullanmak', [['tense', Enums().Tenses.past.name, 0]]), 'kullandım')
        self.assertEqual(vb.construct('aramak', [['mode', Enums().VModes.negation.name], ['tense', Enums().Tenses.past.name, 4]]), 'aramadınız')
        self.assertEqual(vb.construct('dilmek', [['mode', Enums().VModes.negation.name], ['tense', Enums().Tenses.past.name, 0]]), 'dilmedim')

    def testVerbConstructFutur(self):

        vb = Verb()
        self.assertEqual(vb.construct('uyukmak', [['tense', Enums().Tenses.futur.name, 3]]), 'uyukacağız')  
        self.assertEqual(vb.construct('yazmak', [['tense', Enums().Tenses.futur.name, 1]]), 'yazacağın')
        
    def testVerbConstructVoluntative(self):

        self.assertEqual(Verb().construct('yapmak', [['mode', Enums().Imperative.voluntative.name, 0]]), 'yapayım')
        self.assertEqual(Verb().construct('yapmak', [['mode', Enums().Imperative.voluntative.name, 1]]), 'yapalım')
        self.assertEqual(Verb().construct('gitmek', [['mode', Enums().Imperative.voluntative.name, 1]]), 'gitelim')      

    def testVerbConstructImperative(self):

        self.assertEqual(Verb().construct('gelmek', [['mode', Enums().Imperative.imperative.name, 0]]), 'gel')
        self.assertEqual(Verb().construct('okumak', [['mode', Enums().Imperative.imperative.name, 1]]), 'okuyun')
        self.assertEqual(Verb().construct('gelmek', [['mode', Enums().Imperative.imperative.name, 1]]), 'gelin')
        self.assertEqual(Verb().construct('demek', [['mode', Enums().VModes.negation.name], ['mode', Enums().Imperative.imperative.name, 0]]), 'deme')     
        self.assertEqual(Verb().construct('etmek', [['mode', Enums().VModes.negation.name], ['mode', Enums().Imperative.imperative.name, 1]]), 'etmeyin')  

    def testVerbDeconstruct(self):

        from python.languaid.core.util.util import deconstruct
        # self.assertEqual(deconstruct('yiyeyim', 'verb'), [Enums().Imperative.voluntative.name])
        self.assertEqual(deconstruct('geliyorum', 'verb'), ['person', 1 , Enums().Tenses.present.name])
        self.assertEqual(deconstruct('geleceğin', 'verb'), ['person', 2, Enums().Tenses.futur.name])
        with self.assertRaises(ValueError):
            deconstruct('', None)
            deconstruct(None, None)
        
    def tearDown(self):

        print('tests done - tearing down')


if __name__ == "__main__": 
    unittest.main()
