import cv2
import numpy as np
import os
import sys

IMAGE_PATH = 'test.png' 


WINDOW_NAME = 'Real-time RGB Threshold Adjustment'
MAX_THRESHOLD_VALUE = 255

def nothing(x):
    pass

def update_threshold(val):
    """
    ฟังก์ชัน Callback ที่ถูกเรียกใช้ทุกครั้งที่แถบเลื่อนถูกปรับค่า
    """
  
    b_th = cv2.getTrackbarPos('B_TH (Blue)', WINDOW_NAME)
    g_th = cv2.getTrackbarPos('G_TH (Green)', WINDOW_NAME)
    r_th = cv2.getTrackbarPos('R_TH (Red)', WINDOW_NAME)

    color_select = image.copy()
    
    bgr_threshold = [b_th, g_th, r_th]

    thresholds = (image[:,:,0] < bgr_threshold[0]) | \
                 (image[:,:,1] < bgr_threshold[1]) | \
                 (image[:,:,2] < bgr_threshold[2])

    color_select[thresholds] = [0, 0, 0]

    cv2.imshow(WINDOW_NAME, color_select)


if __name__ == '__main__':
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: ไม่พบไฟล์ภาพที่: {IMAGE_PATH}")
        sys.exit(1)
        
    image = cv2.imread(IMAGE_PATH)
    
    if image is None:
        print(f"Error: ไม่สามารถอ่านไฟล์ภาพที่: {IMAGE_PATH} ได้")
        sys.exit(1)

    cv2.namedWindow(WINDOW_NAME)

    # R Threshold (ช่องสีแดง)
    cv2.createTrackbar('R_TH (Red)', WINDOW_NAME, 200, MAX_THRESHOLD_VALUE, update_threshold)
    # G Threshold (ช่องสีเขียว)
    cv2.createTrackbar('G_TH (Green)', WINDOW_NAME, 200, MAX_THRESHOLD_VALUE, update_threshold)
    # B Threshold (ช่องสีน้ำเงิน)
    cv2.createTrackbar('B_TH (Blue)', WINDOW_NAME, 200, MAX_THRESHOLD_VALUE, update_threshold)
    
    update_threshold(0)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()