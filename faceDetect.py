import cv2  
import numpy as np
from PIL import ImageGrab

face_ref = cv2.CascadeClassifier("face_ref.xml")

def close_window():
    cv2.destroyAllWindows()
    exit()

def face_detection(frame):
    optimized_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale(optimized_frame, scaleFactor=3.1, minSize=(40,40),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    return faces

def drawer_box(frame):
    for x,y,w,h in face_detection(frame):
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)

def main():
    while True : 
        screenshot = np.array(ImageGrab.grab(bbox=(-1250, 200, -250, 900), all_screens=True))[:, :, ::-1].copy()
        # screenshot2 = cv2.resize(screenshot, (int(1000*90/100), int(700*90/100)))
        drawer_box(screenshot)
        

        # Naming a window 
        cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL) 
        
        # Using resizeWindow() 
        cv2.resizeWindow("Resized_Window", int(1000*90/100), int(700*90/100)) 

        cv2.imshow("Resized_Window", screenshot)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_window()

if __name__ == '__main__':
    main()
