import os, random, time


VIDEO_PATH="/home/pi/Videos/"
PROCESS="omxplayer "


LIST_SIZE = 50
counter_list = 0

played_list = [None]*LIST_SIZE

while 1:

	video_file = random.choice(os.listdir(VIDEO_PATH))

	if video_file[-3:] == "mov" and video_file not in played_list:
		os.system(PROCESS + VIDEO_PATH + video_file)
		played_list[counter_list] = video_file
		counter_list +=1

		
	if counter_list == LIST_SIZE:
		played_list = [None]*LIST_SIZE
		counter_list = 0


