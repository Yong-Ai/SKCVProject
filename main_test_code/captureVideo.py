# reference
#  https://nrsyed.com/2018/02/12/get-pixel-rgb-value-from-webcam-video-in-opencv-c-and-python/

import cv2

if __name__ == '__main__':

    cap = cv2.VideoCapture('../resource/test.mp4')

    if not cap.isOpened():
        raise RuntimeError('Error opening VideoCapture.')

    while( cap.isOpened() ):
        ret, frame = cap.read()

        if ret == False:
            break

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()