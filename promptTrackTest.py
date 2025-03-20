from PromptTrack import PromptTracker
import os 

tracker = PromptTracker()
video_file= "test/video_test/test.mp4"

for video_path in [video_file]:
    if video_path.split(".")[-1] in ["mp4"] :
        video_file= video_path
        print("we start tracking the video", video_file)
        tracker = PromptTracker()
        tracker.detect_objects(video_file, prompt="penguin",nms_threshold=0.8, detection_threshold=0.3 ,detector="OWL-VITV2")
        
        
        #video_file: is the path of the video 
        #prompt: comma separated names of the entities you would like to track example to track birds and pigs  prompt="pig,bird"
        #nms_threshold: used for applying nms on mdetr
        #detection_threshold: is the threshold on detection that will be reported 
        #detector: is the detector you would like to use we provide mdetr and owl-vitv2 that you could use as parameters 

        tracker.process_mot (video_file, fixed_parc=True,track_thresh=0.40, match_thresh=1, frame_rate=25,max_time_lost=float('inf'),nbr_frames_fixing=800)
        
        
        
        #Track_thresh: is the detection threshold that the tracker will use to perform its tracking
        #match_thresh: 1-threshold on the matching between tracks and new detections,  1 to match all detections to track, and 0 to match no detection with previous tracks
        #frame_rate: frame rate of the video
        #fixed_parc: set this variable to true if the number of animal in the parc is fixed and does not change all over the video 
        #video_file: is the path of the video 

        #Default values fixed_parc=True, nbr_items=15, track_thresh=0, match_thresh=1, frame_rate=6, track_buffer=10000, max_time_lost=20000)


        tracker.read_video_with_mot(video_file,fps=20)
