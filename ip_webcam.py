import cv2
import urllib2
import numpy as np
import sys

host = "192.168.11.7:8080"
if len(sys.argv)>1:
    host = sys.argv[1]

hoststr = 'http://' + host + '/video'
print 'Streaming ' + hoststr

print 'Print Esc to quit'
stream=urllib2.urlopen(hoststr)

bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        #flags = 1 for color image
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),flags=1)
        print i.shape
        cv2.imshow(hoststr,i)
        if cv2.waitKey(1)==27:
            exit(0)