'''
    Created on Dec 27, 2018

    @author: fb
    @summary: unit tests for noun construction/deconstruction
    @see: lfko.python.languaid.core.lang.noun.py
'''

import unittest
from lfko.python.languaid.core.lang.noun import Noun
from lfko.python.languaid.core.util.enums import Enums


class LangCoreNounTest(unittest.TestCase):
    '''
    
    '''
    
    def testFaultTolerance(self):
        """
        
        """
        nn = Noun()
        with self.assertRaises(TypeError):
            nn.construct(None, None)
            nn.construct('', [])
            nn.construct('STRING', [])
            nn.construct('', ['STRING'])
        
    def testVerbConstruct(self):
        """ 
        
        """
        nn = Noun()
        self.assertEquals(nn.construct(noun='canta', args=[['number', Enums().Number.plural.name]]), 'cantalar')
        self.assertEquals(nn.construct(noun='canta', args=[['mode', Enums().Modes.possession.name, 1]]), 'cantan')
        self.assertEquals(nn.construct(noun='fotoğraf makine', args=[['mode', Enums().Modes.possession.name, 2]]), 'fotoğraf makinesi')
        
        self.assertEquals(nn.construct(noun='kız', args=[['mode', Enums().Modes.possession.name, 0]]), 'kızım')
        self.assertEquals(nn.construct(noun='kız', args=[['mode', Enums().Modes.possession.name, 1]]), 'kızın')
        self.assertEquals(nn.construct(noun='kız', args=[['mode', Enums().Modes.possession.name, 2]]), 'kızı')
        self.assertEquals(nn.construct(noun='kız', args=[['mode', Enums().Modes.possession.name, 3]]), 'kızımız')
        self.assertEquals(nn.construct(noun='kız', args=[['mode', Enums().Modes.possession.name, 4]]), 'kızınız')
        self.assertEquals(nn.construct(noun='kız', args=[['mode', Enums().Modes.possession.name, 5]]), 'kızları')
        
        self.assertEquals(nn.construct(noun='otobüs', args=[['mode', Enums().Modes.possession.name, 0]]), 'otobüsüm')
        self.assertEquals(nn.construct(noun='otobüs', args=[['mode', Enums().Modes.possession.name, 1]]), 'otobüsün')
        self.assertEquals(nn.construct(noun='otobüs', args=[['mode', Enums().Modes.possession.name, 2]]), 'otobüsü')
        self.assertEquals(nn.construct(noun='otobüs', args=[['mode', Enums().Modes.possession.name, 3]]), 'otobüsümüz')
        self.assertEquals(nn.construct(noun='otobüs', args=[['mode', Enums().Modes.possession.name, 4]]), 'otobüsünüz')
        self.assertEquals(nn.construct(noun='otobüs', args=[['mode', Enums().Modes.possession.name, 5]]), 'otobüsleri')

    def testNounDeconstruct(self):
        """ 
        
        """
        from lfko.python.languaid.core.util.util import deconstruct
        print(deconstruct('otobüsleri', 'noun'))


if __name__ == "__main__": 
    unittest.main()
