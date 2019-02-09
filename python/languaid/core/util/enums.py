'''
    Created on Dec 31, 2018

    @author: fb
    @summary: contains enums
'''
from enum import Enum


class Enums():

    # enums representing the currently available word modifications, for both verbs and nouns
    Number = Enum('Number', 'singular plural')
    VModes = Enum('VModes', 'negation reciprocal voluntative imperative')  # verb modes
    NModes = Enum('NModes', 'possession')  # noun modes
    Tenses = Enum('Tenses', 'past present futur')
    WTypes = Enum('WTypes', 'noun verb')
    Imperative = Enum('Imperative', 'voluntative imperative')  # not used
    Languages = Enum('Languages', 'en tr')  # supported languages

    def getAllEnums(self):
        '''
            @return: A list containing all currently available Enums
        '''
        return [self.Number, self.VModes, self.NModes, self.Tenses, self.Imperative]

    def getVerbEnums(self):
        '''
        '''
        return [self.VModes, self.Tenses, self.Imperative]

    def getNounEnums(self): 
        '''
        '''
        return [self.NModes, self.Number]
        
