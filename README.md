### Mediul de dezvoltare si functionalitate

Aplicatia a fost realizata utilizand ca mediu de dezvoltare PyCharm 2023.2.1 si are ca scop inregistrarea audio si video a unei ferestre de pe YouTube.
Aceasta implica realizarea a 4 fisiere de tip .py si anume un program principal unde vor fi testate functiile implementate.
### Implementare
Fisierul main.py reprezinta scriptul principal unde sunt testate celelalte functii implemnetate. Fisierul presupune definirea unei functii record_audio_and_video care este responsabila de inregistrarea audio si video simultan de pe un site web (YouTube) si de combinarea lor într-un fisier video final. Functia creeaza o bariera de sincronizare pentru a porni inregistrarile audio si video simultan pentru a evita decalaje. Apoi, deschide un browser Chrome pentru a reda un videoclip YouTube, initiaza doua fire de executie pentru inregistrarea audio si video, asteapta incheierea acestora, si prelucreaza inregistrarile. In cele din urma, suprapune sunetul pe videoclip, salveaza rezultatul si inchide resursele, inclusiv browser-ul Selenium.
Fisierul VideoRecorder.py contine functia record_video, care inregistreaza doar browser-ul deschis cu ajutorul bibliotecii Selenium.Ea utilizeaza o bariera de sincronizare pentru a asigura inceperea inregistrarii simultan cu inregistrarea audio. Se initializeaza un obiect video, apoi, se captureaza si se inregistreaza cadrele video in functie de durata specificata. La final, resursele sunt eliberate prin inchiderea obiectului video, iar inregistrarea video este salvata in fisierul specificat.
Fisierul AudioRecorder.py contine functia record_audio, care inregistreaza sunetul browser-ului. Pentru a inregistra doar sunetul furnizat de browser am modificat OutPut-ul dispozitivului audio 
pentru browser-ul Google Chrome(asa cum se poate observa in imaginea de mai jos), astfel inregistram doar sunetul furnizat de pagina de YouTube indiferent daca in paralel se aud si alte sunete pe desktop.
Fisierul calculate_sound_level.py contine functia extract_sound_level, care determina nivelul sunetului in db, din inregistarea audio, si il salveaza intr-un fisier .txt.

### Testare
Pentru a vedea functionalitatea aplicatiei este nevoie sa se descarce cele 4 fisiere de tip .py, sa se instaleze bibliotecile necesare si sa se ruleze fisierul main.py.
Fisierul VideoRecorder.py contine functia record_video, care inregistreaza doar browser-ul deschis cu ajutorul bibliotecii Selenium.

![image](https://github.com/IzabelaBurcica/Arobs/assets/106831283/c96c3c88-7380-49f0-b9ac-13b662e9cb27)
