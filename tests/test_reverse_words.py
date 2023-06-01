from unittest import TestCase

import reverse_words as rw


class TestReverseWords(TestCase):
    def test1(self):
        text = 'In a hole in the ground there lived a hobbit.'
        expected = "ni a eloh ni eht dnuorg ereht devil a tibboh."
        result = rw.reverse_words_in_a_string(text)
        self.assertEqual(expected, result)

    def test2(self):
        text = "Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell,"
        expected = 'ton a ytsan, ytrid, tew eloh, dellif htiw eht sdne fo smrow dna na yzoo llems,'
        result = rw.reverse_words_in_a_string(text)
        self.assertEqual(expected, result)

    def test3(self):
        text = "Hobbit's name was Bilbo."
        expected = "s'tibboh eman saw oblib."
        result = rw.reverse_words_in_a_string(text)
        self.assertEqual(expected, result)

    def test4(self):
        text = ""
        expected = ""
        result = rw.reverse_words_in_a_string(text)
        self.assertEqual(expected, result)

    def test5(self):
        text = None
        result = rw.reverse_words_in_a_string(text)
        self.assertIsNone(result)

    def test6(self):
        text = "This hobbit was a very well-to-do hobbit, and his name was Baggins. The Bagginses had lived in " \
               "the neighbourhood of The Hill for time out of mind."
        expected = "siht tibboh saw a yrev od-ot-llew tibboh, dna sih eman saw sniggab. eht sesniggab dah devil ni " \
                   "eht doohruobhgien fo eht llih rof emit tuo fo dnim."
        result = rw.reverse_words_in_a_string(text)
        self.assertEqual(expected, result)

    def test7(self):
        text = "and his name was Baggins.The Bagginses had lived in"
        expected = "dna sih eman saw eht.sniggab sesniggab dah devil ni"

        result = rw.reverse_words_in_a_string(text)
        self.assertEqual(expected, result)
