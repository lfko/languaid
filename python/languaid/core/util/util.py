'''
    Created on Dec 31, 2018

    @author: lfko
    @summary: module for providing some utility functions or functions, which are used in multiple modules
'''


def deconstruct(word, wordType):
    """ 
        @summary: deconstruct an already valid verb to its separate suffixes 
        @param word: the word to analyse
        @param wordType: type of the word (e.g. verb or noun) 
        @return: a dict containing the found suffixes
    """
    import re
    from lfko.python.languaid.core.util.ruleLoader import RuleLoader
    
    found_suffixes = []
    
    suffix_order = RuleLoader().getSuffixOrder(wordType, 'deconstruct')  # load the building rules for verbs

    for key, value in suffix_order[0].items():

        # suffixes = self.rl.find([order])
        
        # for s in suffixes:
        # replace the vowel wildcard characters with a '.' so we can use regex
        s_tmp = key.replace('-', '.').replace('_', '.')
        suffixes = s_tmp.split('|')
        for s in suffixes:
            # look for a match at the end of the word string
            if re.search(r"(" + s + ")", word):
                found_suffixes.append(value)  # adds the found suffix to the dict of suffixes
                # word = word[:-len(s)]  # removes the ending from the noun
                break
    
    # print(found_suffixes)
    return found_suffixes
