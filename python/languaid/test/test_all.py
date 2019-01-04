'''
    Created on Jan 4, 2019

    @author: lfko
    @summary: script for providing a convenient way of testing all unit tests at once (or, at least, calling them all at once)
'''

# from . import lang_noun_test, lang_translate_test, lang_verb_test, util_settings_test
from python.languaid.test.lang_noun_test import LangCoreNounTest
from python.languaid.test.lang_verb_test import LangCoreVerbTest


def runAllUnitTests():
    """ 
        @summary: call all unit test modules
    """
    
    LangCoreNounTest().runTests()
    LangCoreVerbTest().runTests()


runAllUnitTests()
