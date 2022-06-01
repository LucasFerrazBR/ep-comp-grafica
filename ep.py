import cv2
import numpy as np

video = cv2.VideoCapture('Sistemas Distribuídos – Aula 01 - Introdução aos Sistemas Distribuídos.mp4')

while video.isOpened():
    ret,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, im_bw = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
    dilate = cv2.dilate(im_bw, kernel, iterations=5)
    result = cv2.bitwise_xor(dilate, gray)
    _, result_bw = cv2.threshold(result, 128, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_not(result_bw)

    cv2.imshow('Resultado', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()