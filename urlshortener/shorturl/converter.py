#!/usr/bin/env python
# encoding: utf-8
BINARY_ALPHABET      = '01'
HEXADECIMAL_ALPHABET = '0123456789ABCDEF'

BASE56_URLSAFE_ALPHABET = ('ABCDEFGHJKLMNPQRSTUVWXYZ'
                           'abcdefghijkmnpqrstuvwxyz'
                           '23456789')
BASE62_URLSAFE_ALPHABET = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           'abcdefghijklmnopqrstuvwxyz'
                           '0123456789')
BASE64_URLSAFE_ALPHABET = BASE62_URLSAFE_ALPHABET + '-_'

class BaseConverter(object):
    decimal_digits = '0123456789'

    def __init__(self, digits, signal='-'):
        self.signal = signal
        self.digits = digits

    def encode(self, string):
        return self.convert(string, self.decimal_digits, self.digits,
                            self.signal)

    def decode(self, string):
        return self.convert(string, self.digits, self.decimal_digits,
                            self.signal)

    def convert(number, fromdigits, todigits, signal):
        if (str(number)[0] == signal):
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
            x = x * len(fromdigits) + fromdigits.index(digit)

        # create the result in base 'len(todigits)'
        if x == 0:
            res = todigits[0]
        else:
            res = ''
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = signal + res
        return res
    convert = staticmethod(convert)

bin = BaseConverter(BINARY_ALPHABET)
hexconv = BaseConverter(HEXADECIMAL_ALPHABET)
base56_urlsafe = BaseConverter(BASE56_URLSAFE_ALPHABET)
base62_urlsafe = BaseConverter(BASE62_URLSAFE_ALPHABET)
base64_urlsafe = BaseConverter(BASE64_URLSAFE_ALPHABET, signal='$')

