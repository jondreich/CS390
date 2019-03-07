import numpy as np
import cv2

kernel_sharpening = np.array([[-1,-1,-1], [-1, 9.1,-1], [-1,-1,-1]])

cap0 = cv2.VideoCapture(0)
#cap0.set(3, 160)
#cap0.set(4, 160)

while(True):
    ret, frame = cap0.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sharp = cv2.filter2D(gray, -1, kernel_sharpening)
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow('frame', cv2.flip(edges, 1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cv2.destroyAllWindows()