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
        # nb.grid(row=0, column=0, columnspan=5, rowspan=2)
        nb.pack(expand=1, fill="both")

        welcome_frame = ttk.Frame(nb, borderwidth=5, relief="sunken", width=200, height=100)
        # welcome_frame.grid(column=0, row=0, columnspan=3, rowspan=2)
        welcome_frame.pack()

        verb_frame = ttk.Frame(nb, borderwidth=5, relief="sunken", width=200, height=100)
        verb_frame.pack()  # makes the frame visible
        
        noun_frame = ttk.Frame(nb, borderwidth=5, relief="sunken", width=200, height=100)
        noun_frame.pack()
        
        trans_frame = ttk.Frame(nb, borderwidth=5, relief="sunken", width=200, height=100)
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
        l = tkinter.Label(welcome_frame, text="Welcome to the LanguAid application!")
        # .pack(side=tkinter.TOP)  # resizes itself
        # exit_button = tkinter.Button(welcome_frame, text='Exit', fg='red', command=nb.quit)
        # exit_button.pack(side=tkinter.LEFT)
        about_button = tkinter.Button(welcome_frame, text='About', fg='blue', command=self.__printAbout__)
        # about_button.pack(side=tkinter.LEFT)
        
        l.grid(row=0, column=0)
        # exit_button.grid(row=1, column=1)
        about_button.grid(row=1, column=0)
        
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
        input_group = tkinter.LabelFrame(verb_frame)
        input_group.grid(row=0, column=0)
        l = tkinter.Label(input_group, text='Enter your word here', font=("Helvetica", 12))
        l.grid(row=0, column=0, padx=5, pady=5)

        self.input_verb = tkinter.Entry(input_group)
        self.input_verb.grid(row=0, column=1)
        # self.input_verb.pack()
        
        self.tense_buttons = []
        self.mode_buttons = []
        self.number_buttons = []
        
        # RadioButton for selecting if infintive should be constructed
        self.v_tense = tkinter.StringVar()
        self.infintive_rButton = tkinter.Checkbutton(verb_frame, variable=self.v_tense, onvalue='infinitive', text='infinitive', command=self.__change_state__)
        self.infintive_rButton.grid(row=1, column=0)
        # self.infintive_rButton.pack()
        
        mode_group = tkinter.LabelFrame(verb_frame, text="Mode")
        mode_group.grid(row=2, column=0)
        self.v_mode = tkinter.StringVar()
        for i, mode in enumerate(self.gc.verb_modes):
            c = tkinter.Radiobutton(mode_group, variable=self.v_mode, value=mode, text=mode, command=self.__change_state__)
            c.grid(row=2, column=i)
            # c.pack()
            self.mode_buttons.append(c)
        
        tense_group = tkinter.LabelFrame(verb_frame, text="Tense")
        tense_group.grid(row=3, column=0)
        for i, tense in enumerate(self.gc.verb_tenses):
            c = tkinter.Radiobutton(tense_group, variable=self.v_tense, value=tense, text=tense)
            c.grid(row=3, column=i)
            # c.pack(anchor=tkinter.W)
            self.tense_buttons.append(c)
        
        person_group = tkinter.LabelFrame(verb_frame, text="Tense")
        person_group.grid(row=4, column=0)
        self.v_number = tkinter.IntVar()
        for i in range(6):
            c = tkinter.Radiobutton(person_group, variable=self.v_number, value=i, text=i + 1)
            c.grid(row=4, column=i)
            # c.pack()
            self.number_buttons.append(c)
        
        btn_group = tkinter.LabelFrame(verb_frame)
        btn_group.grid(row=5, column=0)
        self.build_verb_button = tkinter.Button(btn_group, text='Build verb', command=self.__constructVerb__)
        self.build_verb_button.grid(row=5, column=0)
        # self.build_verb_button.pack(side=tkinter.BOTTOM)
        self.check_verb_button = tkinter.Button(btn_group, text='Check verb', command=self.__checkVerb__)
        self.check_verb_button.grid(row=5, column=1)
        # self.check_verb_button.pack(side=tkinter.BOTTOM)
        self.reset_verb_button = tkinter.Button(btn_group, text='Reset', command=self.__reset__)
        self.reset_verb_button.grid(row=5, column=2)
        # self.reset_verb_button.pack(side=tkinter.BOTTOM)
        
        self.outVerb = tkinter.StringVar()  # binding a StringVar to the label, so we just have to upate the variable
        self.output_verb = tkinter.Label(verb_frame, text='Verb will go here!', textvariable=self.outVerb)
        self.output_verb.grid(row=1, column=1)
        # .pack(side=tkinter.BOTTOM)
        
    def __initTranslateFrame__(self, trans_frame):
        '''
            @summary: Translate Frame
            @param trans_frame: Frame
        '''
        input_group = tkinter.LabelFrame(trans_frame)
        input_group.grid(row=0, column=0)
        l = tkinter.Label(input_group, text='Enter your word here', font=("Helvetica", 12))
        l.grid(row=0, column=0, padx=5, pady=5)
        self.trans_entry = tkinter.Entry(input_group)
        self.trans_entry.grid(row=0, column=1)
        # self.trans_entry.pack()
        self.translate_button = tkinter.Button(trans_frame, text='Translate', font=("Helvetica", 12), command=self.__translate__)
        self.translate_button.grid(row=2, column=0)

        self.lang_opt = tkinter.IntVar()
        
        rBtn_group = tkinter.LabelFrame(trans_frame)
        rBtn_group.grid(row=1, column=0)
        tkinter.Radiobutton(rBtn_group, text="tr <> en", variable=self.lang_opt, value=0).grid(row=1, column=0)
        # .pack(anchor=tkinter.W)
        tkinter.Radiobutton(rBtn_group, text="en <> tr", variable=self.lang_opt, value=1).grid(row=1, column=1)
        # .pack(anchor=tkinter.W)
        self.outTrans = tkinter.StringVar()
        self.word_label = tkinter.Label(trans_frame, text="Helvetica", textvariable=self.outTrans, font=("Helvetica", 16))
        self.word_label.grid(row=4, column=1)
    
    def __initNounFrame__(self, noun_frame):
        '''
            @summary: Noun Frame; There are some special fields, which need to be initialised separately
            @param noun_frame: Frame
        '''
        input_group = tkinter.LabelFrame(noun_frame)
        input_group.grid(row=0, column=0)
        l = tkinter.Label(input_group, text='Enter your word here', font=("Helvetica", 12))
        l.grid(row=0, column=0, padx=5, pady=5)

        self.input_noun = tkinter.Entry(input_group)
        self.input_noun.grid(row=0, column=1)
        # self.input_noun.pack()
        group = tkinter.LabelFrame(noun_frame, text="Mode", padx=5, pady=5)
        group.grid(row=1, column=0)
        self.n_mode = tkinter.StringVar()
        for i, mode in enumerate(self.gc.noun_modes):
            tkinter.Radiobutton(group, text=mode, value=mode, variable=self.n_mode).grid()
            
        # singular or plural
        self.n_number = tkinter.StringVar()
        # for number in self.gc.noun_number:
        # tkinter.Radiobutton(noun_frame, text='plural', value='plural', variable=self.n_number).pack()
        
        group2 = tkinter.LabelFrame(noun_frame, text="Person")
        group2.grid(row=3, column=0)
        self.person_number = tkinter.IntVar()
        for i in range(6):
            tkinter.Radiobutton(group2, variable=self.person_number, value=i, text=i + 1).grid(row=3, column=i)
            # self.person_number_rbutton.pack(anchor=tkinter.E)
        
        btn_group = tkinter.LabelFrame(noun_frame)
        btn_group.grid(row=4, column=0)
        self.build_verb_button = tkinter.Button(btn_group, font=("Helvetica", 12), text='Build noun', command=self.__constructNoun__)
        self.build_verb_button.grid(row=4, column=0)
        # self.build_verb_button.pack(side=tkinter.BOTTOM)
        self.check_verb_button = tkinter.Button(btn_group, font=("Helvetica", 12), text='Check noun', command=self.__checkNoun__)
        self.check_verb_button.grid(row=4, column=1)
        # self.check_verb_button.pack(side=tkinter.BOTTOM)
        
        self.outNoun = tkinter.StringVar()  # binding a StringVar to the label, so we just have to upate the variable
        self.output_noun = tkinter.Label(noun_frame, text='Noun will go here!', font=("Helvetica", 16), textvariable=self.outNoun)
        self.output_noun.grid(row=1, column=1)
        # .pack(side=tkinter.RIGHT)

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
        self.outTrans.set(trans_word)
        # self.trans_entry.delete(0, tkinter.END) 
    
    def __constructNoun__(self):
        '''
            @summary: function for calling the controller to construct a noun
        '''
        args = []
        if self.n_number.get() != '':
            args = [['number', self.n_number.get()]]
        if self.n_mode.get() != '':
            args.append(['mode', self.n_mode.get(), self.person_number.get()])
        
        try:
            self.outNoun.set(self.gc.constructNoun(self.input_noun.get(), args))
        except TypeError:
            messagebox.showwarning('Warning', 'Not enough parameters supplied!')
        # self.person_number_rbutton.deselect()
        
    def __constructVerb__(self):
        '''
            @summary: function for calling the controller to construct a verb
        '''
        args = []
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
root.geometry("400x250")
mainGui = LanguaidGUI(root)

# starts the actual execution
# mainloop will be executed indefinetly long, until we close the window
root.mainloop()
