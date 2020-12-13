import cv2   

# load image
img = cv2.imread('divide_image_4_parts.png')

##########################################
# At first vertical devide image         #
##########################################
# start vertical devide image
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
left1 = img[:, :width_cutoff]
right1 = img[:, width_cutoff:]
# finish vertical devide image

##########################################
# At first Horizontal devide left1 image #
##########################################
#rotate image LEFT1 to 90 CLOCKWISE
img = cv2.rotate(left1, cv2.ROTATE_90_CLOCKWISE)
# start vertical devide image
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
l1 = img[:, :width_cutoff]
l2 = img[:, width_cutoff:]
# finish vertical devide image
#rotate image to 90 COUNTERCLOCKWISE
l1 = cv2.rotate(l1, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save
cv2.imwrite("one_horisont_1.jpg", l1)
#rotate image to 90 COUNTERCLOCKWISE
l2 = cv2.rotate(l2, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save
cv2.imwrite("one_horisont_2.jpg", l2)

##########################################
# At first Horizontal devide right1 image#
##########################################
#rotate image RIGHT1 to 90 CLOCKWISE
img = cv2.rotate(right1, cv2.ROTATE_90_CLOCKWISE)
# start vertical devide image
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
r1 = img[:, :width_cutoff]
r2 = img[:, width_cutoff:]
# finish vertical devide image
#rotate image to 90 COUNTERCLOCKWISE
r1 = cv2.rotate(r1, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save
cv2.imwrite("second_vhorisont_1.jpg", r1)
#rotate image to 90 COUNTERCLOCKWISE
r2 = cv2.rotate(r2, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save
cv2.imwrite("second_horisont_2.jpg", r2)

