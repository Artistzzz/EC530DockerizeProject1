from MatricesMultiplication import multiply_matrices
import unittest
import numpy as np

class TestMatrixMultiplication(unittest.TestCase):
    def test_non_empty_matrices(self):
        with self.assertRaises(ValueError):
            multiply_matrices([], [[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            multiply_matrices([[1, 2], [3, 4]], [])

    def test_input_format(self):
        with self.assertRaises(ValueError):
            multiply_matrices([1, 2, 3], [[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            multiply_matrices([[1, 2], [3, 4]], "Not a matrix")

    def test_elements_are_integers(self):
        with self.assertRaises(ValueError):
            multiply_matrices([[1, 2.5], [3, 4]], [[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            multiply_matrices([[1, 2], [3, 4]], [[1, 'a'], [3, 4]])

    def test_multiplicability(self):
        with self.assertRaises(ValueError):
            multiply_matrices([[1, 2, 3]], [[1, 2], [3, 4]])

    def test_correct_multiplication(self):
        result = multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        expected = np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()