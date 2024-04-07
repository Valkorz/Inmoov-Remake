from deepface import DeepFace
import cv2 as cv
import os

def identify(flow):

    capture = cv.VideoCapture(0)
    capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 640)

    counter_users = 0

    matching = False
   

    while True:
        sucess, frame = capture.read()
        if capture.isOpened():
            if flow == 1:
                cv.imshow("Signing Up", frame) 
                if cv.waitKey(5) & 0xFF == ord('q'):
                    cv.imwrite(f"Users/User{counter_users+1}.jpg", frame)
                    print("Signing up sucessfully")
                    break
            elif flow == 2:
                cv.imshow("Logging", frame)
                if cv.waitKey(5) & 0xFF == ord('q'):
                    cv.imwrite("Login.jpg", frame)
                    break
                

    for i in range (1,5):             
        capture.release()
        cv.destroyAllWindows()
    
    if flow == 2:  
        results = DeepFace.find(img_path="Login.jpg", db_path="Users")
        print(results[0]["distance"])
        os.remove(path="Login.jpg")
        matching = True
        
        return matching
        
