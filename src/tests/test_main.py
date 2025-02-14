import unittest
import main

class TestMain(unittest.TestCase):

    def test_main_runs(self):
        try:
            main.main()
        except Exception as e:
            self.fail(f"main.py raised {type(e).__name__}: {e}")

if __name__ == '__main__':
    unittest.main()