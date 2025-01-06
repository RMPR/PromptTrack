import unittest
import math
from PromptTrack import PromptTracker


class PromptTrackerTestCase(unittest.TestCase):

    def setUp(self):
        self.tracker = PromptTracker()

    def test_fixed_entities(self):
        try:
            video_file = "/home/sophie/aggression_detection/package/test/video_test/test3.mp4"
            self.tracker.detect_objects(video_file, prompt="pigs")
            self.tracker.process_mot (video_file,)
            self.tracker.read_video_with_mot(video_file)
        except:
            self.fail("test_fixed_entities raised an error")


    '''def test_variable_entities(self):
        """Test natural number 5 multiplied by 2"""

        # 5 multiplied by 2 return 10
        result = self.multiplication.multiply(5)
        self.assertEqual(result, 10)

    def test_integer_number(self):
        """Test integer number -7 multiplied by 2"""

        # -7 multiplied by 2 return -14
        result = self.multiplication.multiply(-7)
        self.assertEqual(result, -14)

    def test_rational_number(self):
        """Test rational number 6/17 multiplied by 2"""

        # 6/17 multiplied by 2 return (6/17) * 2
        result = self.multiplication.multiply(6/17)
        self.assertEqual(result, (6/17) * 2)

    def test_real_number(self):
        """Test real number PI multiplied by 2"""

        # PI multiplied by 2 return 2PI
        result = self.multiplication.multiply(math.pi)
        self.assertEqual(result, math.pi * 2)'''


if __name__ == '__main__':
    unittest.main()