from unittest import TestCase

from roman_numerals import convert_roman_numeral_to_integer


class TestInvalidRomanNumerals(TestCase):
    def test_1(self):
        roman = 'LD'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_2(self):
        roman = 'IIIX'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_3(self):
        roman = 'LID'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_4(self):
        roman = 'VIIIXI'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_5(self):
        roman = 'IIX'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_6(self):
        roman = 'VV'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_7(self):
        roman = 'GIII'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_8(self):
        roman = 'IIII'
        result = convert_roman_numeral_to_integer(roman)
        self.assertIsNone(result)

    def test_9(self):
        with self.assertRaises(ValueError):
            convert_roman_numeral_to_integer('')

    def test_11(self):
        with self.assertRaises(ValueError):
            convert_roman_numeral_to_integer(None)
