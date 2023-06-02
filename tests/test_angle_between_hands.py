from unittest import TestCase

from angle_between_hands import find_angle_between_hands


class TestAngleBetweenHands(TestCase):
    def test_1(self):
        time = (12, 30)
        angle = find_angle_between_hands(time, realistic_clock=False)
        self.assertEqual((180, 0), angle)

    def test_2(self):
        time = (12, 30)
        angle = find_angle_between_hands(time)
        self.assertEqual((165, 0), angle)

    def test_3(self):
        time = (3, 15)
        angle = find_angle_between_hands(time, False)
        self.assertEqual((0, 0), angle)

    def test_4(self):
        time = (3, 15)
        angle = find_angle_between_hands(time, True)
        self.assertEqual((7, 30), angle)

    def test_5(self):
        time = (12, 00)
        angle = find_angle_between_hands(time, True)
        self.assertEqual((00, 00), angle)

    def test_6(self):
        time = (12, 00)
        angle = find_angle_between_hands(time, False)
        self.assertEqual((00, 00), angle)

    def test_7_invalid(self):
        time = (13, 00)
        angle = find_angle_between_hands(time, False)
        self.assertEqual((None, None), angle)

    def test_8_invalid(self):
        time = (6, 65)
        angle = find_angle_between_hands(time, False)
        self.assertEqual((None, None), angle)
