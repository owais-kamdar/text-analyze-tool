import unittest
from script import analyze_text

class TestScript(unittest.TestCase):

    def setUp(self):
        # Create a sample text file for testing
        self.test_file = 'test_text.txt'
        with open(self.test_file, 'w') as f:
            f.write("This is a test. This test is only a test.")

    def test_analyze_text(self):
        # Analyze the text and get statistics
        stats = analyze_text(self.test_file, top_n=2)

        # Verify total and unique word counts
        # Note: Expecting 10 total words here because 'test' appears 3 times
        self.assertEqual(stats['total_words'], 10)
        self.assertEqual(stats['unique_words'], 5)

        # Verify most common words
        self.assertEqual(stats['common_words'][0], ('test', 3))
        self.assertEqual(stats['common_words'][1], ('this', 2))

    def tearDown(self):
        # Clean up test file
        import os
        os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
