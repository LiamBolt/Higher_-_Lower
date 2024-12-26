# test.py
import unittest
from game import compare_user_guess

data_example = [
    {
        'name': 'Apass',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Uganda'
    },
    {
        'name': 'Samanya Uganda',
        'follower_count': 45,
        'description': 'Online news platform', 'country': 'Uganda'},
]


class TestHigherLowerGame(unittest.TestCase):
    def test_compare_user_guess_correct_a(self):
        score = 0
        result = compare_user_guess(
            'a', score,
            ['Apass', 50, 'Musician', 'Uganda'],
            ['Samanya Uganda', 45, 'Online news platform', 'Uganda']
        )
        # User guessed 'a', and A has more followers (50 > 45)
        self.assertEqual(result, score + 1)

    def test_compare_user_guess_correct_b(self):
        score = 0
        result = compare_user_guess(
            'b', score,
            ['Apass', 50, 'Musician', 'Uganda'],
            ['Uganda Wildlife Authority', 350,
             'Government agency for wildlife conservation', 'Uganda']
        )
        # User guessed 'b', and B has more followers (350 > 50)
        self.assertEqual(result, score + 1)

    def test_compare_user_guess_incorrect(self):
        score = 0
        result = compare_user_guess(
            'a', score,
            ['Samanya Uganda', 45, 'Online news platform', 'Uganda'],
            ['Uganda Wildlife Authority', 350,
             'Government agency for wildlife conservation', 'Uganda']
        )
        # User guessed 'a', but B has more followers (350 > 45)
        self.assertEqual(result, score)


if __name__ == "__main__":
    unittest.main()
