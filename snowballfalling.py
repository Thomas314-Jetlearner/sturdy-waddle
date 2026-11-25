# import cv2
# import random
# cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# flakes= []



# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     frame.flip(frame, 1 )

#     wid = random.randint(0,640)
#     heigh = random.randint(0, 480)
#     flakes.append([wid,heigh])


#     for flake in flakes:
#         flake.x = wid
#         flake.y = heigh

#         cv2.circle(frame, (wid, heigh), 1.5, (246, 246, 255), -2)

#         flake[1] +=5
#         if flake[1] > 640:
#             flake[1] = 0
#             flake[0] = random.randint(20, 620)

#         if cv2.waitKey(50) & 0xFF == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()



    

import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

color = (0,0,255)

flakes = []
for i in range(100):
    wid = random.randint(0, 639)
    heigh = random.randint(0, 479)
    radius = random.randint(1, 5)  
    flakes.append([wid, heigh, radius])

while True:
    ret, frame = cap.read()

    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))
    edges = cv2.Canny(gray, 100, 200)
    output = np.zeros_like(frame)
    output[edges == 255] = color
    for flake in flakes:
  
        flake[1] += flake[2] + 1 

        
        if flake[1] >= 480:
            flake[1] = 0
            flake[0] = random.randint(0, 639)
            flake[2] = random.randint(1, 5) 
        cv2.circle(frame, (flake[0], flake[1]), flake[2], (color), -1)


    cv2.imshow("Snowfall", output)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('w'):
        color = (0, 0, 255)

    elif k == ord('e'):
        color = (0, 255, 0)

    elif k == ord('r'):
        color = (255, 0, 0)

    elif k == ord('t'):
        color = (0, 255, 255)

    elif k == ord('y'):
        color = (0, 100, 100)

    elif k == ord('u'):
        color = (100, 100, 0)

    elif k == ord('i'):
        color = (0, 255, 255)

    elif k == ord('o'):
        color = (255, 255, 0)

    elif k == ord('p'):
        color = (255, 0, 255)

    elif k == ord('q'):
        break

        

cap.release()
cv2.destroyAllWindows()