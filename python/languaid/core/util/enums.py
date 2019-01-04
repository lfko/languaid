'''
    Created on Dec 31, 2018

    @author: fb
    @summary: contains enums
'''
from enum import Enum


class Enums():

    # enums representing the currently available word modifications, for both verbs and nouns
    Number = Enum('Number', 'singular plural')
    Modes = Enum('Modes', 'possession negation reciprocal passive')
    Tenses = Enum('Tenses', 'past present futur')
    Imperative = Enum('Imperative', 'voluntative imperative')  
