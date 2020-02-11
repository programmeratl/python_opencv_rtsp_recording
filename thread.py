#!/usr/bin/python
import cv2
import numpy as np
import time
import xml.sax
import os
from parsing import XMLParser
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name,url, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.url=url
      self.counter = counter
      self.frame_width=640
      self.frame_height=480
      self.counter=0
   
   def get_output(out=None):
    #Specify the path and name of the video file as well as the encoding, fps and resolution
    if out:
        out.release()
    print("frame width is : ", frame_width)	
    return cv2.VideoWriter('recordings/'+time.strftime('%d %m %Y - %H %M %S' )+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (self.frame_width,self.frame_height))

   
   def run(self):
      print "Starting " + self.name
      threadLock.acquire()	
      start_recording(self)
      threadLock.release()
      #print_time(self.name, 5, self.counter)
      #print "Exiting " + self.name

   
def start_recording(self):
	    if not os.path.exists(self.name):
		os.mkdir(self.name,0o777)
	    # Create a VideoCapture object
	    cap = cv2.VideoCapture(self.url)
	    next_time = time.time() + 10
	    # Check if camera opened successfully
	    if (cap.isOpened() == False): 
		print("Unable to read camera feed")
	 
	    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
	    # We convert the resolutions from float to integer.
	    self.frame_width = int(cap.get(3))
	    self.frame_height = int(cap.get(4))
	    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
	    #out = cv2.VideoWriter('recordings/latest.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (self.frame_width,self.frame_height))
	    out=self.get_output()
	    start_time = time.time()
	    while(True):
		  if time.time() > next_time:
			next_time += 10
			out = self.get_output(out)
		  ret, frame = cap.read()
		 
		  if ret == True: 
		     
		    # Write the frame into the file 'output.avi'
		    out.write(frame)
		    #start_time = time.time()
		    #print(start_time)
			
		 
		    # Display the resulting frame    
		    cv2.imshow('frame',frame)
		 
		    # Press Q on keyboard to stop recording
		    if cv2.waitKey(1) & 0xFF == ord('q'):
		      break
		 
		  # Break the loop
		  else:
		    break 
	 
	      # When everything done, release the video capture and video write objects
	    cap.release()
	    out.release()
	 
	    # Closes all the frames
	    cv2.destroyAllWindows()    

"""
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
"""

threadLock = threading.Lock()
threads = []
#XML Operation--------------------
param={}
counter=0
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
dataV=XMLParser()
parser.setContentHandler( dataV )

parser.parse("data.xml")
param=dataV.get_detail()
for key in param:
	print(key,'->',param[key])
	try:
	  #thread1 = myThread(1, "Thread-1", 1)
	  #thread.start_new_thread( start_recording, (param[key][0], param[key][1], ) )
	  #thread[counter] = threading.Thread(start_recording(param[key][0], param[key][1], ))
	  thread = myThread(counter,param[key][0], param[key][1], 1)
	except:
	  print "Error: unable to start thread"
	thread.start()
	threads.append(thread)
	counter+=1
	#start_recording(param[key][0],param[key][1])
	#for k in param[key]:
		#print(k)
		#start_recording()

for t in threads:
    t.join()
		
#---------------------------------