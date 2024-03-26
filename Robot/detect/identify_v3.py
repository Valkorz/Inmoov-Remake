import cv2 as cv
import mediapipe as mp
import serial

mp_holistic = mp.solutions.holistic
capture = cv.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
finger_count = 0
finger_vector_D = [0, 0, 0, 0, 0]
finger_vector_E = [0, 0, 0, 0, 0]


               

model = mp_holistic.Holistic(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5   
)

while capture.isOpened():
    success, frame = capture.read()
    if not success:
        print("Failed to read frame")
        break

    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = model.process(image)

    if results.left_hand_landmarks:  # Checking for left hand landmarks
        landmarks = []
        for landmark in results.left_hand_landmarks.landmark:
            landmarks.append([landmark.x, landmark.y])
        
        
        if len(landmarks) >= 21:
            if landmarks [4][1] < landmarks[2][1]:
                print("Polegar (E)")
                finger_vector_D[0] = 1
            if landmarks[8][1] < landmarks[6][1]:       
                print("Indicador (E)")
                finger_vector_D[1] = 1
            if landmarks[12][1] < landmarks[10][1]:     
                print("Meio (E)")
                finger_vector_D[2] = 1
            if landmarks[16][1] < landmarks[14][1]:    
                print("Anelar (E)")
                finger_vector_D[3] = 1
            if landmarks[20][1] < landmarks[18][1]:     
                print("Mindinho (E)")
                finger_vector_D[4] = 1
           
            

    if results.right_hand_landmarks:  # Checking for left hand landmarks
        landmarks = []
        for landmark in results.right_hand_landmarks.landmark:
            landmarks.append([landmark.x, landmark.y])
        
        
        if len(landmarks) >= 21:
            if landmarks [4][1] < landmarks[2][1]:
                print("Polegar (D)")
                finger_vector_E[0] = 1
            if landmarks[8][1] < landmarks[6][1]:       
                print("Indicador (D)")
                finger_vector_E[1] = 1
            if landmarks[12][1] < landmarks[10][1]:     
                print("Meio (D)")
                finger_vector_E[2] = 1
            if landmarks[16][1] < landmarks[14][1]:    
                print("Anelar (D)")
                finger_vector_E[3] = 1
            if landmarks[20][1] < landmarks[18][1]:     
                print("Mindinho (D)")
                finger_vector_E[4] = 1


    mp_drawing.draw_landmarks(
        frame,
        results.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS
    )
    mp_drawing.draw_landmarks(
        frame,
        results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )
    mp_drawing.draw_landmarks(
        frame,
        results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS
    )

    cv.imshow("Live", frame)
    if cv.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
