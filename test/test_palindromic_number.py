
#!/usr/bin/env python

# By Saurabh Katkar

import unittest
import logging

from mock import MagicMock 

logging.getLogger().setLevel(logging.INFO)
    
class PalindromicNumberTest(unittest.TestCase):
    
    def _getTargetClass(self):
        from app.palindromic_number import PalindromicNumber
        return PalindromicNumber
    
    def setUp(self):
        self.number = 267        
        self.processor = self._getTargetClass()(self.number)
        
    def test_getBitRepresentation(self):
        a = self.processor.getBitRepresentation(self.number, 4)
        self.assertEqual(a, '10023')
        self.assertRaises(ValueError, self.processor.getBitRepresentation, str(self.number), 4)
        
    def test_getPalindrome(self):
        a = self.processor.getPalindrome(2,36)
        self.assertEqual(a, (self.number,14))
        self.processor.getBitRepresentation = MagicMock(return_value = '12021')
        mock_a = self.processor.getPalindrome(2,36)
        self.assertEqual(mock_a, (self.number, 2))
        self.assertRaises(ValueError, self.processor.getPalindrome, 1, 44)
        
    def tearDown(self):
        logging.info('\n*** Finished Test %s ***\n', self.id().split('.')[-1])
        
        
if __name__ == "__main__":
    unittest.main()
