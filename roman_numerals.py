"""Take a Roman numeral as its input and returns its value as an integer.
Modern Roman numerals are written by expressing each decimal digit of the number to be
encoded separately, starting with the leftmost decimal digit and skipping any 0s (zeroes).
1990 is rendered as MCMXC (1000 = M, 900 = CM, 90 = XC) and
2008 is rendered as MMVIII (2000 = MM, 8 = VIII).
The Roman numeral for 1666, MDCLXVI, uses each letter in descending order."""
import typing

roman_to_int_dict = {
    'm': 1000,
    'd': 500,
    'c': 100,
    'l': 50,
    'x': 10,
    'v': 5,
    'i': 1,
}


def check_that_valid_number(roman_num: str) -> bool:
    prev_char = None
    conseq_char = 0
    for char in roman_num:
        if char.lower() not in roman_to_int_dict:
            return False
        if char == prev_char:
            conseq_char += 1
        else:
            conseq_char = 0
        if conseq_char >= 3:
            return False
        prev_char = char
    return True


def convert_to_integer(roman_num: str) -> typing.Optional[int]:
    roman_num = roman_num.lower()
    as_int = 0

    if not check_that_valid_number(roman_num):
        print("Invalid roman number!")
        return None
    for i, char in enumerate(roman_num):
        current_int = roman_to_int_dict[char]
        try:
            next_char = roman_num[i+1]
            next_int = roman_to_int_dict[next_char]
        except IndexError:
            as_int += current_int
            break

        if current_int < next_int:
            # IX
            as_int -= current_int
        else:
            # XI, III
            as_int += current_int
    return as_int


def main():
    roman_num = 'IV'
    num = convert_to_integer(roman_num)
    num


if __name__ == "__main__":
    main()
