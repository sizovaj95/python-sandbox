"""
Script to reverse each word in a string.
Assumptions:
- all lowercase
- words are groups of characters separated by single space
- words original order is kept
- don't reverse punctuation
- words with "-/'" etc are considered as one word
E.g. "In a hole in the ground there lived a hobbit." -> "ni a eloh ni eht dnuorg ereht devil a tibboh."
"""
import re
from typing import Optional


def reverse_words_in_a_string(text: Optional[str]) -> Optional[str]:
    if not text:
        return text
    words = text.split(' ')
    new_text = []
    for word in words:
        new_word = word.lower()[::-1]
        if re.search(r"\W", new_word[0]):
            new_word = new_word[1:] + new_word[0]

        new_text.append(new_word)
    new_text = ' '.join(new_text)
    return new_text


def main():
    text = 'In a hole in the ground there lived a hobbit.'
    new_text = reverse_words_in_a_string(text)


if __name__ == "__main__":
    main()
