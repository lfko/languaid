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
        @summary: GUI class using tkinter
    """
    
    def __init__(self, master):
        """
            @summary: Constructor; initialises required GUI components
            @param master: root widget
        """
        self.lang_opts = [['tr', 'en'], ['en', 'tr']]
        self.gc = GuiController()
                
        nb = ttk.Notebook(master)
        nb.grid(row=5, column=5, columnspan=50, rowspan=49)

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

    def __change_state__(self):
        '''
            @summary: changing state of the mode RadioButtons from disabled to normal and vice versa
        '''
        if(self.v_mode.get() in ['imperative', 'voluntative']):
            for c in self.tense_buttons:
                c.configure(state='disabled')
                c.deselect()
            for c in self.number_buttons:
                c.configure(state='disabled')
                c.deselect()
                
            self.v_number.set(0)
        else:
            for c in self.tense_buttons:
                c.configure(state='normal')
            for c in self.number_buttons:
                c.configure(state='normal')

    def __initVerbFrame__(self, verb_frame):
        '''
            @summary: Verb Frame; There are some special fields, which need to be initialised separately
            @param verb_frame: Frame
        '''

        self.input_verb = tkinter.Entry(verb_frame)
        self.input_verb.pack()
        
        self.tense_buttons = []
        self.mode_buttons = []
        self.number_buttons = []
        
        # RadioButton for selecting if infintive should be constructed
        self.v_tense = tkinter.StringVar()
        self.infintive_rButton = tkinter.Checkbutton(verb_frame, variable=self.v_tense, onvalue='infinitive', text='infinitive', command=self.__change_state__)
        self.infintive_rButton.pack()
        
        self.v_mode = tkinter.StringVar()
        for mode in self.gc.verb_modes:
            c = tkinter.Radiobutton(verb_frame, variable=self.v_mode, value=mode, text=mode, command=self.__change_state__)
            c.pack()
            self.mode_buttons.append(c)
        
        for tense in self.gc.verb_tenses:
            c = tkinter.Radiobutton(verb_frame, variable=self.v_tense, value=tense, text=tense)
            c.pack(anchor=tkinter.W)
            self.tense_buttons.append(c)
        
        self.v_number = tkinter.IntVar()
        for i in range(6):
            c = tkinter.Radiobutton(verb_frame, variable=self.v_number, value=i, text=i)
            c.pack()
            self.number_buttons.append(c)
        
        self.build_verb_button = tkinter.Button(verb_frame, text='Build verb', command=self.__constructVerb__)
        self.build_verb_button.pack(side=tkinter.BOTTOM)
        self.check_verb_button = tkinter.Button(verb_frame, text='Check verb', command=self.__checkVerb__)
        self.check_verb_button.pack(side=tkinter.BOTTOM)
        self.reset_verb_button = tkinter.Button(verb_frame, text='Reset', command=self.__reset__)
        self.reset_verb_button.pack(side=tkinter.BOTTOM)
        
        self.outVerb = tkinter.StringVar()  # binding a StringVar to the label, so we just have to upate the variable
        self.output_verb = tkinter.Label(verb_frame, text='Verb will go here!', textvariable=self.outVerb).pack(side=tkinter.BOTTOM)
        
    def __initTranslateFrame__(self, trans_frame):
        '''
            @summary: Translate Frame
            @param trans_frame: Frame
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
            @param noun_frame: Frame
        '''

        self.input_noun = tkinter.Entry(noun_frame)
        self.input_noun.pack()
        
        self.n_mode = tkinter.StringVar()
        for mode in self.gc.noun_modes:
            tkinter.Radiobutton(noun_frame, text=mode, value=mode, variable=self.n_mode).pack()
            
        # singular or plural
        self.n_number = tkinter.StringVar()
        # for number in self.gc.noun_number:
        tkinter.Radiobutton(noun_frame, text='plural', value='plural', variable=self.n_number).pack()
        
        self.person_number = tkinter.IntVar()
        for i in range(6):
            self.person_number_rbutton = tkinter.Radiobutton(noun_frame, variable=self.person_number, value=i, text=i)
            self.person_number_rbutton.pack(anchor=tkinter.E)
        
        self.build_verb_button = tkinter.Button(noun_frame, text='Build noun', command=self.__constructNoun__)
        self.build_verb_button.pack(side=tkinter.BOTTOM)
        self.check_verb_button = tkinter.Button(noun_frame, text='Check noun', command=self.__checkNoun__)
        self.check_verb_button.pack(side=tkinter.BOTTOM)
        
        self.outNoun = tkinter.StringVar()  # binding a StringVar to the label, so we just have to upate the variable
        self.output_noun = tkinter.Label(noun_frame, text='Noun will go here!', textvariable=self.outNoun).pack(side=tkinter.RIGHT)

    def __printAbout__(self):
        messagebox.showinfo('About', 'LanguAid version 1.0, author Florian Becker (885187), http://github.com/lfko')
    
    def __reset__(self):
        # deselect any selected mode RadioButtons 
        [c.deselect() for c in self.mode_buttons]
    
    def __translate__(self):
        '''
            @summary: Calls the controller for the translation of the inputted word and shows the result in a messagebox
        '''
        trans_word = self.gc.translate(self.trans_entry.get(), self.lang_opts[self.lang_opt.get()][0], self.lang_opts[self.lang_opt.get()][1])
        messagebox.showinfo('Translation', self.trans_entry.get() + ' -> ' + trans_word)
        self.trans_entry.delete(0, tkinter.END) 
    
    def __constructNoun__(self):
        '''
            @summary: function for calling the controller to construct a noun
        '''

        if self.n_number.get() != '':
            args = [['number', self.n_number.get()]]
        if self.n_mode.get() != '':
            args.append(['mode', self.n_mode.get(), self.person_number.get()])
        
        self.outNoun.set(self.gc.constructNoun(self.input_noun.get(), args))
        self.person_number_rbutton.deselect()
        
    def __constructVerb__(self):
        '''
            @summary: function for calling the controller to construct a verb
        '''
        if(self.input_verb.get() == ''):
            messagebox.showwarning('Warning', 'No word has been inputted!')            
        if(self.v_tense.get() == ''):
            messagebox.showwarning('Warning', 'Not enough parameters supplied!')
        else:
            args = [['mode', self.v_mode.get()], ['tense', self.v_tense.get(), self.v_number.get()]]
            self.outVerb.set(self.gc.constructVerb(self.input_verb.get(), args))

    def __checkVerb__(self):
        '''
            @summary: checks the components of a noun
        '''
        messagebox.showinfo('CheckVerb', 'verb consists of the following blocks: ' + str(self.gc.checkWord(self.input_verb.get(), 'verb')))
    
    def __checkNoun__(self):
        '''
            @summary: checks the components of a verb
        '''
        messagebox.showinfo('CheckNoun', 'noun consists of the following blocks: ' + str(self.gc.checkWord(self.input_noun.get(), 'noun')))
        # self.gc.checkWord(self.input_verb.get(), 'noun')


# root window widget - must be generated before anything else
root = tkinter.Tk()
mainGui = LanguaidGUI(root)

# starts the actual execution
# mainloop will be executed indefinetly long, until we close the window
root.mainloop()
