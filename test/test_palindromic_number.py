
import unittest

logger = logging.getLogger(__name__)

class MyModel(object):
    name = 'PalindromicNumberTest'
    

class PalindromicNumberTest(unittest.TestCase):
    
    my_data = {}
    
    def _getTargetClass(self):
        from app.palindromic_number import PalindromicNumber
        return PalindromicNumber
    
    
    def setUp(self):
        self.number = 267        
        self.processor = self._getTargetClass()(MyModel(), self.number)
        
        
    def test_getBitRepresentation(self):
        pass
    
    
    def test_getPalindrome(self):
        pass
        
        
    def tearDown(self):
        logger.info('\n*** Finished Test %s ***\n', self.id().split('.')[-1])
        
        
def main():
    unitTest(headless=True, separateProc=False, runCoverage=False, suppressOutput=False)