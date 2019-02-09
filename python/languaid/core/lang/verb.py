'''
    Created on Dec 3, 2018

    @author: fb
    @summary: 
'''

from python.languaid.core.util.ruleLoader import RuleLoader
from python.languaid.core.lang.vowel import VowelHarmonizer
from python.languaid.core.util.enums import Enums


class Verb():
    
    def __init__(self):
        """ 
            @summary: default constructor
        """
        self.vh = VowelHarmonizer()
        self.rl = RuleLoader()
        self.vowels = self.rl.find(['vowels', 'vowels'])
        self.Modes = [e.name for e in Enums().VModes]
        self.Tenses = [e.name for e in Enums().Tenses]

    def construct(self, word, args=[]):
        """ 
            @summary: construct a verb with the requested suffixes
            @param word: the verb to decline (in its infinitive form)
            @param args: list of parameters
            @return: a conjugated verb
        """
        if word == '' or word == None:
            raise TypeError('empty word supplied')
        if len(args) == 0 or args == None:
            raise TypeError('empty argument lists supplied')

        # the basic build rule: replace the suffix of the infinitive
        word_stem = word.replace('mak', '').replace('mek', '')

        buildRule = "'" + word_stem + "'"
        print(args)
        for arg in args:

            suffix = self.rl.find(arg)
            if suffix == None:
                continue

            if len(buildRule) > 0:
                
                if (buildRule[-2] == '-' or buildRule[-2] in self.vowels) and suffix[0] == '%':
                    suffix = suffix.replace('%', 'y')  # to separate sequent vowels we include an 'y'
                elif buildRule[-2] in self.vowels: 
                    if (suffix[0] in self.vowels) or (suffix[0] in ['_', '-']):
                        buildRule = buildRule[:-2] + "'"
                        word_stem = word_stem[:-1]

            buildRule = buildRule + " + " + "'" + suffix + "'"

        # with eval, we are able to execute a string as actual python code
        evalBuild = eval(buildRule)
        
        return self.vh.harmonize(word_stem, evalBuild)

