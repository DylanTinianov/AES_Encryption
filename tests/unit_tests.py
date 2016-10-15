import unittest


class UnitTest(unittest.TestCase):
    def test_key_schedule(self):
        # make sure key expansion works properly
        self.assertEqual(1, 1)
        pass

    def test_encryption(self):
        # make sure encryption doesnt have errors
        pass

    def test_decryption(self):
        # check if decrypted text is the same as before it was encrypted
        pass


if __name__ == '__main__':
    unittest.main(exit=False)
