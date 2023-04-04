import cv2

img = cv2.imread('../DATA/wii.jpg')

while True :
    cv2.imshow('Hello CV', img)

    # If waited at least 1 ms AND pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()