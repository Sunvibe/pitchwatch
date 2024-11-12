# pitchwatch
A Python-based Dockerized recorder for the world’s "laziest experiment": capturing the live stream of the Pitch Drop Experiment.

The Pitch Drop Experiment, which started in 1935, is one of the longest-running science experiments in history, documenting the incredibly slow flow of pitch, a tar-like substance. More details about the experiment can be found [here](https://en.wikipedia.org/wiki/Pitch_drop_experiment). A live video stream of the experiment is available at [thetenthwatch.com](http://thetenthwatch.com/).

### ToDo's
* [x] Create a github repo for this project
* [x] Involve ChatGPT writing this readme 
* [x] Copy the existing code stuff to this repo
* [x] Simple basic structure for this project (using chatgpt)
    * Goal: Find an easy procedure to keep this repo as an dockerized container using portainer 
    * Build takes about 5 min and the docker image is about 700mb big... seems to me a bit sus...
* [ ] "Dockerize" this app for a simple capture test on a remote server running portainer (confirm my personal capturing issues)
* [ ] Add local dev guide with python venv's
* [ ] Determine the ideal frequency and storage capacity for captured images.

### How to Capture the Stream
The stream’s website currently embeds the live stream (as of 2024-11-11) via the following link:
`https://livestream.com/accounts/4931571/events/5369913/player?width=1590&height=895&autoPlay=true&mute=true`

In the JavaScript block of this webpage, the m3u8 URL for the live stream can be found within `window.config`, specifically at `["event"]["stream_info"]["m3u8_url"]`.

Using Python’s `cv2.VideoCapture` along with this m3u8 URL, we can connect to the stream and capture individual frames as images. The stream updates at intervals between 1 to 6 seconds, with an average of approximately one new frame every 5 seconds.

#### Known Issues with Python Stream Capture
During testing on my PC, I encountered an issue where, after capturing frames for 1-2 seconds (around 40 frames), the process pauses for roughly 5 seconds, then resumes capturing frames for another 1-2 seconds, repeating this pattern.

Additionally, I noticed that the stream itself was stuttering and pausing in the browser on my PC, which may indicate that the issue is related to the system or the stream quality itself, rather than the capture process.

This inconsistency prevents capturing images at precise intervals (e.g., every 10th second). While this may be a drawback for anyone seeking absolute precision, it is not expected to impact the overall experiment significantly.

### Testing Results
* **Expected Capture Rate**: Every 30 seconds, resulting in ~2880 images per day (~576 MB of storage per day).
* **Compression Efficiency**:
    - 167 images (uncompressed): ~30 MB
    - Compressed as zip: ~29.5 MB  
    - → Image compression appears to provide minimal space savings.