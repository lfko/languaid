'''
    Created on Dec 3, 2018

    @author: fb
    @summary: purposed main entry class of the application
'''


def app_as_gui():
    """ 
        load the application with the tkinter gui
    """


def app_as_cli():
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
    from lfko.python.languaid.core.lang.verb import Verb
    
    print(' constructVerb called ')

    vb = Verb()
    
    while(True):
        args = []
        word = input(' >> enter a verb to conjugate (or "menu" to get back to the main menu) ').strip()
        
        if word == 'menu':
            break
        
        print(' currently appliable modes: ' + str([e.name for e in vb.Modes]))
        mode = input(' which mode to apply? ').strip()
        args.append([mode])
        
        print(' currently appliable tenses: ' + str([e.name for e in vb.Tenses]))        
        tense = input(' which tense to apply? ').strip()
        person = input(' which person? supply an index from 0 - 5 ').strip()
        args.append([tense, int(person)])
        
        print(' summary: mode {} for verb {} in tense {} for person {}'.format(mode, word, tense, person))
        print(args)
        print(' constructed verb: ', vb.construct(word, args))

    # called if while() was broken
    app_as_cli()

    
def __constructNoun__():
    """ 
    
    """
    from lfko.python.languaid.core.lang.noun import Noun
    
    print(' constructNoun called ')
    
    no = Noun()
    
    while(True):
        args = []
        word = input(' >> enter a noun to declin (or "menu" to get back to the main menu) ').strip()
        
        if word == 'menu':
            break
        
        print(' currently appliable modes: ' + str([e.name for e in no.Modes]))
        mode = input(' which mode to apply? ').strip()
        # args.append([mode])
        
        if mode == no.Modes.possession.name:
            person = input(' which person? supply an index from 0 - 5 ').strip()
            args.append([mode, int(person)])
        else:
            args.append([mode])
            
        print(' currently appliable numbers: ' + str([e.name for e in no.Number]))        
        number = input(' which number to apply? ').strip()
        args.append([number])
        
        print(' summary: mode {} for noun {} with number {} (for person {})'.format(mode, word, number, person))
        print(args)
        print(' constructed noun: ', no.construct(word, args))

    # called if while() was broken
    app_as_cli()


def __translate__():
    """ """
    import lfko.python.languaid.core.lang.translate as tr

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
    app_as_cli()


def __check__():
    pass


def __exit__():
    """
    
    """
    import sys
    
    print(' Goodbye! Görüşürüz!')
    sys.exit(0)


if __name__ == '__main__':
    # app_as_gui()
    app_as_cli()
