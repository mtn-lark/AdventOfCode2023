import unittest
from camel_cards import (
    calculate_hand_type,
    is_hand_better,
)


class TestCamelCards(unittest.TestCase):
    def test_calculate_hand_type(self):
        # High card
        hand = "AQKJ9"
        expected_hand_type = 0
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "KQJ98"
        expected_hand_type = 0
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "5432A"
        expected_hand_type = 0
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        # One pair
        hand = "AAKJ9"
        expected_hand_type = 1
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "KQQJ9"
        expected_hand_type = 1
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "54322"
        expected_hand_type = 1
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        # Two pair
        hand = "AAKK9"
        expected_hand_type = 2
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "KQQJJ"
        expected_hand_type = 2
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "44232"
        expected_hand_type = 2
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        # Three of a kind
        hand = "AAAQ9"
        expected_hand_type = 3
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "KQQQJ"
        expected_hand_type = 3
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "54KKK"
        expected_hand_type = 3
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        # Full house
        hand = "AAAKK"
        expected_hand_type = 4
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "KK999"
        expected_hand_type = 4
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "4K4KK"
        expected_hand_type = 4
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        # Four of a kind
        hand = "AAAA9"
        expected_hand_type = 5
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "AKKKK"
        expected_hand_type = 5
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "94999"
        expected_hand_type = 5
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        # Five of a kind
        hand = "AAAAA"
        expected_hand_type = 6
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "JJJJJ"
        expected_hand_type = 6
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

        hand = "99999"
        expected_hand_type = 6
        actual_hand_type = calculate_hand_type(hand)
        self.assertEqual(actual_hand_type, expected_hand_type)

    def test_is_hand_better(self):
        self.assertTrue(is_hand_better("AAAAA", "AAAA9"))
        self.assertTrue(is_hand_better("AAAA9", "AAAA8"))
        self.assertTrue(is_hand_better("AAA9A", "A9AAA"))
        self.assertTrue(is_hand_better("A6123", "A5432"))
        self.assertTrue(is_hand_better("AAA33", "A3A3A"))
        self.assertTrue(is_hand_better("AAA33", "33AAA"))

        self.assertFalse(is_hand_better("AAAA9", "AAAAA"))
        self.assertFalse(is_hand_better("AAAA8", "AAAA9"))
        self.assertFalse(is_hand_better("A9AAA", "AAA9A"))
        self.assertFalse(is_hand_better("A5432", "A6123"))
        self.assertFalse(is_hand_better("A3A3A", "AAA33"))
        self.assertFalse(is_hand_better("33AAA", "AAA33"))


if __name__ == "__main__":
    unittest.main()
