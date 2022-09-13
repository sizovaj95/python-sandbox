from unittest import TestCase

import roman_numerals


class TestRomanNumeral(TestCase):
    def test_1(self):
        roman = 'XI'
        self.assertEqual(11, roman_numerals.convert_to_integer(roman))

    def test_2(self):
        roman = 'V'
        self.assertEqual(5, roman_numerals.convert_to_integer(roman))

    def test_3(self):
        roman = 'IX'
        self.assertEqual(9, roman_numerals.convert_to_integer(roman))

    def test_4(self):
        roman = 'MCMXC'
        self.assertEqual(1990, roman_numerals.convert_to_integer(roman))

    def test_5(self):
        roman = 'MMVIII'
        self.assertEqual(2008, roman_numerals.convert_to_integer(roman))

    def test_6(self):
        roman = 'MDCLXVI'
        self.assertEqual(1666, roman_numerals.convert_to_integer(roman))

    def test_7(self):
        roman = 'III'
        self.assertEqual(3, roman_numerals.convert_to_integer(roman))

    def test_8(self):
        roman = 'GIII'
        self.assertIsNone(roman_numerals.convert_to_integer(roman))

    def test_9(self):
        roman = 'IIII'
        self.assertIsNone(roman_numerals.convert_to_integer(roman))

    def test_10(self):
        roman = 'VIIIIX'
        self.assertIsNone(roman_numerals.convert_to_integer(roman))

    def test_11(self):
        roman = 'MMXXII'
        self.assertEqual(2022, roman_numerals.convert_to_integer(roman))

    def test_12(self):
        roman = 'MMMCMXCIX'
        self.assertEqual(3999, roman_numerals.convert_to_integer(roman))
