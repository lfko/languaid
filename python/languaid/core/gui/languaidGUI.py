'''
    Created on Dec 3, 2018

    @author: lfko
    @summary: modul implementing the main GUI for the application
'''

import tkinter
from tkinter import messagebox, ttk
from python.languaid.core.gui.languaidGuiController import GuiController 


class LanguaidGUI():
    """
    """
    
    def __init__(self, master):
        """
            @summary: Constructor; initialises required GUI components
            @param master: root widget
        """
        self.lang_opts = [['tr', 'en'], ['en', 'tr']]
        self.gc = GuiController()
                
        nb = ttk.Notebook(master)
        nb.grid(row=10, column=10, columnspan=50, rowspan=49)

        welcome_frame = ttk.Frame(nb)
        welcome_frame.pack()

        verb_frame = ttk.Frame(nb)
        verb_frame.pack()  # makes the frame visible
        
        noun_frame = ttk.Frame(nb)
        noun_frame.pack()
        
        trans_frame = ttk.Frame(nb)
        trans_frame.pack()
        
        # adding the separate frames as tabs to the notebook widget
        nb.add(welcome_frame, text='Start')
        nb.add(verb_frame, text='Verbs')
        nb.add(noun_frame, text='Nouns')
        nb.add(trans_frame, text='Translator')
        self.__initVerbFrame__(verb_frame)
        self.__initTranslateFrame__(trans_frame)
        self.__initNounFrame__(noun_frame)
        '''
            Welcome Frame
        '''
        # add a child widget to the frame (its root)
        tkinter.Label(welcome_frame, text="Welcome to the LanguAid application!").pack(side=tkinter.TOP)  # resizes itself
        tkinter.Button(welcome_frame, text='Exit', fg='red', command=nb.quit).pack(side=tkinter.LEFT)
        tkinter.Button(welcome_frame, text='About', fg='blue', command=self.__printAbout__).pack(side=tkinter.LEFT)
        
        # frame internally stores references to all its child widgets - so no problem arises here, if we get out of focus

    def __initVerbFrame__(self, verb_frame):
        '''
            @summary: Verb Frame; There are some special fields, which need to be initialised separately
        '''

        self.input_verb = tkinter.Entry(verb_frame)
        self.input_verb.pack()
        
        self.mode_vars = []
        self.v_mode = tkinter.StringVar()
        for mode in self.gc.verb_modes:
            # tkinter.Checkbutton(verb_frame, text=mode, variable=self.gc.verb_modes[i]).pack()
            tkinter.Radiobutton(verb_frame, variable=self.v_mode, value=mode, text=mode).pack(anchor=tkinter.E)
            self.mode_vars.append(self.v_mode)
        
        self.v_tense = tkinter.StringVar()
        for tense in self.gc.verb_tenses:
            tkinter.Radiobutton(verb_frame, variable=self.v_tense, value=tense, text=tense).pack(anchor=tkinter.W)
        
        self.build_verb_button = tkinter.Button(verb_frame, text='Build verb', command=self.__constructVerb__)
        self.build_verb_button.pack(side=tkinter.BOTTOM)
        # self.check_verb_button = tkinter.Button(verb_frame, text='Check verb', command=self.gc.checkVerb)
        # self.check_verb_button.pack(side=tkinter.BOTTOM)
        
        self.outVerb = tkinter.StringVar()  # binding a StringVar to the label, so we just have to upate the variable
        self.output_verb = tkinter.Label(verb_frame, text='Verb will go here!', textvariable=self.outVerb).pack(side=tkinter.BOTTOM)
        
    def __initTranslateFrame__(self, trans_frame):
        '''
            @summary: Translate Frame
        '''
        
        self.trans_entry = tkinter.Entry(trans_frame)
        self.trans_entry.pack()
        self.translate_button = tkinter.Button(trans_frame, text='Translate', command=self.__translate__)
        self.translate_button.pack(side=tkinter.BOTTOM)

        self.lang_opt = tkinter.IntVar()
        
        tkinter.Radiobutton(trans_frame, text="tr <> en", variable=self.lang_opt, value=0).pack(anchor=tkinter.W)
        tkinter.Radiobutton(trans_frame, text="en <> tr", variable=self.lang_opt, value=1).pack(anchor=tkinter.W)
    
    def __initNounFrame__(self, noun_frame):
        '''
            @summary: Noun Frame; There are some special fields, which need to be initialised separately
        '''

        self.input_noun = tkinter.Entry(noun_frame)
        self.input_noun.pack()
        
        for i, mode in enumerate(self.gc.noun_modes):
            self.gc.noun_modes[i] = tkinter.Variable()
            l = tkinter.Checkbutton(noun_frame, text=mode, variable=self.gc.noun_modes[i])
            l.pack()
        
        self.build_verb_button = tkinter.Button(noun_frame, text='Build noun', command=self.__constructNoun__)
        self.build_verb_button.pack(side=tkinter.BOTTOM)
        # self.check_verb_button = tkinter.Button(noun_frame, text='Check noun', command=self.gc.checkVerb)
        # self.check_verb_button.pack(side=tkinter.BOTTOM)
        
        self.outNoun = tkinter.StringVar()  # binding a StringVar to the label, so we just have to upate the variable
        self.output_noun = tkinter.Label(noun_frame, text='Noun will go here!', textvariable=self.outNoun).pack(side=tkinter.RIGHT)

    def __printAbout__(self):
        '''
        '''
        messagebox.showinfo('About', 'LanguAid version 1.0, author Florian Becker (885187), http://github.com/lfko')
    
    def __translate__(self):
        '''
            @summary: Calls the controller for the translation of the inputted word and shows the result in a messagebox
        '''
        trans_word = self.gc.translate(self.trans_entry.get(), self.lang_opts[self.lang_opt.get()][0], self.lang_opts[self.lang_opt.get()][1])
        messagebox.showinfo('Translation', self.trans_entry.get() + ' -> ' + trans_word)
        self.trans_entry.delete(0, tkinter.END) 
    
    def __constructNoun__(self):
        '''
        '''
        self.outNoun = self.gc.constructNoun()
        
    def __constructVerb__(self):
        '''
        '''
        if(self.v_mode.get() == '' or self.v_tense.get() == ''):
            messagebox.showwarning('Warning', 'Not enough parameters supplied!')
        else:
            args = [[self.v_tense.get(), 0], [self.v_mode.get()]]
            self.outVerb = self.gc.constructVerb(self.input_verb.get(), args)


# root window widget - must be generated before anything else
root = tkinter.Tk()
mainGui = LanguaidGUI(root)

# starts the actual execution
# mainloop will be executed indefinetly long, until we close the window
root.mainloop()
# root.destroy()
