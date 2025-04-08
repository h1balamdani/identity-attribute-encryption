from charm.core.math.integer import integer
from charm.toolbox.bitstring import Bytes
import math

# Assuming Conversion class is already defined as you provided
class Conversion(object):
    '''
    The goal is to convert arbitrarily between any of the following types
    
    Input types:
    
    * bytes
    * Bytes
    * int
    * Integer Element
    * Modular Integer Element
    
    Output types:
    
    * int
    * Group element
    * Integer element
    * Integer element mod N
    '''
    @classmethod
    def bytes2integer(self, bytestr):
        '''Converts a bytes string to an integer object'''
        return integer(bytestr)

    @classmethod    
    def OS2IP(self, bytestr, element=False):
        '''
        :Return: A python ``int`` if element is False. An ``integer.Element`` if element is True
        
        Converts a byte string to an integer
        '''
        val = 0 
        for i in range(len(bytestr)):
            byt = bytestr[len(bytestr)-1-i]
            val += byt << (8 *i)

        if element:
            return integer(val)  # Return as integer.Element
        else:
            return val  # Return as Python int

    @classmethod
    def int2bin(self, intobj):
        _str = bin(int(intobj))
        _array = []
        for i in range(2, len(_str)):
            _array.append(int(_str[i])) 
        return _array

    @classmethod    
    def IP2OS(self, number, xLen=None):
        '''
        :Parameters:
          - ``number``: is a normal integer, not modular
          - ``xLen``: is the intended length of the resulting octet string
        
        Converts an integer into a byte string'''
        
        ba = bytearray()
        x = number
        if xLen == None:
            xLen = int(math.ceil(math.log(x, 2) / 8.0))
            
        for i in range(xLen):
            ba.append(x % 256)
            x = x >> 8
        ba.reverse()
        return Bytes(ba)

# Create an instance of the Conversion class


# # Example Python int
# python_int = 12345

def integer_element(python_int):
    convert = Conversion()

    # Option 1: Convert Python int to byte string and then use OS2IP to convert to integer.Element
    byte_string = convert.IP2OS(python_int)
    integer_element_1 = convert.OS2IP(byte_string, element=True)

    return integer_element_1
# # Option 2: Convert Python int directly to bytes and then use bytes2integer
# byte_string_2 = python_int.to_bytes((python_int.bit_length() + 7) // 8, 'big')  # Convert int to byte string
# integer_element_2 = convert.bytes2integer(byte_string_2)
# print("Converted integer.Element using bytes2integer method:", integer_element_2)


