import string


class PalindromicNumber(object):
    
    def __init__(self, number):
        self.number = number


    def getBitRepresentation(self, n, base):
        if n <= 0 or n > 1000:
            raise ValueError("Invalid input. Please enter a positive integer between 1 and 1000")
        if n < base:
            if n >= 10:
                return string.ascii_uppercase[n%10]
            return str(n)
        else:
            a = string.ascii_uppercase[(n%base)%10] if (n%base) >= 10 else str(n%base)
            return self.getBitRepresentation(n // base, base) + a
    
    
    def getPalindrome(self):
        for i in range(2, 37):
            bit_str = self.getBitRepresentation(self.number,i)
            if bit_str == bit_str[::-1]:
                return self.number, i


if __name__ == "__main__":
    palindrome = PalindromicNumber("89")
    print palindrome.getPalindrome()