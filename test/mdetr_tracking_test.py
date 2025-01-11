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



if __name__ == '__main__':
    unittest.main()