'''
MIT License

Copyright (c) 2022 SourceCode347

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

https://github.com/sourcecode347/NightVision/
https://sourcecode347.com
'''
from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import numpy as np
def create_blank(width, height, rgb_color=(0, 0, 0)):
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(reversed(rgb_color))
    image[:] = color
    return image
vs = VideoStream(src=-1).start()
time.sleep(2.0) 
firstFrame = None
sicount=0
while True:
  frame = vs.read()
  if frame is None:
    break
  frame = imutils.resize(frame, width=640 , height=480)
  new_image = np.zeros(frame.shape, frame.dtype)
  new_image = np.clip(frame + 25 , 0, 255)
  greenimg = create_blank(640,480,(32,194,14))
  new_frame = cv2.addWeighted(frame , 0.9 , greenimg , 0.1 , 0)
  new_image = cv2.addWeighted(new_image  , 1 , new_frame , 1 , 0)
  text = "SourceCode347"
  cv2.putText(frame, "Author : {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255 , 0 ), 2)
  cv2.putText(frame, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255 , 0), 1)
  cv2.putText(new_image, "Website : {}.com".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255 , 0 ), 2)
  cv2.putText(new_image, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255 , 0), 1)
  cv2.imshow("Normal Vision", frame)
  cv2.imshow("Night Vision", new_image)
  key = cv2.waitKey(1) & 0xFF
  if key == ord("q"):
    break
vs.stop()
cv2.destroyAllWindows()
