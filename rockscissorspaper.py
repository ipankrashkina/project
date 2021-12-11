from cv2 import cv2
import mediapipe as mp
import numpy as np

handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(frame)
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    results = handsDetector.process(flippedRGB)
    if results.multi_hand_landmarks is not None:
        x_point = int(results.multi_hand_landmarks[0].landmark[8].x * flippedRGB.shape[1])
        y_point = int(results.multi_hand_landmarks[0].landmark[8].y * flippedRGB.shape[0])
        x_p1 = int(results.multi_hand_landmarks[0].landmark[5].x * flippedRGB.shape[1])
        y_p1 = int(results.multi_hand_landmarks[0].landmark[5].y * flippedRGB.shape[0])
        x_middle = int(results.multi_hand_landmarks[0].landmark[12].x * flippedRGB.shape[1])
        y_middle = int(results.multi_hand_landmarks[0].landmark[12].y * flippedRGB.shape[0])
        x_m1 = int(results.multi_hand_landmarks[0].landmark[9].x * flippedRGB.shape[1])
        y_m1 = int(results.multi_hand_landmarks[0].landmark[9].y * flippedRGB.shape[0])
        x_ring = int(results.multi_hand_landmarks[0].landmark[16].x * flippedRGB.shape[1])
        y_ring = int(results.multi_hand_landmarks[0].landmark[16].y * flippedRGB.shape[0])
        x_r1 = int(results.multi_hand_landmarks[0].landmark[13].x * flippedRGB.shape[1])
        y_r1 = int(results.multi_hand_landmarks[0].landmark[13].y * flippedRGB.shape[0])
        if y_point > y_p1 and y_middle > y_m1 and y_ring > y_r1:
            print('камень')
        elif y_point < y_p1 and y_middle < y_m1 and y_ring > y_r1:
            print('ножницы')
        elif y_point < y_p1 and y_middle < y_m1 and y_ring < y_r1:
            print('бумага')


    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hands", res_image)
handsDetector.close()