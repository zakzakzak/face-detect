import cv2  
import numpy as np
from PIL import ImageGrab
import time



def close_window():
    cv2.destroyAllWindows()
    exit()

def process_img(original_image) :
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=50)
    return processed_img

def main():
    last_time = time.time()
    while True : 
        screenshot = np.array(ImageGrab.grab(bbox=(-1400, 210, -50, 900), all_screens=True))[:, :, ::-1].copy()
        new_screen = process_img(screenshot)
        # Naming a window 
        cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL) 
        # Untuk resize window
        # cv2.resizeWindow("Resized_Window", int(1350*50/100), int(690*50/100)) 
        cv2.imshow("Resized_Window", new_screen)


        # Time counter
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            close_window()

if __name__ == '__main__':
    main()
