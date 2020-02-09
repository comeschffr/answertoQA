from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
import numpy as np
import cv2
import sys


target_bgr = [39, 39, 255]
minBGR = np.array(target_bgr)
maxBGR = np.array(target_bgr)


def find_centers(image):
	# Creates a mask that sets luminosity to 255 if target color, shape=(2017, 3400)
	mask = cv2.inRange(image, minBGR, maxBGR)

	points = []
	for i in range(2017):
		for j in range(3400):
			if mask.item((i, j)) == 255:
				points.append((i, j))
	points = np.array(points)
	
	kmeans = KMeans(n_clusters=4).fit(points)
	centers = kmeans.cluster_centers_
	# returns (y, x) tuples
	return centers


image1 = cv2.imread(sys.argv[1])
points1 = find_centers(image1)

if len(sys.argv) == 2:
	print(points1)

else:
	image2 = cv2.imread(sys.argv[2])
	points2 = find_centers(image2)

	# returns a matrix[i][j] of euclidean distances between points1[i] and points2[j]
	costs_matrix = cdist(points1, points2)

	_, assignment = linear_sum_assignment(costs_matrix)

	for i in range(4):
		print("We assign", points1[i], "to", points2[assignment[i]])
