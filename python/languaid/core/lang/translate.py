'''
    Created on Dec 3, 2018

    @author: fb
    @summary: Module used to call a translation API for translating words
'''
import urllib.request
import urllib.parse
import json

from python.languaid.core.util.settings import Settings
from urllib.error import URLError


def translate(word, sourceLang, targetLang):

    if(None in (word, sourceLang, targetLang) or '' in (word, sourceLang, targetLang)):
        raise ValueError('At least one argument is missing!')
    
    print(' translating word {} to target language {}'.format(
        word, sourceLang, targetLang))
    return __openUrl__(word, sourceLang, targetLang)


def __openUrl__(word, source, target):
    """ 
        @summary: creates and opens the url to retrieve the translation
        @param word: the word to translate
        @param source: source language (e.g. 'en')
        @param target: target language (e.g. 'tr')
        @return: translation of the word as string
    """
    json_data = None
    ret = None
    
    url = Settings().getValue('TRANSLATE', 'URL')
    url = url.format(source, target, urllib.parse.quote_plus(word))

    print(' open url to translation service: ', url)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}

    try:
        resp = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(resp) as response:
            raw_data = response.read()
        
        # translate the raw data to a json representation    
        json_data = json.loads(raw_data.decode())
        ret = json_data[0][0][0]  # nested json data: return the actual translation string
    except URLError as err:
        print('Something went wrong: {0}'.format(err))
    
    return ret  
