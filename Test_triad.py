import unittest
import main

# Test cases not responding as expected. Need work before moving forward on other functions
# Currently test_load_it should fail because no exception is raised

class TestTriad(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """Use global files available in current dir for tests and other globals too."""
        print("SetUp")
        cls.mp3_file = "submerse - Stay Home - 07 blueprints.mp3"
        cls.simple_string = "submerse"
        cls.unsupported_file_name = "README.md"
        cls.wrong_type = 0
    
    @classmethod
    def tearDown(cls):
        print("TearDown")

    def test_load_it(self):
        "Tests load_it module for Exceptions"
        # This Should Fail becaus ethis file type is correct.
        with self.assertRaises(Exception) as exp:
            main.Triad.load_it(self, self.mp3_file)
            expected_msg = 'File Type not supported'
            self.assertEqual(exp.exception, expected_msg)
    
    def test_change_label(self):
        # This should Fail because no exception is thrown.
        with self.assertRaises(Exception) as ctx:
            main.Triad.change_label(self, self.simple_string)
            expected_msg = 'To change label, must use string data type.'
            self.assertEqual(ctx.exception, expected_msg)

        

if __name__ == '__main__':
    unittest.main()

# T = TestTriad()
