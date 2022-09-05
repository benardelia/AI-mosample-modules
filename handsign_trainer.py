import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

video_capture = cv2.VideoCapture(0)
detector = HandDetector()
offsets = 20
shape = 300

# folder to save our signs
folder = 'Data/A'

while True:
    success, frame = video_capture.read()
    hands, hand_img = detector.findHands(frame)
    # hand return list of either 1 or 2 dictonary (2 dict if two hands detected and 
    # 1 dict if one hand detected), 
    # if-statement below crop the detected hand in a separate frame, to get hands images 
    # for training our module
    if hands:
        # hands[0] is the first hand to be detected 
        x, y, w, h = hands[0]['bbox']
        # create custome with constant shape to put hand image on it, so as to get images of same size
        # 255 just convert ones into 255 so as imsge could be white istead of (1) black 
        white_img = np.ones((shape, shape, 3), np.uint8) * 255
        image_crop = frame[y - offsets:y + h + offsets, x - offsets:x + w + offsets]
        
        
        
        
        try:
           
            aspectRatio = h/w
            if aspectRatio > 1:
                k = shape / h
                calc_width = math.ceil(k*w)
                image_crop_resized = cv2.resize(image_crop, (calc_width, shape))
                # put a croped image above particular scace of white imahe
                shift_gap = math.ceil((shape - calc_width) / 2)
                image_crop_resized_shape = image_crop_resized.shape
                white_img[:, shift_gap: shift_gap + calc_width] = image_crop_resized
            else:
                k = shape / w
                calc_heigth = math.ceil(k*h)
                image_crop_resized = cv2.resize(image_crop, (shape, calc_heigth))
                # put a croped image above particular scace of white imahe
                shift_gap = math.ceil((shape - calc_heigth) / 2)
                image_crop_resized_shape = image_crop_resized.shape
                white_img[shift_gap: shift_gap + calc_heigth, :] = image_crop_resized
            cv2.imshow('Hand image', image_crop)
            cv2.imshow('White image', white_img)
        except:
            pass
    cv2.imshow('Trainer', frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', white_img)
    # print(hands)
    
