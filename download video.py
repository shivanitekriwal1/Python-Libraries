#file for downloading any video
import urllib

url = input("enter the url of the video here")
name = input("enter the name of the video")
print "downloading"
urllib.urlretrieve(url, "name.mp4")
print "downloaded"