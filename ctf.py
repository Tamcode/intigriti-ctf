import numpy as np
import cv2
import os

dir_path="data" #fill here
files=os.listdir(dir_path)

# for file in files:
# 	# do what you want to do with image - its in array form
# 	# use concatenate to join

files.sort(key=lambda x:int(x.split("_")[1].split(".")[0]))
print(files)

final_img=np.ones((0,231,3))
for i in range(21):
	temp_img=np.ones((11,0,3))
	for j in range(21):
		index=i*21+j
		file=files[index]
		filepath=os.path.join(dir_path,file)
		img = cv2.imread(filepath,cv2.IMREAD_COLOR)
		temp_img=np.concatenate((temp_img,img),axis=1)
	# print(temp_img.shape)
	final_img=np.concatenate((final_img,temp_img),axis=0)
print(final_img.shape)
cv2.imwrite("qr.jpg", final_img)
