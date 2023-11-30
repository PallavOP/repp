import cv2

image1 = cv2.imread(r"monarch.jpg")
image2 = cv2.imread(r"enstin.jpg")

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#a


#enw commensts

canny1 = cv2.Canny(gray1, 150, 200)
canny2 = cv2.Canny(gray2, 100, 170)

cv2.imshow("Canny Edge - Image 1", canny1)
cv2.imshow("Canny Edge - Image 2", canny2)
cv2.waitKey(0)

print("hello")