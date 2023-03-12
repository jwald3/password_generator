import unittest
from password_generator import generate_password_from_chars, generate_password_from_word_list, generate_password, format_time_to_crack, check_strength

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_from_chars(self):
        password, complexity = generate_password_from_chars(10, 'alphanumeric,special')
        self.assertEqual(len(password), 10, "Expect password length to match specified length")
        self.assertGreater(complexity, 0)

    def test_generate_password_from_word_list(self):
        password, complexity = generate_password_from_word_list(12)
        self.assertGreaterEqual(len(password), 12, "Expect password length to meet or exceed minimum length")
        self.assertGreater(complexity, 0)

    def test_generate_password(self):
        password, complexity = generate_password(length=8, allowed_chars='lowercase')
        self.assertEqual(len(password), 8, "Expect password length to match specified length")
        self.assertGreater(complexity, 0)

    def test_format_time_to_crack(self):
        self.assertEqual(format_time_to_crack(1), '1 year', 'Expect formatted time to match expected format')
        self.assertEqual(format_time_to_crack(1000), '1 thousand years', 'Expect formatted time to match expected format')
        self.assertEqual(format_time_to_crack(1000000), '1 million years', 'Expect formatted time to match expected format')
        self.assertEqual(format_time_to_crack(1000000000), '1 billion years', 'Expect formatted time to match expected format')
        self.assertEqual(format_time_to_crack(1000000000000), '1 trillion years', 'Expect formatted time to match expected format')
        self.assertEqual(format_time_to_crack(10000000000000000000000000000000000000), '999 trillion years or more', 'Expect formatted time to match expected format')

    def test_check_strength(self):
        score, feedback = check_strength('password', 52)
        self.assertEqual(score, 0, "Expect score to be 0 for weak password")
        self.assertIn('Password is too short', feedback, 'Expect feedback to include message for weak password')

        score, feedback = check_strength('Password123!', 94)
        self.assertEqual(score, 2, "Expect score to be 2 for strong password")
        self.assertIn('Password length is good', feedback, 'Expect feedback to include message for strong password')

if __name__ == '__main__':
    unittest.main()