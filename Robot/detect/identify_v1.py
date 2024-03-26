import cv2
import mediapipe as mp
import serial

import math


#arduino = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)
mp_holistic = mp.solutions.holistic
capture = cv2.VideoCapture(0)

model = mp_holistic.Holistic(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5   
)


mp_drawing = mp.solutions.drawing_utils


vector_fingers = [0, 0, 0, 0, 0]
finger_count = 0

prev_right_hand_landmarks = None
prev_left_hand_landmarks = None


finger_tip_indices = [4, 8, 12, 16, 20]

while capture.isOpened():
    success, frame = capture.read()

    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    results = model.process(image)

 #Counting process

    # Right Hand
    if results.right_hand_landmarks:
        current_right_hand_landmarks = results.right_hand_landmarks.landmark
        print(f'Polegar Direita: {current_right_hand_landmarks[4].y}')
        print(f'Indicador Direita: {current_right_hand_landmarks[8].y}')
        print(f'Medio Direita: {current_right_hand_landmarks[12].y}')
        print(f'Anelar Direita: {current_right_hand_landmarks[16].y}')
        print(f'Mindinho Direita: {current_right_hand_landmarks[20].y}')

        dista1_1 = (current_right_hand_landmarks[9].x - current_right_hand_landmarks[4].x)**2
        dista2_1 = (current_right_hand_landmarks[9].x - current_right_hand_landmarks[8].x)**2
        dista3_1 = (current_right_hand_landmarks[9].x - current_right_hand_landmarks[12].x)**2
        dista4_1 = (current_right_hand_landmarks[9].x - current_right_hand_landmarks[16].x)**2
        dista5_1 = (current_right_hand_landmarks[9].x - current_right_hand_landmarks[20].x)**2
        
        dista1_2 = (current_right_hand_landmarks[9].y - current_right_hand_landmarks[4].y)**2
        dista2_2 = (current_right_hand_landmarks[9].y - current_right_hand_landmarks[8].y)**2
        dista3_2 = (current_right_hand_landmarks[9].y - current_right_hand_landmarks[12].y)**2
        dista4_2 = (current_right_hand_landmarks[9].y - current_right_hand_landmarks[16].y)**2
        dista5_2 = (current_right_hand_landmarks[9].y - current_right_hand_landmarks[20].y)**2

        dista1_3 = (current_right_hand_landmarks[9].z - current_right_hand_landmarks[4].z)**2
        dista2_3 = (current_right_hand_landmarks[9].z - current_right_hand_landmarks[8].z)**2
        dista3_3 = (current_right_hand_landmarks[9].z - current_right_hand_landmarks[12].z)**2
        dista4_3 = (current_right_hand_landmarks[9].z - current_right_hand_landmarks[16].z)**2
        dista5_3 = (current_right_hand_landmarks[9].z - current_right_hand_landmarks[20].z)**2

        distancia1 = math.sqrt(dista1_1 + dista1_2 + dista1_3)
        distancia2 = math.sqrt(dista2_1 + dista2_2 + dista2_3)
        distancia3 = math.sqrt(dista3_1 + dista3_2 + dista3_3)
        distancia4 = math.sqrt(dista4_1 + dista4_2 + dista4_3)
        distancia5 = math.sqrt(dista5_1 + dista5_2 + dista5_3)

        print(distancia1)
        
        if (distancia1 >= 0.20):
            print("Polegar aberto")
        else:
            print("Polegar fechado")

        if (distancia2 >= 0.20):
            print("Indicador aberto")
        else:
            print("Indicador fechado")

        if (distancia3 >= 0.20):
            print("Medio aberto")
        else:
            print("Medio fechado")

        if (distancia4 >= 0.20):
            print("Anelar aberto")
        else:
            print("Anelar fechado")
        
        if (distancia5 >= 0.20):
            print("Mindinho aberto")
        else:
            print("Mindinho fechado")
    
    if results.left_hand_landmarks:
        current_left_hand_landmarks = results.left_hand_landmarks.landmark
        print(f'Polegar Esquerda: {current_left_hand_landmarks[4]}')
        print(f'Indicador Esquerda: {current_left_hand_landmarks[8]}')
        print(f'Medio Esquerda: {current_left_hand_landmarks[12]}')
        print(f'Anelar Esquerda: {current_left_hand_landmarks[16]}')
        print(f'Mindinho: Esquerda {current_left_hand_landmarks[20]}')
      
    #Drawing process

    mp_drawing.draw_landmarks(
        image,
        results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )

    mp_drawing.draw_landmarks(
        image,
        results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )
    mp_drawing.draw_landmarks(
        image,
        results.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS
    )

    cv2.imshow("Live", image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
