#Set vertical devide
import cv2   
# Read the image
img = cv2.imread('image_test.jpg')
print(img.shape)
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
left1 = img[:, :width_cutoff]
right1 = img[:, width_cutoff:]

#############################################
img = cv2.rotate(left1, cv2.ROTATE_90_CLOCKWISE)
####
print(img.shape)
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
l1 = img[:, :width_cutoff]
l2 = img[:, width_cutoff:]
#now image vertical
l1 = cv2.rotate(l1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("one_horisont_1.jpg", l1)
#
l2 = cv2.rotate(l2, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("one_horisont_2.jpg", l2)


#############################################
img = cv2.rotate(right1, cv2.ROTATE_90_CLOCKWISE)
####
print(img.shape)
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
r1 = img[:, :width_cutoff]
r2 = img[:, width_cutoff:]
#now image vertical
r1 = cv2.rotate(r1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("second_vhorisont_1.jpg", r1)
#
r2 = cv2.rotate(r2, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("second_horisont_2.jpg", r2)
