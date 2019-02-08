'''
    Created on Dec 6, 2018

    @author: lfko
    @summary: : grammatical rules should be loadable, so that the application has a more universal approach

'''

import json
from python.languaid.core.util.settings import Settings


class RuleLoader():

    def __init__(self):
        """ 
            @summary: default constructor
            @param category: name of the category, for which the rules should be loaded
            @return: dictionary containing the specific rules
        """
        
        self.appSet = Settings()

        with open(str(self.appSet.ini_dir) + '/' + self.appSet.getValue('RULES', 'RULE_FILE_NAME')) as f:
            self.data = json.load(f)

    def findAllKeys(self, key_type):
        """ 
            @todo: not yet used
        """
        foodict = {k: v for k, v in self.data.items() if k.startswith(key_type)}
        
        print([v for k, v in foodict[type][0].items() if k.startswith('suffixes')])

    def find(self, args):
        """
            @summary: find the rule entries for a specific key 
            @param args: list of keys for a specific item in a subcategory
            @return: list of rule elements or the element itself
        """
        rules = []
        # list of specific rules for a key of a category
        if len(args) == 3:
            # tuples allow for more complex rule queries
            rules = self.data[args[0]][0][args[1]][0]['items'][args[2]]
        elif len(args) == 2:
            try:
                rules = self.data[args[0]][0][args[1]][0]['items']
            except KeyError:
                return None
        elif len(args) == 1:
            try:
                rules = self.data[args[0]][0]['items']
            except KeyError:
                # we are looking only for the keys of a sub dictionary - should not happen very often
                rules = self.data[args[0]][0].keys()
            
        return rules[0] if len(rules) == 1 else rules

    def getCanUse(self, category, subcategory):
        """
            @summary: Retrieve possible suffixes per word type
            @param category: a suffix category, e.g. mode
            @param subcategory: a subcategory, e.g. imperative for mode
            @return: a list of possibly appliable suffixes
        """
        canUse = self.data[category][0][subcategory][0]['canUse']
        
        return canUse

    def getSuffixOrder(self, wordType, category):
        """ 
            @summary: 
            @param wordType:
            @return:  
        """
        suffixOrder = self.data[category][0]['order'][0][wordType]
        return suffixOrder

