import cv2

img = cv2.imread('sample.png')
cv2.namedWindow('screen2', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('screen2', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#cv2.moveWindow('screen2',1940,0)
cv2.imshow('screen2', img)
cv2.waitKey(0)
