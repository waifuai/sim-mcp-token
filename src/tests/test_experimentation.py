import unittest
import experimentation

class TestExperimentation(unittest.TestCase):

    def test_experimentation_runs(self):
        try:
            experimentation.param_ranges
        except Exception as e:
            self.fail(f"experimentation.py raised {type(e).__name__}: {e}")

if __name__ == '__main__':
    unittest.main()