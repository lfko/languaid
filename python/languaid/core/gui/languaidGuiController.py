'''
    Created on Feb 8, 2019

    @author: lfko
    @summary: modul implementing all the underlying, not gui-related functions of the main gui
'''
from python.languaid.core.lang.verb import Verb
from python.languaid.core.lang.noun import Noun
import python.languaid.core.lang.translate as tr


class GuiController():
    '''
    classdocs
    '''

    def __init__(self):
        '''
            Constructor
        '''
        
        self.vb = Verb()
        self.n = Noun()
        self.verb_modes = [m for m in self.vb.Modes]
        self.verb_tenses = [t for t in self.vb.Tenses]
        self.noun_modes = [m for m in self.n.Modes]
        self.noun_number = [n for n in self.n.Number]
        
    def constructVerb(self, word, args):
        '''
            @param args: List of arguments; arguments itself are lists distinct parameters
        '''
        return self.vb.construct(word, args)
        
    def checkVerb(self):
        '''
        '''
                
        self.verb_modes
        
    def constructNoun(self):
        '''
        '''
        
    def translate(self, word, src_lang, target_lang):
        '''
        '''
        return tr.translate(word, src_lang, target_lang)
