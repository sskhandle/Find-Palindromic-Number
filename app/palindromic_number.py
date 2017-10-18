import string
import csv


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
    
    
    def getPalindrome(self, min_base, max_base):
        if min_base < 2 or max_base > 36:
            raise ValueError("Invalid Min / Max Base. The Base value should be between 2 and 36")
        for i in range(min_base, max_base+1):
            bit_str = self.getBitRepresentation(self.number,i)
            if bit_str == bit_str[::-1]:
                return self.number, i
        return (self.number, None)

'''
if __name__ == "__main__":
    palindrome = PalindromicNumber(89)
    print palindrome.getPalindrome(2, 36)
'''    

if __name__ == "__main__":
    input_file = open("input/file.csv", "rb")
    output_file = open("output/file.csv", "wb")

    reader = csv.reader(input_file)
    writer = csv.writer(output_file, delimiter=',')
    writer.writerow(["Decimal", "Smallest Base"])
    row_num = 0
    for row in reader:
        if row_num == 0:
            row_num += 1
            continue
        palindrome = PalindromicNumber(int(row[0]))
        writer.writerow(palindrome.getPalindrome(2,36))
        
    input_file.close()
    output_file.close()
