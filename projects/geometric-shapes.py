import cv2

image = cv2.imread('lena.jpg', 1)

image = cv2.line(image, (0,0), (255,255), (0,0,255), 5)
image = cv2.arrowedLine(image, (0,255), (255,255), (0,255,0), 5)
image = cv2.arrowedLine(image, (0,510), (255,255), (255,0,0), 5)
image = cv2.rectangle(image, (330,50), (500,200), (255,0,0), 5)

cv2.imshow('Lena', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

