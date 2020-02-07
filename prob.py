import cv2
import numpy as np
from sklearn.cluster import KMeans

image = cv2.imread("image.png")

target_bgr = [39, 39, 255]
minBGR = np.array(target_bgr)
maxBGR = np.array(target_bgr)

# Creates a mask that sets luminosity to 255 if target color, shape=(2017, 3400)
mask = cv2.inRange(image, minBGR, maxBGR)
# mask.item((y, x)) returns 255 or 0

points = []
for i in range(2017):
	for j in range(3400):
		if mask.item((i, j)) == 255:
			points.append((i, j))
points = np.array(points)
print("Points found")


# Display result
# cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Resized Window', 1400, 800)

# cv2.imshow('Resized Window', mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

kmeans = KMeans(n_clusters=4).fit(points)
print("Training done")
barycenter = kmeans.cluster_centers_
print(barycenter)