
import cv2
import numpy as np
import pyautogui
from datetime import datetime, timedelta

#numarul de cadre pe secunda la care se va inregistra videoclipul
frame_rate = 10.0

#definim functia de inregistrare a desktopului avand ca parametrii numele fisierului video asa cum va fi salvat, nr de secunde ale video ului si un parametru bariera
def record_video(video_filename, record_seconds, barrier):
    #asteapta ca toate thread-urile sa se sincronizeze pentru ca inregistrarea video si audio sa porneasca simultan
    barrier.wait()

    #testam sa vedem daca cele doua inregistrari pornesc in acelasi timp
    #print("A INCEPUT THREAD UL VIDEO",  datetime.now())

    #definim dimensiunile ecranului prin utilizarea functiei size()
    screen_width, screen_height = pyautogui.size()
    #definim un cod cu patru caractere pentru codec-ul de compresie a videoclipului
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    #iintializam obiectul video_out
    video_out = cv2.VideoWriter(video_filename, fourcc, frame_rate, (screen_width, screen_height))

    print("Înregistrează ecranul...")
    start_time = datetime.now()
    #calculam momentul cand inregistrarea trebuie sa se opreasca adugand o perioada de timp
    end_time = start_time + timedelta(seconds=record_seconds)
    #print(end_time)

    # Calculează numărul de cadre necesare
    num_frames = int(frame_rate * record_seconds)

    for _ in range(num_frames):
        #captam cadre din videoclip folosind functia screenshot()
        screenshot = pyautogui.screenshot()
        #capturile de ecran le stocam intr-o matrice
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_out.write(frame)

    print("Înregistrare ecran finalizată.")
    #eliberam resursele
    video_out.release()

