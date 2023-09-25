import time
import cv2
import numpy as np
import pyautogui
from datetime import datetime, timedelta

frame_rate = 10.0

def record_video(video_filename, record_seconds):

    #print("A INCEPUT THREAD UL VIDEO",  datetime.now())
    screen_width, screen_height = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video_out = cv2.VideoWriter(video_filename, fourcc, frame_rate, (screen_width, screen_height))

    print("Înregistrează ecranul...")
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=record_seconds)
    print(end_time)

    # Calculează numărul de cadre necesare
    num_frames = int(frame_rate * record_seconds)

    for _ in range(num_frames):
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_out.write(frame)

    print("Înregistrare ecran finalizată.")

    video_out.release()

if __name__ == "__main__":
    record_video("test.avi", 13)