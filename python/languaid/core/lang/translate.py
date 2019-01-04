'''
    Created on Dec 3, 2018

    @author: fb
    @summary: 
'''
import urllib.request
import urllib.parse
import json

from lfko.python.languaid.core.util.settings import Settings
from urllib.error import URLError


def translate(word, sourceLang, targetLang):
    """ 
        @summary: default constructor
    """
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
    
    url = Settings().getValue('TRANSLATE', 'URL')
    url = url.format(source, target, urllib.parse.quote_plus(word))
    # url = 'http://cevir.ws/vl?q=' + word + '&m=25&p=both&l' + target
    # free Google Translate API (without developer registration)
    # url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + source + '&tl=' + \
    #    target + '&dt=t&q=' + urllib.parse.quote_plus(word)

    print(' open url to translation service: ', url)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    # TODO add timeout
    try:
        resp = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(resp) as response:
            raw_data = response.read()
    except URLError:
        print('Something went wrong.')
        
    json_data = json.loads(raw_data.decode())

    # TODO what to return here?
    return json_data[0][0][0]
