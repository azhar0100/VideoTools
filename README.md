# VideoTools
Scripts that are helpful for me to have, in order to work on video related AI tasks

## getframes_script.py

This file extracts frames for each file given in command line arguments in a directory with the same name as the video file. It also extracts an mp3 with the audio from the file. This works best if the files have single video and audio streams, it'll need to be modified for files with multiple streams.
This requires the sh module to work at all, and that can easily be installed via pip. 
The script is in python3.
