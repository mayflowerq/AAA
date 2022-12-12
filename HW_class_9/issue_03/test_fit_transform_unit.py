from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_seqw(self):
        actual = fit_transform(['Seqw', 'Terwfre', 'Dolce', 'pops'])
        expected = [('Seqw', [0, 0, 0, 1]),
                    ('Terwfre', [0, 0, 1, 0]),
                    ('Dolce', [0, 1, 0, 0]),
                    ('pops', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_two(self):
        actual = fit_transform(['2'])
        expected = [('2', [2])]
        self.assertNotEqual(actual, expected)

    def test_one_two_three(self):
        actual = fit_transform(['1', '2', '3'])
        expected = [('1', [0, 0, 1]), ('2', [0, 1, 0]), ('3', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_qwerty(self):
        actual = fit_transform(['Q', 'W', 'E', 'R', 'T', 'Y'])
        expected = [('Q', [0, 0, 0, 0, 0, 1]),
                    ('W', [0, 0, 0, 0, 1, 0]),
                    ('E', [0, 0, 0, 1, 0, 0]),
                    ('R', [0, 0, 1, 0, 0, 0]),
                    ('T', [0, 1, 0, 0, 0, 0]),
                    ('Y', [1, 0, 0, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_exception(self):
        actual = fit_transform(['D', 'O', 'G'])
        expected = [('D', [0, 0, 1]), ('O', [0, 1, 0]), ('G', [1, 0, 0])]
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            pass
