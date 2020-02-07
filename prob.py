import cv2
import numpy as np
from sklearn.cluster import KMeans
import sys


imgPath = sys.argv[1]
image = cv2.imread(imgPath)


target_bgr = [39, 39, 255]
minBGR = np.array(target_bgr)
maxBGR = np.array(target_bgr)


def find_barycenter(image):
	# Creates a mask that sets luminosity to 255 if target color, shape=(2017, 3400)
	mask = cv2.inRange(image, minBGR, maxBGR)
	# mask.item((y, x)) returns 255 or 0

	points = []
	for i in range(2017):
		for j in range(3400):
			if mask.item((i, j)) == 255:
				points.append((i, j))
	points = np.array(points)
	
	kmeans = KMeans(n_clusters=1).fit(points)
	barycenter = kmeans.cluster_centers_
	return((barycenter[0][1], barycenter[0][0]))


print(find_barycenter(image))
