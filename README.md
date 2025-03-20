# **PromptTrack**
## 📄 **Overview**
**PromptTracker** is a powerful object tracking tool that enables the detection and tracking of objects in videos using **text-based  prompts**. It supports advanced object detection models such as **MDETR** and **OWL-VITV2**, providing robust tracking with options to handle **fixed populations** in enclosed environments.

---

## 📥 **Installation**

To install PromptTracker, use the following command:

```python
pip install prompt-tracker
pip install --no-deps bytetracker





The package has been implemented for python from 3.9 to earlier (last version currently 3.12)
You can check our [github repo](https://github.com/ngobibibnbe/PromptTrack)


## Usage

```python
from PromptTrack import PromptTracker

tracker = PromptTracker()

video_file = "[path_to_your_video](https://www.pexels.com/video/penguins-hopping-down-the-stairs-9116156/)"  #[video example](https://www.pexels.com/video/penguins-hopping-down-the-stairs-9116156/)

tracker.detect_objects(video_file, prompt="penguin;pig",nms_threshold=0.8) 
tracker.process_mot (video_file, fixed_parc=False,track_thresh=0.3, match_thresh=0.8, frame_rate=25,max_time_lost=300)
tracker.read_video_with_mot(video_file)


## Parameters of tracker.detect_objects
#video_file: is the path of the video 

#prompt: comma separated names of the entities you would like to track example to track birds and pigs  prompt="pig,bird"

#nms_threshold: used for applying nms on mdetr

#detection_threshold: is the threshold on detection that will be reported 

#detector: is the detector you would like to use we provide mdetr and owl-vitv2 that you could use as parameters 




## Parameters of tracker.process_mot 

#Track_thresh: is the detection threshold that the tracker will use to perform its tracking

#match_thresh: 1-threshold on the matching between tracks and new detections,  1 to match all detections to track, and 0 to match no detection with previous tracks

#frame_rate: frame rate of the video

#fixed_parc: set this variable to true if the number of animal in the parc is fixed and does not change all over the video 

#video_file: is the path of the video 

#Default values fixed_parc=True, nbr_items=15, track_thresh=0, match_thresh=1, frame_rate=25, track_buffer=10000, max_time_lost=100



##  Result
It will provide you in the video folder, a video with the track and a json file with track in the format {frame_id:{pig_id:{x:"", y:"",width:"",height:""}}}

