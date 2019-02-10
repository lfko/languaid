'''
    Created on Dec 6, 2018

    @author: fb
    @summary: Module used for constructing a valid noun with the rules supplied
'''

from python.languaid.core.util.ruleLoader import RuleLoader
from python.languaid.core.lang.vowel import VowelHarmonizer
from python.languaid.core.util.enums import Enums


class Noun():
    
    def __init__(self):

        self.vh = VowelHarmonizer()
        self.rl = RuleLoader()
        # load the valid vowels
        self.vowels = self.rl.find(['vowels', 'vowels'])
        # load valid modes and numbers for nouns
        self.Number = [e.name for e in Enums().Number]
        self.Modes = [e.name for e in Enums().NModes]
    
    def construct(self, noun, args=[]):
        """ 
            @summary: construct a valid noun; there are some restrictions, which should be applied 
            @param noun: the basic noun
            @param args[]: contains the suffixes we'd like to apply/attach to the basic noun, e.g. 'plural' or 'possession'
            @return: a declined noun
        """
        if noun == '' or noun == None:
            raise TypeError('empty noun supplied')
        if len(args) == 0 or args == None:
            raise TypeError('empty argument lists supplied')

        buildRule = "'" + noun + "'"

        for arg in args:

            suffix = self.rl.find(arg)  # find the suffix to attach
            if buildRule[-2] in self.vowels and suffix[0] == '_': 
                # if the word ends with a vowel we don't need to replace the '_' of the suffix with a vowel
                buildRule = buildRule + " + " + "'" + suffix.replace('_', '') + "'"
            elif buildRule[-2] in self.vowels and suffix[0] == '%':
                suffix = suffix.replace('%', 's')  # specific rule to separate sequent vowels
                buildRule = buildRule + " + " + "'" + suffix + "'"
            else:
                buildRule = buildRule + " + " + "'" + suffix + "'"

        # with eval, we are able to execute a string as actual python code
        evalBuild = eval(buildRule)
        
        return self.vh.harmonize(noun, evalBuild)
