import unittest

from randomkey import generate_key
# This test generates 10 keys and checks if any of them are the same. 
# If any duplicates are found, the test fails, indicating that the keys are not random. Note that this test does not guarantee 
# that the keys are perfectly random, but it provides a reasonable level of confidence in the randomness of the keys.

class TestRandomKey(unittest.TestCase):

    def test_randomness(self):
        keys = set()
        for _ in range(10):
            key = generate_key()
            print (key)
            # the test is asserting that the generated key is not already in the set of keys.
            self.assertNotIn(key, keys, "Duplicate key found, randomness test failed.")
            keys.add(key)

if __name__ == '__main__':
    unittest.main()