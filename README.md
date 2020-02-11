# python_opencv_rtsp_recording
Recording of rtsp:// camera stream with python opencv.

Subject: Recording of rtsp:// camera stream with python opencv. Multiple stream recording possible. We are using data.xml that keeps urls, name of stream ( user defined)
and duration of recording.

(1)data.xml stores rtsp:// or http:// stream link and fps detail. We are using &amp instead of & in rtsp:// url format.

(2)parsing.py parse data.xml .
(3)thread.py receive all parameters from parsing.py and create threads for recording. In the function start_recording we are creating folder name as of stream name 
and recording video file of duration metioned in <schedule></schdule> in data.xml.

Note: worked with Python 2.7.3
