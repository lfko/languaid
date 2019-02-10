'''
    Created on Feb 8, 2019

    @author: lfko
    @summary: modul implementing all the underlying, not gui-related functions of the main gui
'''
from python.languaid.core.lang.verb import Verb
from python.languaid.core.lang.noun import Noun
from python.languaid.core.util.util import deconstruct
import python.languaid.core.lang.translate as tr


class GuiController():

    def __init__(self):

        self.vb = Verb()
        self.n = Noun()
        # we need to access these properties in the GUI class, therefore we are forwarding them here in the controller
        self.verb_modes = [m for m in self.vb.Modes]
        self.verb_tenses = [t for t in self.vb.Tenses]
        self.noun_modes = [m for m in self.n.Modes]
        self.noun_number = [n for n in self.n.Number]
        
    def constructVerb(self, word, args):
        '''
            @param word: a verb in infinitive form
            @param args: List of arguments; arguments itself are lists distinct parameters
            
        '''
        return self.vb.construct(word, args)
        
    def constructNoun(self, word, args):
        '''
            @param word: a noun
            @param args: List of arguments; arguments itself are lists distinct parameters
        '''
        return self.n.construct(word, args)

    def checkWord(self, word, wtype):
        '''
            @param word: word to check/deconstruct
            @param wtype: verb or noun 
        '''
        return deconstruct(word, wtype)
    
    def translate(self, word, src_lang, target_lang):
        '''
            @param word: the word to translate
            @param src_lang: source lang, abbreviated (e.g. en)
            @param target_lang: dito
        '''
        return tr.translate(word, src_lang, target_lang)
