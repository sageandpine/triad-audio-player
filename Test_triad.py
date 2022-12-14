import unittest
import main

class TestTriad(unittest.TestCase):
    @classmethod
    def setUp(cls):
        """Use global files available in current dir for tests and other globals too."""
        cls.simple_string = "submerse"
        cls.unsupported_file_name = "README.md"
        cls.wrong_type = 0

    @classmethod
    def tearDown(cls):
        pass

    def test_load_it(self):
        "Tests load_it module for Exceptions."
        with self.assertRaises(ValueError) as exp:
            main.Triad.load_it(self, self.wrong_type)
            expected_msg = "File loaded must be string"
            self.assertEqual(exp.exception, expected_msg)

        with self.assertRaises(Exception) as exp:
            main.Triad.load_it(self, self.mp3_file)
            expected_msg = "File Type not supported"
            self.assertEqual(exp.exception, expected_msg)

    def test_change_song_label(self):
        """Tests change_song_label module for Exceptions."""
        with self.assertRaises(ValueError) as ctx:
            main.Triad.change_song_label(self, self.wrong_type)
            expected_msg = "To change label, must use string data type."
            self.assertEqual(ctx.exception, expected_msg)

    def test_update_now_playing(self):
        """"Tests update_now_playing module for exceptions."""
        with self.assertRaises(ValueError) as exp:
            main.Triad.update_now_playing(self, self.wrong_type)
            expected_msg = "Songs loaded must be list type."
            self.assertEqual(exp.exception, expected_msg)
    
    def test_update_pl_editor(self):
        "Tests update_pl_editor module for Exceptions."
        with self.assertRaises(ValueError) as exp:
            main.Triad.update_pl_editor(self, self.wrong_type)
            expected_msg = "Songs loaded must be list type."
            self.assertEqual(exp.exception, expected_msg)
    
    def test_get_meta(self):
        "Tests update_pl_editor module for Exceptions."
        with self.assertRaises(ValueError) as exp:
            main.Triad.get_meta(self, self.wrong_type, self.wrong_type)
            expected_msg = "Directory and File to be loaded must be string type."
            self.assertEqual(exp.exception, expected_msg)
        

if __name__ == "__main__":
    unittest.main()

# T = TestTriad()
