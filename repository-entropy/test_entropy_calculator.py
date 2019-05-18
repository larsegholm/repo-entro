import unittest
from entropy_calculator import EntropyCalculator


class EntropyCalculatorTest(unittest.TestCase):

    def test_empty_string(self):
        ent_calc = EntropyCalculator()
        text = ""

        entropy = ent_calc.calculate_entropy(text)
        self.assertEqual(entropy, 0)

    def test_constant_string(self):
        ent_calc = EntropyCalculator()
        text = "aaa"

        entropy = ent_calc.calculate_entropy(text)
        self.assertEqual(entropy, 0)

    def test_random_string(self):
        ent_calc = EntropyCalculator()
        text = "wfkjqpwqfjpqwfjqw"

        entropy = ent_calc.calculate_entropy(text)
        self.assertGreater(entropy, 0)


if __name__ == '__main__':
    unittest.main()
