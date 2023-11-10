import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if generated operators are valid
        valid_operator = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, valid_operator)

    def test_calculation(self):
        test_cases = [(5, 2, '+', '5 + 2', 7),
                      (10, 15, '-', '10 - 15', -5),
                      (6, 5, '*', '6 * 5', 30),
                      (0, 9, '+', '0 + 9', 9)]

        for number_1, number_2, operator, expected_problem, expected_answer in test_cases:
            problem, result = calculation(number_1, number_2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(result, expected_answer)


if __name__ == "__main__":
    unittest.main()
