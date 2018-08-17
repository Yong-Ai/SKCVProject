import cv2
import numpy as np

if __name__ == '__main__':

    cap = cv2.VideoCapture('../resource/test.mp4')

    if (cap.isOpened() == False ):
        print("error opening the video files")

    while( cap.isOpened() ):
        ret, frame = cap.read()

        if ret == False:
            break

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()