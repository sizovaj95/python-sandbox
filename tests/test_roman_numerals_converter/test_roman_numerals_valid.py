from unittest import TestCase

import roman_numerals


class TestValidRomanNumerals(TestCase):
    def test_1(self):
        roman = 'XI'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(11, result)

    def test_2(self):
        roman = 'V'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(5, result)

    def test_3(self):
        roman = 'IX'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(9, result)

    def test_4(self):
        roman = 'MCMXC'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(1990, result)

    def test_5(self):
        roman = 'MMVIII'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(2008, result)

    def test_6(self):
        roman = 'MDCLXVI'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(1666, result)

    def test_7(self):
        roman = 'III'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(3, result)

    def test_8(self):
        roman = 'MMXXII'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(2022, result)

    def test_9(self):
        roman = 'MMMCMXCIX'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(3999, result)

    def test_10(self):
        roman = 'CDL'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(450, result)

    def test_11(self):
        roman = 'XIV'
        result = roman_numerals.convert_roman_numeral_to_integer(roman)
        self.assertEqual(14, result)
