import cv2

def click_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)


img = cv2.imread("solar-system.jpg")

cv2.putText(img,
    "Sun" ,
    (20, 300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Mercury" ,
    (110, 180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Venus" ,
    (190, 265),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Earth" ,
    (285, 265),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Mars" ,
    (382, 265),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Jupiter" ,
    (480, 100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Saturn" ,
    (680, 100),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Uranus" ,
    (960, 130),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.putText(img,
    "Neptune" ,
    (1110, 290),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255))

cv2.imshow("Solar System", img)

cv2.imwrite("Solar_systemwithname.jpg", img)

cv2.setMouseCallback("Solar System", click_event)

cv2.waitKey(0)