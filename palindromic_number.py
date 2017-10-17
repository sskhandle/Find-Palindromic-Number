import string
def getBitRep(n, base):
    if n < base:
        if n >= 10:
            return string.ascii_uppercase[n%10]
        return str(n)
    else:
        a = string.ascii_uppercase[(n%base)%10] if (n%base) >= 10 else str(n%base)
        return getBitRep(n // base, base) + a
        
print getBitRep(576,11)


def getPalindrome(n):
    for i in range(2, 37):
        bit_str = getBitRep(n,i)
        if bit_str == bit_str[::-1]:
            return n, i

print getPalindrome(20)