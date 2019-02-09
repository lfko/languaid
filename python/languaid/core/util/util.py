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
    
    if('' in (word, wordType)):
        raise ValueError('No parameters supplied!')
    
    import re
    from python.languaid.core.util.ruleLoader import RuleLoader
    
    found_suffixes = []
    
    rules = RuleLoader().getSuffixOrder(wordType, 'deconstruct')  # load the building rules
    suffix_order = RuleLoader().getSuffixOrder(wordType + '_order', 'deconstruct')
    suffix_order = suffix_order[::-1]

    for suf in suffix_order:
        d = dict((k, v) for k, v in rules[0].items() if v == suf)

        for k, v in d.items():

            # replace the vowel wildcard characters with a '.' so we can use regex
            s_tmp = k.replace('-', '.').replace('_', '.')
            suffixes = s_tmp.split('|')
            
            for i, s in enumerate(suffixes):
                # look for a match at the end of the word string

                if re.search(r"(" + s + ")$", word):
                    found_suffixes.append(v)  # adds the found suffix to the dict of suffixes
                    if v in ['possession', 'person']:
                        found_suffixes.append(i)

                    word = re.sub(s, '', word)  # removes the ending from the noun
                    break
    
    return found_suffixes
