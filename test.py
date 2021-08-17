import unittest
import greet

class TestGreetWorld(unittest.TestCase):
    def test_greet_world(self):
        import greet
        self.assertEqual(greet.greet_world(), "Hi World!")

if __name__=="_main__":
    unittest.main()