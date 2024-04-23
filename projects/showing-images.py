import cv2

img = cv2.imread('lena.jpg', -1) # -1,0,1
print(img)

cv2.imshow('image', img)
k = cv2.waitKey(5000)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena2.jpg', img)
    cv2.destroyAllWindows()