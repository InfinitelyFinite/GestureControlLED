import cv2
from HandTrackingModule import handDetector
import math
from serial import Serial
from threading import Thread
from time import sleep

cap = cv2.VideoCapture(0)
detector = handDetector(detectionCon=0.8)
ser = Serial('/dev/cu.usbserial-10',9600)

def changeBrightness(length):
    length = int(length)
    ser.write(str(255-length).encode())
    sleep(1)
    print(255-length)

def main():
    x = Thread(target=changeBrightness)
    while True:
        _, frame = cap.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(frame, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

            length = math.hypot(x2 - x1, y2 - y1)

            if length < 50:
                cv2.circle(frame, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                length = 0
            elif length > 255:
                length = 255

            if x.is_alive():
               pass
            else:
                x = Thread(target=changeBrightness, args=(length,))
                x.start()



        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

if __name__ == "__main__":
    main()