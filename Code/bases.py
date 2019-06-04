import string
import math

hex_dict = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g', '17' : 'h', '18': 'i', '19': 'j', '20': 'k',  '21': 'l', '22': 'm', '23': 'n', '24': 'o', '25': 'p', '26': 'q', '27': 'r', '28': 's', '29': 't', '30': 'u',  '31': 'v', '32': 'w', '33': 'x', '34': 'y', '35': 'z' }

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    result = 0 #Keep a running total
    i = 0
    reversed_digits = digits[::-1]

    for digit in reversed_digits:
        if digit.isalpha():
            for key, value in hex_dict.items():    # 
                    if value == digit:
                        digit = key

        output= (base**i)
        total = int(digit) * output
        result += total
        i += 1    
    return result

def encode(number, base):
    """Encode the given number in base 10 to digits in the given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    output_list = []
    remainder = 0
    
    while number > 0:
        remainder = number % base 

        if remainder > 9:
            remainder = hex_dict[str(remainder)]
        output_list.insert(0, str(remainder))

        quotient = math.floor(number / base)
        number = quotient
        
    return ''.join(output_list)
        
def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    result = decode(digits, base1)
    return encode(result, base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    # print(decode('a', 16))
    print(convert('1010', 2, 16))
