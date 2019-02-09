#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Created on Dec 3, 2018

    @author: fb
    @summary: purposed main entry class of the application
'''
import os


def loader():
    '''
        should the application be started as CLI or GUI
    '''
    # os.environ['MAIN_DIR'] = "../../languaid"
    import sys
    print(sys.path)
    
    print(' Welcome to LanguAid! ')
    print(' GUI or CLI? ')
    decision = input('Type in "gui" for GUI or "cli" for CLI').lower().strip()
    if decision not in ('gui', 'cli'):
        print(' Invalid option! Try again ')
        loader()
    elif decision == 'gui':
        __app_as_gui__()
    elif decision == 'cli':
        __app_as_cli__()


def __app_as_gui__():
    """ 
        load the application with the tkinter gui
    """
    # by loading the class the module will be loaded as well and so the gui
    from python.languaid.core.gui.languaidGUI import LanguaidGUI


def __app_as_cli__():
    """ 
        load the application on the cli
    """
    menuItems = [('translate a word', __translate__),
                 ('check a word (noun or verb)', __check__),
                 ('construct a verb', __constructVerb__),
                 ('construct a noun', __constructNoun__),
                 ('exit the application', __exit__)]

    # load a welcome message and the options menu
    welcome_txt = open('../res/welcome-txt.txt', 'r')
    print(welcome_txt.read())
    for i, item in enumerate(menuItems):
        print('>> (' + str(i) + ')', item[0])

    choice = input('>> ')

    try:
        if int(choice) < 0:
            raise ValueError(' wrong choice! ')

        # execute the selected menu entry - we read the function pointer, add
        # '()' and thus, it is an executable function call
        menuItems[int(choice)][1]()
    except(ValueError, IndexError):
        pass


def __constructVerb__():
    """
    
    """
    from python.languaid.core.lang.verb import Verb
    
    print(' constructVerb called ')

    vb = Verb()
    
    while(True):
        args = []
        word = input(' >> enter a verb to conjugate (or "menu" to get back to the main menu) ').strip()
        
        if word == 'menu':
            break
        
        print(' currently applicable modes: ' + str([m for m in vb.Modes]))
        mode = input(' which mode to apply? ').strip()
        args.append([mode])
        
        print(' currently appliable tenses: ' + str([t for t in vb.Tenses]))        
        tense = input(' which tense to apply? ').strip()
        person = input(' which person? supply an index from 0 - 5 ').strip()
        args.append([tense, int(person)])
        
        print(' summary: mode {} for verb {} in tense {} for person {}'.format(mode, word, tense, person))
        print(args)
        print(' constructed verb: ', vb.construct(word, args))

    # called if while() was broken
    __app_as_cli__()

    
def __constructNoun__():
    """ 
    
    """
    from python.languaid.core.lang.noun import Noun
    
    print(' constructNoun called ')
    
    no = Noun()
    
    while(True):
        args = []
        word = input(' >> enter a noun to declin (or "menu" to get back to the main menu) ').strip()
        
        if word == 'menu':
            break
        
        print(' currently appliable modes: ' + str([e for e in no.Modes]))
        mode = input(' which mode to apply? ').strip()
        # args.append([mode])
        
        if mode in no.Modes:
            person = input(' which person? supply an index from 0 - 5 ').strip()
            args.append([mode, int(person)])
        else:
            args.append([mode])
            
        print(' currently appliable numbers: ' + str([e for e in no.Number]))        
        number = input(' which number to apply? ').strip()
        args.append([number])
        
        print(' summary: mode {} for noun {} with number {} (for person {})'.format(mode, word, number, person))
        print(args)
        print(' constructed noun: ', no.construct(word, args))

    # called if while() was broken
    __app_as_cli__()


def __translate__():
    """ """
    import python.languaid.core.lang.translate as tr

    print(' translate called ')

    while(True):
        word = input(
            '>> enter a word to translate (or "menu" to get back to the main menu) ').strip()

        if word == 'menu':
            break

        source = input('source language?').strip()
        target = input('target language?').strip()

        print('summary: {}, from {} to {}'.format(word, source, target))
        print('translation: ', tr.translate(word, source, target))

    # called if while() was broken
    __app_as_cli__()


def __check__():
    """ """
    from python.languaid.core.util.util import deconstruct

    print(' check called ')

    while(True):
        word = input(
            '>> enter a word to check (or "menu" to get back to the main menu) ').strip()

        if word == 'menu':
            break

        wtype = input('Type (verb, noun)?').strip()
        wtype = wtype.lower()

        print('summary: {}, from {} to {}'.format(word, wtype))
        print('deconstruction: ', str(deconstruct(word, wtype)))

    # called if while() was broken
    __app_as_cli__()


def __exit__(self, exception_type, exception_value, traceback):
    """
        @summary: Basically ends the application
        @param exception_type:
        @param exception_value:
        @param traceback: 
    """
    import sys
    
    print(' Goodbye! Görüşürüz!')
    sys.exit(0)


if __name__ == '__main__':
    loader()
