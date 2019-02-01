'''
    Created on Dec 3, 2018

    @author: lfko
    @summary: modul implementing the main GUI for the application
'''

import tkinter
from tkinter import messagebox, ttk


class LanguaidGUI():
    """
    """
    
    def __init__(self, master):
        """
            @summary: Constructor; initialises required GUI components
            @param master: root widget
        """
                
        nb = ttk.Notebook(master)
        nb.grid(row=10, column=10, columnspan=50, rowspan=49, sticky='NESW')

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
        
        '''
            Welcome Frame
        '''
        # add a child widget to the frame (its root)
        tkinter.Label(welcome_frame, text="Welcome to the LanguAid application!").pack(side=tkinter.TOP)  # resizes itself
        tkinter.Button(welcome_frame, text='Exit', fg='red', command=nb.quit).pack(side=tkinter.LEFT)
        tkinter.Button(welcome_frame, text='About', fg='blue', command=self.__printAbout__).pack(side=tkinter.LEFT)
        
        # frame internally stores references to all its child widgets - so no problem arises here, if we get out of focu
        
        '''
            Translate Frame
        '''
        
        self.trans_entry = tkinter.Entry(trans_frame)
        self.trans_entry.pack()
        self.test_button = tkinter.Button(trans_frame, text='Translate', command=self.__translate__)
        self.test_button.pack(side=tkinter.BOTTOM)

        self.lang_opt = tkinter.IntVar()
        
        tkinter.Radiobutton(trans_frame, text="tr <> en", variable=self.lang_opt, value=0).pack(anchor=tkinter.W)
        tkinter.Radiobutton(trans_frame, text="en <> tr", variable=self.lang_opt, value=1).pack(anchor=tkinter.W)
        
        """
        menu = tkinter.Menu(master)
        master.config(menu=menu)  # attach the menu to the root
        
        options_menu = tkinter.Menu(menu)
        menu.add_cascade(label='Options', menu=options_menu)  # pulldown menu
        options_menu.add_command(label='Translate', command=self.__translate__)
        options_menu.add_separator()
        # options_menu.add_command(label='Translate', self.__translate__)
        options_menu.add_command(label='Construct a verb', command=self.__constructVerb__)
        
        helpmenu = tkinter.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.__printAbout__)
        """

    def __printAbout__(self):
        """
        """
        messagebox.showinfo('About', 'LanguAid version 1.0, author Florian Becker (885187), http://github.com/lfko')
    
    def __constructVerb__(self):
        """
        """
    
    def __translate__(self):
        """
            @summary: 
        """
        import python.languaid.core.lang.translate as tr
        
        lang_opts = [['tr', 'en'], ['en', 'tr']]

        input_word = self.trans_entry.get()
        
        trans_word = tr.translate(input_word, lang_opts[self.lang_opt.get()][0], lang_opts[self.lang_opt.get()][1])

        messagebox.showinfo('Translation', input_word + ' -> ' + trans_word)
        self.trans_entry.delete(0, tkinter.END) 


# root window widget - must be generated before anything else
root = tkinter.Tk()
mainGui = LanguaidGUI(root)

# starts the actual execution
# mainloop will be executed indefinetly long, until we close the window
root.mainloop()
# root.destroy()
