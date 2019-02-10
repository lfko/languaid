'''
    Created on Dec 30, 2018

    @author: lfko
    @summary: Module which is used during the vowel harmonization
'''
from python.languaid.core.util.ruleLoader import RuleLoader


class VowelHarmonizer():
    
    def __init__(self):

        self.rl = RuleLoader()
        self.vowels = self.rl.find(['vowels', 'vowels'])

    def harmonize(self, word_stem, word):
        """
            @summary: harmonizes the vowels of a verb/noun corresponding to the grammatical rules
            @param word_stem:
            @param word:
            @return: a noun/verb with harmonized vowels   
        """
        preceding_vow = [c for c in word_stem if c in self.vowels][-1]  # the first reference vowel
        word = word.replace('-_', '_')  # to avoid cases where to vowels could follow each other

        # get the dictionary of high vowels
        high_vow = self.rl.find(['vowels', 'high_vowels'])
        # get the dictionary of low vowels
        low_vow = self.rl.find(['vowels', 'low_vowels'])

        # since strings are immutable, we manage a list of replacements, which
        # will be applied afterwards to the word
        word_repl = {}
        for i, c in enumerate(word):

            if c in self.vowels or c in ['-', '_']:
            
                # char is a valid vowel
                if c != preceding_vow and word[(i - 1)] != '*':
                    if c == '_':
                        cNew = high_vow[preceding_vow]
                    elif c == '-':
                        cNew = low_vow[preceding_vow]
                    else:
                        cNew = c

                    # strings are immutable, so we save the changes for later and apply them later to build the final verb 
                    word_repl[i] = cNew
                    preceding_vow = cNew

                    # TODO Konsonantenerweichung
                    
                else:
                    preceding_vow = c

        # get the word as a list, so we can replace characters (i.e. vowels)
        word_as_list = list(word)
        for key in word_repl.keys():
            word_as_list[key] = word_repl[key]

        # final word
        word = ''.join(word_as_list)
        word = word.replace('*', '').replace('%', '')  # just remove some remaining special characters
        
        return word
