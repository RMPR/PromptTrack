from PromptTrack import PromptTracker

tracker = PromptTracker()

tracker.detect_objects(video_file, prompt="i am interested in penguin",nms_threshold=0.8) 
