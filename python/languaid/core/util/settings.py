'''
    Created on Dec 28, 2018

    @author: fb
    @summary: Class for loading a configuration file and retrieving values from this file
'''

import configparser, pathlib, os
import logging


class Settings():
    
    def __init__(self):
        """ 
            @summary: default constructor
        """
        self.ini_filename = 'settings.ini'
        self.__loadSettings__()

    def __loadSettings__(self, mainDir='/home/lfko/git'):
        """ 
            @summary:
            @param mainDir: main directory of the application
            @todo: conceive a suitable mainDir value
        """
        
        if mainDir == '':
            logging.error('Empty main directory parameter supplied.')
            raise ValueError('Empty main directory parameter supplied.')
        
        if os.path.isdir(mainDir) == False:
            logging.error('Supplied directory name is not a valid directory.')
            raise TypeError('Supplied directory name is not a valid directory.')
        
        ini_dir = pathlib.Path(mainDir + '/python/LanguAid/')
        logging.debug('ini directory ' + str(ini_dir))
        
        # for loop through all files in the specified directory
        for file in ini_dir.iterdir():
            if str(file).find(self.ini_filename) > 0:
                ini_file = file  # settings.ini found
    
        # using the ConfigParser for accessing keys and values inside an ini file
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        
        logging.debug(self.ini_filename + ' loaded ')
    
    def listSections(self):
        """ 
            @summary: list all currently available sections
            @todo: return an actual list
            @return: 
        """
        
        print(self.config.sections())
        
        return []
        
    def listKeys(self, section='DEFAULT'):
        """ 
            @summary: list all keys and corresponding values for a specific section
            @todo: return an actual list
            @return: 
        """
        
        print(self.config.items(section))
        
        return []
    
    def getValue(self, section, key):
        """ 
            @summary: retrieves a value for a given key in a given section
            @param section: specific section of settings
            @param key: key of a specific setting in a specific section
            @return: value for that @key in that @section 
        """
        
        if section == '' or key == '':
            raise ValueError('Wrong or missing parameter supplied.')
        
        # section names and keys are defined in an uppercase manner inside the settings file
        section = section.upper()
        key = key.upper()
        
        logging.debug('loading key {} from section {} '.format(key, section))
        
        return self.config[section][key]
    
