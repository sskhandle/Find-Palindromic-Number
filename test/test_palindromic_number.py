
import unittest2 as unittest
import logging

# from unittest2.mock import MagicMock

logger = logging.getLogger(__name__)
    
class PalindromicNumberTest(unittest.TestCase):
    
    def _getTargetClass(self):
        from playground.SSK.palindromic_number.app.palindromic_number import PalindromicNumber
        return PalindromicNumber
    
    def setUp(self):
        self.number = 267        
        self.processor = self._getTargetClass()(self.number)
        
    def test_getBitRepresentation(self):
        a = self.processor.getBitRepresentation(self.number, 4)
        self.assertEqual(a, 10023)
        str_a = self.processor.getBitRepresentation(str(self.number), 4)
        self.assertRaises(ValueError, str_a)
        
    def test_getPalindrome(self):
        # self.processor.getBitRepresentation = MagicMock(return_value = 12021)
        a = self.processor.getPalindrome(2,36)
        self.assertEqual(len(a), 2)
        invalid_base_a = self.processor.getPalindrome(1,44)
        self.assertRaises(ValueError, invalid_base_a)
        
    def tearDown(self):
        logger.info('\n*** Finished Test %s ***\n', self.id().split('.')[-1])
        
        
if __name__ == "__main__":
    # unittest.main()
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(PalindromicNumberTest))
