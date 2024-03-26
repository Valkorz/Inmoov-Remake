
import cv2
import mediapipe as mp
import serial
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_holistic = mp.solutions.holistic


cap = cv2.VideoCapture(0)

model =  mp_hands.Hands(
  model_complexity=0,
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5
) 

model2 = mp_holistic.Holistic(
  static_image_mode=False,
  model_complexity=1,
  smooth_landmarks=True,
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5
)


while cap.isOpened():
    success, image = cap.read()
  

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model.process(image)
    results2 = model2.process(image)
   
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

   
    fingerCount = 0

    if results.multi_hand_landmarks:

      for hand_landmarks in results.multi_hand_landmarks:
      
        handIndex = results.multi_hand_landmarks.index(hand_landmarks)
        handLabel = results.multi_handedness[handIndex].classification[0].label

      
        handLandmarks = []

        
        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])

      
        if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
          fingerCount = fingerCount+1
          print("Polegar aberto")
        elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
          fingerCount = fingerCount+1

       
        if handLandmarks[8][1] < handLandmarks[6][1]:       
          fingerCount = fingerCount+1
          print("Indicador aberto")
        if handLandmarks[12][1] < handLandmarks[10][1]:     
          fingerCount = fingerCount+1
          print("Medio aberto")
        if handLandmarks[16][1] < handLandmarks[14][1]:    
          fingerCount = fingerCount+1
          print("Anelar aberto")
        if handLandmarks[20][1] < handLandmarks[18][1]:     
          fingerCount = fingerCount+1
          print("Mindinho aberto")

       
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )
        mp_drawing.draw_landmarks(
            image,
            results2.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS
        )
        print(fingerCount)


   
    
    cv2.imshow('Live', image)
    if cv2.waitKey(5) & 0xFF == 'q':
      break

cap.release()
cv2.destroyAllWindows()