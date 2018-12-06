import unittest


def max_number(n):
    sorted_number = sorted(list(str(n)), reverse=True)  # to string -> create a list -> sorting reverse
    return int(''.join(sorted_number))


class TestStringMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(max_number(12345), 54321)
        self.assertEqual(max_number(10457), 75410)
        self.assertEqual(max_number(100000), 100000)
        self.assertEqual(max_number(33556988), 98865533)


if __name__ == '__main__':
    unittest.main()
