# TestcaughtSpeeding.py

# Import Statements
import unittest
import caughtSpeeding

class KnownValues(unittest.TestCase):

    def test_caughtSpeedingForSameSpeed_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(45, 45, False)
        # Check for expected output
        self.assertEqual(0, result)

    def test_caughtSpeedingFor6over_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(51, 45, False)
        # Check for expected output
        self.assertEqual(500, result)

    def test_caughtSpeedingFor10over_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(55, 45, False)
        # Check for expected output
        self.assertEqual(500, result)

    def test_caughtSpeedingFor21over_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(61, 40, False)
        # Check for expected output
        self.assertEqual(1000, result)

    def test_caughtSpeedingFor45over_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(100, 55, False)
        # Check for expected output
        self.assertEqual(1500, result)

    def test_caughtSpeedingFor26over_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(81, 55, False)
        # Check for expected output
        self.assertEqual(1500, result)

    def test_caughtSpeedingForOver100_NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(105, 55, False)
        # Check for expected output
        self.assertEqual(2000, result)

    def test_caughtSpeedingFor10over_Birthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(65, 55, True)
        # Check for expected output
        self.assertEqual(0, result)

    def test_caughtSpeedingFor20over_Birthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(60, 40, True)
        # Check for expected output
        self.assertEqual(500, result)

    def test_caughtSpeedingFor25over_Birthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(65, 40, True)
        # Check for expected output
        self.assertEqual(1000, result)

    def test_caughtSpeedingFor103_Birthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(103, 55, True)
        # Check for expected output
        self.assertEqual(1500, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
