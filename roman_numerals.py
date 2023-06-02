"""Take a Roman numeral as its input and returns its value as an integer.
Modern Roman numerals are written by expressing each decimal digit of the number to be
encoded separately, starting with the leftmost decimal digit and skipping any 0s (zeroes).
1990 is rendered as MCMXC (1000 = M, 900 = CM, 90 = XC) and
2008 is rendered as MMVIII (2000 = MM, 8 = VIII).
The Roman numeral for 1666, MDCLXVI, uses each letter in descending order.

Assumptions:
- Roman numerals only up to 3999, so no overlines

Rules:
- no numeral can come together more than 3 times: no IIII
- repeated numerals add up: XXX=30
- V, L, and D do not repeat
- only I, X and C can be subtracted: I from V and X; X from L and C; C from D and M
- numeral placed before a numeral of greater value is subtracted from it
- numeral placed after a numeral of greater value is summed with it
"""
from typing import Optional
import re


ROMAN_TO_INT_DICT = {
    'm': 1000,
    'd': 500,
    'c': 100,
    'l': 50,
    'x': 10,
    'v': 5,
    'i': 1,
}


class RomanNumeral:
    """Helper class to hold info about character"""
    def __init__(self, char: str, i: int):
        self.roman = char.lower()
        self.arabic = self.map_roman_to_arabic(self.roman)
        self.i = i

    @staticmethod
    def map_roman_to_arabic(char) -> Optional[int]:
        try:
            return ROMAN_TO_INT_DICT[char]
        except KeyError:
            return None

    @property
    def is_valid(self) -> bool:
        if self.roman not in ROMAN_TO_INT_DICT:
            return False
        return True


class RomanNumeralsConverter:
    NON_REPEATING_LETTERS = ['v', 'l', 'd']
    REPEATING_LETTERS = ['i', 'x', 'c', 'm']
    SUBTRACTIVE_LETTERS = ['i', 'x', 'c']

    def __init__(self, roman_numeral: str):
        self.roman_numeral = roman_numeral

    @property
    def roman_numeral(self):
        return self._roman

    @roman_numeral.setter
    def roman_numeral(self, value: Optional[str]):
        if not value:
            raise ValueError("Roman numeral cannot be None or empty string!")
        self._roman = value.lower()

    @property
    def as_char_list(self) -> list[RomanNumeral]:
        return [RomanNumeral(c, i) for i, c in enumerate(self.roman_numeral)]

    def is_start_of_group(self, char: RomanNumeral) -> tuple:
        """Check if character is a start of group of subsequent characters (e.g. III)"""
        if match := re.search(r"%s{2,3}" % char.roman, self.roman_numeral):
            if match.start() == char.i:
                return True, len(match[0])
        return False, None

    def check_if_valid(self) -> bool:
        """Check for obvious mistakes"""
        if not all([char.is_valid for char in self.as_char_list]):
            # GI
            return False
        for letter in self.NON_REPEATING_LETTERS:
            if self.roman_numeral.count(letter) > 1:
                # VV
                return False
        for letter in self.REPEATING_LETTERS:
            if re.search(r"%s{4,}" % letter, self.roman_numeral):
                # IIII
                return False
        return True

    def next_char(self, i: int) -> Optional[RomanNumeral]:
        try:
            return self.as_char_list[i+1]
        except IndexError:
            return None

    def is_legal_subtraction(self, left_char: RomanNumeral, right_char: RomanNumeral) -> bool:
        """Check that correct combination of minuend and subtrahend (eg IX and not IC)"""
        if left_char.roman in self.SUBTRACTIVE_LETTERS and right_char.arabic <= left_char.arabic * 10:
            return True
        else:
            return False

    def calculate_by_roman_num_rules(self, left_char: RomanNumeral, right_char: RomanNumeral, as_int: int) -> \
            Optional[int]:
        """Depending on whether value on the right is smaller or larger"""
        if left_char.arabic < right_char.arabic:
            if self.is_legal_subtraction(left_char, right_char):
                as_int -= left_char.arabic
            else:
                as_int = None
        else:
            as_int += left_char.arabic
        return as_int

    def convert_to_int(self) -> Optional[int]:
        if not self.check_if_valid():
            return None
        as_int = 0
        for char in self.as_char_list:
            next_char = self.next_char(char.i)
            if next_char is None:
                as_int += char.arabic
                break
            start_of_group, group_len = self.is_start_of_group(char)
            if start_of_group:
                group_value = char.arabic * group_len
                next_group_start = self.next_char(char.i + group_len - 1)
                if next_group_start and group_value < next_group_start.arabic:
                    # IIIX
                    as_int = None
                    break
            as_int = self.calculate_by_roman_num_rules(char, next_char, as_int)
            if not as_int:
                break
        return as_int


def convert_roman_numeral_to_integer(roman_numeral: str) -> Optional[str]:
    converter = RomanNumeralsConverter(roman_numeral)
    integer = converter.convert_to_int()
    return integer
