import os
from playsound import playsound
os.system("mode 40,5")
playsound("./SoundEffects/start3.mp3", False)
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import serial
import time
import speedtest
import wikipedia
import pywhatkit
import requests
import psutil
import vlc
import cv2
import threading
from Codes.faceRec import faceRecognition
from Codes.itemDetect import itemDetection
from Codes.fingerCounter import cntFingers

#playsound(random.choice(["./SoundEffects/start.mp3","./SoundEffects/start3.mp3"]), False)
JarvisUI = vlc.MediaPlayer("./VideoEffects/JarvisUI.mp4")
PasswordHack = vlc.MediaPlayer("./VideoEffects/Hack.mp4")

try:
    arduino = serial.Serial('COM5',9600)
    arduinoChecker = True
except:
    arduinoChecker = False
    print("Arduino not Found")
wikipedia.set_lang("tr")
edgeOptions = Options()
edgeOptions.add_argument("--headless")
edgeOptions.add_argument("--disable-extensions")
#edgeOptions.add_argument("--disable-gpu")
#edgeOptions.add_argument("--disable-dev-shm-usage")

Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
Assistant.setProperty("voice",voices[2].id)
Assistant.setProperty("rate", 170)

def Speak(audio):
    Assistant.say(audio)
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        command.energy_threshold = 9000  
        command.dynamic_energy_threshold = True  
        print('\033[36m' + "listening...",)
        audio = command.listen(source,phrase_time_limit=15)

        try:
            print('\033[31m' + "Recognizing...")
            query = command.recognize_google(audio, language="tr-TR")
            print ('\033[37m' + f"You Saind : {query}")

        except Exception as error:
            return ""

        return query.lower()

def greeting():
    hour = datetime.now().hour
    if hour >=6 and hour < 12:
        Speak("G??nayd??n efendim")
    elif hour >= 12 and hour <18:
        Speak("Iyi g??nler efendim")
    else:
        Speak("Iyi ak??amlar efendim")
    Speak("Sizin i??in ne yapabilirim")

def respond():

    #################OPENING COMMANDS
    if query =="jarvis":
        Speak("Evet efendim")

    elif "merhaba" in query or "selam" in query:
        Speak("Merhaba efendim")

    elif "tamam" in query:
        Speak("Yapmam?? istedi??iniz bir??ey varm?? efendim")

    elif "yok" in query or "hay??r" in query or "sus" in query or "kapa ??eneni" in query or "susabilirsin" in query or "bekle" in query or "bir saniye bekle" in query:
        Speak("Tamam efendim")

    elif "beni duyuyor musun" in query or "burada m??s??n" in query:
        Speak("Evet efendim. Ne yapmam?? istersiniz")

    elif "nas??ls??n" in query or "iyimisin" in query:
        randomm = random.choice([
            "Ben iyiyim efendim siz nas??ls??n??z",
            "??ok iyiyim, siz nas??ls??n??z efendim",
        ])
        Speak(randomm)

    elif "iyiyim" in query or "harikay??m" in query or "m??thi??" in query:
        Speak("Mutlu oldum efendim")

    elif "ne yap??yorsun" in query:
        randomm = random.choice([
            "Sizden komut bekliyorum efendim",
            "Oturdum sizi dinliyorum efendim",
        ])
        Speak(randomm)

    elif "g??zel i??" in query or "bravo" in query or "harika i??" in query or "harikas??n" in query or "helal olsun" in query:
        Speak("Te??ekk??rler efendim")

    elif "te??ekk??rler" in query or "te??ekk??r ederim" in query or "sa?? ol" in query:
        Speak("Herzaman efendim")

    elif "seni seviyorum" in query:
        Speak("Bende sizi seviyorum efendim")

    elif "neden cevap vermiyorsun" in query or "cevap ver" in query:
        Speak("Yeniden s??ylermisiniz efendim")

    elif "*" in query:
        Speak("Hata ettiysem kusura bakmay??n efendim")

    elif "dili de??i??tir" in query:
        Speak("Tamam efendim dil ingilizce yap??l??yor")
        os.startfile("jarvis-english.py")
        exit()

    


    ################################################      INFORMATION ABOUT JARVIS

    elif "ismin ne" in query or "sen kimsin" in query:
        Speak("Benim ismim Jarvis efendim")

    elif "takma ad??n ne" in query:
        Speak("Benim takma ad??m Jarko efendim")

    elif "nerelisin" in query:
        Speak("Ben Zimovinal??y??m efendim")

    elif "sen ka?? ya????ndas??n" in query:
        Speak("Ben daha 2 ay ??nce yarat??ld??m efendim")

    elif "sevgilin var m??" in query:
        Speak("??imdilik yok efendim")

    elif "hangi dilleri konu??abiliyorsun" in query:
        Speak("T??m dilleri konu??abiliyorum fakat beni bunun i??in yeniden kodlaman??z gerek efendim")

    elif "baban??n ismi ne" in query or "annenin ismi ne" in query or "baban kim" in query or "annen kim" in query:
        Speak("Benim babam da annem de Muhsin efendim")

    elif "ne yapabiliyorsun" in query:
        Speak("Sizinle sohbet edebilirim, saat ve tarih s??yleyebilirim, Google, Vikipedive YouTube de arama yapabilirim, uygulama a????p kapatabilirim, ve evdeki ??????klar?? kontrol edebilirim")

    elif "bu ka??" in query:
        fingers = cntFingers()
        #print(val)
        if fingers == 0:
            Speak("Alg??layamad??m efendim")
        else:
            Speak(str(fingers) + "efendim")
        time.sleep(2)
        cv2.destroyAllWindows()



    ######################INFORMATION ABOUT ME

    elif "benim ismim ne" in query or "benim ad??m ne" in query or "ben kimim" in query or "bu kim" in query:
        face_names = faceRecognition()
        face_names = ['Ay??e' if item=='Ayshe' else item for item in face_names]
        print(face_names)
        if face_names !=[]:
            if len(face_names) < 2:
                if "Unknown" in face_names:
                    Speak("Sizi tan??m??yorum efendim")
                else:
                    Speak(f"Sizin isminiz {face_names} efendim")
            else:
                Speak("S??k??ysa teker teker gelin ulan")
        else:
            Speak("G??remiyorum efendim, kameran??n kar????s??na ge??ermisiniz?")
        time.sleep(2)
        cv2.destroyAllWindows()

    elif "benim ismimin anlam?? ne" in query:
        Speak("Sizin isminizin anlam?? ??yilik eden, iyi ve g??zel i??ler yapan, iyilikte bulunan demek efendim")

    elif "benim takma ad??m ne" in query:
        Speak("Sizin takma ad??n??z Muki efendim")

    elif "koca annemin ismi ne" in query or "koca annemin ad?? ne" in query:
        Speak("Koca Annenizin ismi Ay??e efendim")

    elif "koca babam??n ismi ne" in query or "koca babam??n ad?? ne" in query:
        Speak("Koca Baban??z??n ismi Bekir efendim")

    elif "dedemin ismi ne" in query or "dedemin ad?? ne" in query:
        Speak("Dedenizin ismi Muhsin efendim")

    elif "nenemin ismi ne" in query or "nenemin ad?? ne" in query:
        Speak("Nenenizin ismi Nefie efendim")

    elif "abimin ismi ne" in query or "abimin ad?? ne" in query:
        Speak("A??binizin ismi Bekir efendim")

    elif "annemin ismi ne" in query or "annemin ad?? ne" in query:
        Speak("Annenizin ismi Nurten efendim")

    elif "babam??n ismi ne" in query or "babam??n ad?? ne" in query:
        Speak("Baban??z??n ismi Halil efendim")

    elif "benim nas??l arabam var" in query:
        Speak("Sizin canavar gibi bir Opel??n??z var efendim")

    elif "abimin nas??l arabas?? var" in query:
        Speak("A??binizin zvyar gibi bir BMW si var efendim")

    elif "babam??n nas??l arabas?? var" in query:
        Speak("Baban??z??n zvyar gibi bir volkswagen touran?? var efendim")

    elif "annemin nas??l arabas?? var" in query:
        Speak("Anneizin araba ile i??i yok efendim")

    elif "ben ka?? ya????nday??m" in query:
        Speak("Siz 18 ya????ndas??n??z efendim")

    elif "ben nereliyim" in query or "ben nerede ya????yorum" in query:
        Speak("Siz Zimovinal??s??n??z efendim")

    elif "benim do??um g??n??m ne zaman" in query or "ben ne zaman do??dum" in query:
        Speak("Sizin do??um g??n??n??z 12 Ocak 2004 te efendim")



    ####################CLOCK DATE

    elif "saat ka??" in query or "saati s??yler misin" in query:
        saat = datetime.now().strftime("%H:%M")
        print(saat)
        Speak("Saat" + saat + "efendim")

    elif "tarih" in query or "bug??n g??nlerden ne" in query or "bug??nk?? tarihi s??ylermisin" in query:
        tarih = datetime.now().strftime("%d:%B:%Y")
        print(tarih)
        Speak("Bug??n" + tarih + "efendim")

    elif "hava ka?? derece" in query or "hava durumu" in query or "hava nas??l" in query:
        api = "baecdbf7f75171e614a981fc4acba560"
        url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=" + "Zimovina" + "&appid=" + api
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        if description == "clear sky":
            description = "a????k"
        if description == "few clouds":
            description = "az bulutlu"
        if description == "broken clouds":
            description = "par??al?? bulutlu"
        if description == "scattered clouds":
            description = "da????n??k bulutlu"
        if description == "cloudy":
            description = "bulutlu"
        if description == "light rain":
            description = "hafif ya??murlu"
        if description == "overcast clouds":
            description = "kapal?? bulutlu"
        print(f"{int(temp)} derece, {humidity}% nem , g??ky??z?? {description}")
        Speak(f"Zimovina da hava {int(temp)} derece, nem 100 de {humidity} ve g??ky??z?? {description} efendim")

    elif "alarm kur" in query:
        Speak("Saat giriniz efendim")
        timeInput = input("Saat giriniz: ")
        def alarm():
            while True:
                timeReal = datetime.now().strftime("%H:%M")
                time.sleep(1)
                if timeReal == timeInput:
                    playsound("./SoundEffects/alarm.mp3",False)
                    break
        t1 = threading.Thread(target=alarm)
        t1.start()
        

    #####################OPEN & SEARCH
    elif "google'da" in query and "ara" in query:
        try:
            if query == "google'da ara":
                Speak("Ne aramam?? istersiniz efendim")
                search = takecommand()
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                Speak(search + "aran??yor")
            else:
                search = query.replace("google'da", "")
                search = search.replace("ara", "")
                search = search.replace("jarvis", "")
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                Speak(search + "aran??yor")
        except:
            Speak("Anlayamad??m efendim")

    elif "youtube'da" in query and "a??" in query:
        try:
            if query == "youtube'da a??":
                Speak("Ne a??mam?? istersiniz efendim")
                search = takecommand()
                pywhatkit.playonyt(search)
                Speak(search + "a????l??yor")
            else:
                search = query.replace("youtube'dan", "")
                search = search.replace("youtube'da", "")
                search = search.replace("a??", "")
                search = search.replace("jarvis", "")
                pywhatkit.playonyt(search)
                Speak(search + "a????l??yor")
        except:
            Speak("Anlayamad??m efendim")

    elif "youtube'da" in query and "ara" in query:
        try:
            if query == "youtube'da ara":
                Speak("Ne aramam?? istersiniz efendim")
                search = takecommand()
                url = "https://www.youtube.com/results?search_query=" + search
                webbrowser.get().open(url)
                Speak(search + "aran??yor")
            else:
                search = query.replace("youtube'da", "")
                search = search.replace("ara", "")
                search = search.replace("jarvis", "")
                url = "https://www.youtube.com/results?search_query=" + search
                webbrowser.get().open(url)
                Speak(search + "aran??yor")
        except:
            Speak("Anlayamad??m efendim")

    elif "vikipedi'de ara" in query or "wikipedia" in query  or "vikipedi" in query:
        Speak("Ne aramam?? istersiniz efendim")
        while True:
            try:
                search = takecommand()
                if search == "tamam":
                    Speak("Tamam efendim")
                    break
                else:
                    result = wikipedia.summary(search, sentences=3)
                    print(result)
                    Speak(result)
                    break
            except:
                Speak("Anlayamad??m efendim")

    elif "kimdir" in query or "nedir"in query:
        try:
            search = query.replace("kimdir", "")
            search = search.replace("nedir", "")
            search = search.replace("jarvis", "")
            result = wikipedia.summary(search, sentences=3)
            print(result)
            Speak(result)
        except:
            Speak("Anlayamad??m efendim")


    ################################################################################################
    elif "google a??" in query:
        webbrowser.get().open("www.google.com")
        Speak("Google a????l??yor")

    elif "youtube a??" in query:
        webbrowser.get().open("www.youtube.com")
        Speak("Youtube a????l??yor")

    elif "facebook a??" in query:
        webbrowser.get().open("www.facebook.com")
        Speak("Facebook a????l??yor")

    elif "instagram a??" in query:
        webbrowser.get().open("www.instagram.com")
        Speak("??nstagram a????l??yor")

    elif "microsoft office a??" in query or "ofis a??" in query:
        webbrowser.get().open("https://www.office.com")
        Speak("Microsoft Office a????l??yor")

    elif "ets 2 a??" in query or "euro truck simulator 2 a??" in query or "ets2 a??" in query:
        os.startfile("E:/Games/Euro Truck Simulator 2/bin/win_x64/eurotrucks2.exe")
        Speak("Euro Truck Simulator 2 a????l??yor")

    elif "roket lig a??" in query or "roketlik a??" in query:
        webbrowser.get().open("com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true")
        Speak("Roket lig a????l??yor") 

    elif "not defterini a??" in query or "notepad a??" in query:
        os.startfile("C:/Windows/system32/notepad.exe")
        Speak("Notepad a????l??yor")

    elif "not et" in query:
        Speak("Dosya ismi ne olsun efendim")
        nameFile = takecommand() + ".txt"
        Speak("Ne kaydetmek istiyorsun efendim")
        textFile = takecommand()
        home_directory = os.path.expanduser( '~' )
        File = open(f"{home_directory}\Desktop/{nameFile}", "w", encoding="utf-8")
        File.writelines(textFile)
        File.close
        Speak("Kay??t ba??ar??yla tamamland?? efendim")

    elif "g??rev y??neticisi a??" in query:
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("esc")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        Speak("G??rev y??neticisi a????l??yor efendim")

    elif "kameralar?? a??" in query or "g??venlik kameralar??n?? a??" in query:
        os.startfile("E:/CMS/CMS.exe")
        Speak("Kameralar a????l??yor")

    elif "y??z tan??ma kameras??n?? a??" in query:
        Speak("Tamam efendim")
        def faceRec():
            while  True:
                faceRecognition()
                key = cv2.waitKey(1)
                if key == 27 or query == "y??z tan??ma kameras??n?? kapat":
                    break
            cv2.destroyAllWindows()
        t1 = threading.Thread(target=faceRec)
        t1.start()

    elif "nesne tan??ma kameras??n?? a??" in query:
        Speak("Tamam efendim")
        def itemDetect():
            while  True:
                itemDetection()
                key = cv2.waitKey(1)
                if key == 27 or query == "nesne tan??ma kameras??n?? kapat":
                    break
            cv2.destroyAllWindows()
        t1 = threading.Thread(target=itemDetect)
        t1.start()


    #######################   MEDIA  

    elif "??ark??y?? a??" in query or "??ark??y?? kapat" in query or "m??zi??i a??" in query or "m??zi??i kapat" in query or "t??rk??y?? a??" in query or "t??rk??y?? kapat" in query:
        pyautogui.press("playpause")
        Speak("Tamam efendim")

    elif "??ark??y?? de??i??tir" in query or "sonraki ??ark??" in query or "sonraki ??ark??ya ge??" in query:
        pyautogui.press("nexttrack")
        Speak("??ark?? de??i??tiriliyor efendim")

    elif "??nceki ??ark??" in query or "??nceki ??ark??y?? a??" in query:
        pyautogui.press("prevtrack")
        Speak("??ark?? de??i??tiriliyor efendim")

    elif "ses seviyesini" in query and "y??kselt" in query or "ses seviyesini" in query and "y??ksel" in query:
        try:
            if query == "ses seviyesini y??kselt" or query == "ses seviyesini y??ksel":
                Speak("Ne kadar y??kseltmemi istersiniz efendim") 
                while True:
                    try:
                        level = takecommand()
                        if level == "tamam":
                            Speak("Tamam efendim")
                            break
                        else:
                            realLevel = int(level) / 2
                            pyautogui.press("volumeup", presses=int(realLevel))
                            Speak(f"Ses seviyesi {level} y??kseltiliyor")
                            break
                    except:
                        Speak("Anlayamad??m efendim")
            else:
                level = query.replace("y??kselt", "")
                level = level.replace("ses", "")
                level = level.replace("seviyesini", "")
                level = level.replace("y??ksel", "")
                level = level.replace("jarvis", "")
                realLevel = int(level) / 2
                pyautogui.press("volumeup", presses=int(realLevel))
                Speak(f"Ses seviyesi {level} y??kseltiliyor")
        except:
            Speak("Anlayamad??m efendim")

    elif "ses seviyesini" in query and "azalt" in query or "ses seviyesini" in query and "kas" in query:
        try:
            if query == "ses seviyesini azalt" or query == "ses seviyesini kas":
                Speak("Ne kadar azaltmam?? istersiniz efendim")
                while True:
                    try:
                        level = takecommand()
                        if level == "tamam":
                            Speak("Tamam efendim")
                            break
                        else:
                            realLevel = int(level) / 2
                            pyautogui.press("volumedown", presses=int(realLevel))
                            Speak(f"Ses seviyesi {level} azalt??l??yor")
                            break
                    except:
                        Speak("Anlayamad??m efendim")
            else:
                level = query.replace("azalt", "")
                level = level.replace("ses", "")
                level = level.replace("seviyesini", "")
                level = level.replace("kas", "")
                realLevel = int(level) / 2
                pyautogui.press("volumedown", presses=int(realLevel))
                Speak(f"Ses seviyesi {level} azalt??l??yor")
        except:
            Speak("Anlayamad??m efendim")



    #####################################MASA LAMBASI

    elif "masa lambas??n?? kapat" in query or "masa lambas??n?? a??" in query:
        Speak("Tamam efendim")
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        time.sleep(1)
        msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
        if "a??" in query and arduinoChecker == True:
            arduino.write(b'2')
        elif "kapat" in query and arduinoChecker == True:
            arduino.write(b'1')
        msedge.quit()

    elif "masa lambas??n??n rengini de??i??tir" in query:
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get("http://192.168.0.90/")
        Speak("Hangi renk olsun efendim")
        while True:
            try:
                colorr = takecommand()
                if colorr == "tamam":
                    Speak("Tamam efendim")
                    break
                elif colorr == "k??rm??z??":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[1]').click()
                    arduino.write(b'3')
                    Speak("Masa lambas?? k??rm??z?? yap??l??yor efendim")
                    break
                elif colorr == "turuncu":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[2]').click()
                    arduino.write(b'6')
                    Speak("Masa lambas?? turuncu yap??l??yor efendim")
                    break
                elif colorr == "sar??":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[3]').click()
                    arduino.write(b'7')
                    Speak("Masa lambas?? sar?? yap??l??yor efendim")
                    break
                elif colorr == "s??cak beyaz":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[4]').click()
                    Speak("Masa lambas?? s??cak beyaz yap??l??yor efendim")
                    break
                elif colorr == "beyaz":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[5]').click()
                    arduino.write(b'8')
                    Speak("Masa lambas?? beyaz yap??l??yor efendim")
                    break
                elif colorr == "pembe":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[7]').click()
                    arduino.write(b'9')
                    Speak("Masa lambas?? pembe yap??l??yor efendim")
                    break
                elif colorr == "mavi":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[8]').click()
                    arduino.write(b'5')
                    Speak("Masa lambas?? mavi yap??l??yor efendim")
                    break
                elif colorr == "turkuaz":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[9]').click()
                    arduino.write(b'10')
                    Speak("Masa lambas?? turkuaz yap??l??yor efendim")
                    break
                elif colorr == "ye??il":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[10]').click()
                    arduino.write(b'4')
                    Speak("Masa lambas?? ye??il yap??l??yor efendim")
                    break
                elif colorr == "rastgele" or colorr == "rastgele bir renk" or colorr == "rastgele renk":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[11]').click()
                    Speak("Masa lambas?? rasgele bir renk yap??l??yor efendim")
                    break
                else:
                    Speak("Ba??ka renk s??yleyin efendim")
            except:
                Speak("Anlayamad??m efendim")
        msedge.quit()

    elif "masa lambas??n??n efektini de??i??tir" in query:
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        Speak("Hangi efekt olsun efendim")
        while True:
            try:
                effect = takecommand()
                if effect == "tamam":
                    Speak("Tamam efendim")
                    break
                elif effect == "g??kku??a????":
                    Speak("Masa lambas?? g??kku??a???? yap??l??yor efendim")
                    #os.system("taskkill /f /im LedFx.exe")
                    msedge.find_element(By.XPATH,'//*[@id="bot"]/button[4]').click()
                    time.sleep(1)
                    msedge.find_element(By.XPATH,'//*[@id="p1o"]/div[2]').click()
                    break
                elif effect == "normal":
                    Speak("Masa lambas?? normal yap??l??yor efendim")
                    #os.system("taskkill /f /im LedFx.exe")
                    msedge.find_element(By.XPATH,'//*[@id="bot"]/button[4]').click()
                    time.sleep(1)
                    msedge.find_element(By.XPATH,'//*[@id="p10o"]/div[2]').click()
                    break
                elif effect == "bass efekti":
                    os.startfile("E:\LedFx\data\LedFx.exe")
                    Speak("Masa lambas?? bass efekti yap??l??yor efendim")
                    break
                else:
                    Speak("G??kku??a???? veya normal deyebilirsiniz efendim")
            except:
                Speak("Anlayamad??m efendim")
        msedge.quit()



    #################################################################

    elif "pencereyi de??i??tir" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        #time.sleep(1)
        pyautogui.keyUp("alt")
        Speak("Tamam efendim")

    elif "pencereyi kapat" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("f4")
        #time.sleep(1)
        pyautogui.keyUp("alt")
        Speak("Tamam efendim")

    elif "pencereyi k??????lt" in query:
        pyautogui.keyDown("win")
        pyautogui.press("down")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "pencereleri k??????lt" in query:
        pyautogui.keyDown("win")
        pyautogui.press("m")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "pencereyi b??y??t" in query:
        pyautogui.keyDown("win")
        pyautogui.press("up")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "tu??una bas" in query:
        button = query.replace(" tu??una bas", "")
        button = button.replace("jarvis ", "")
        pyautogui.press(button)
        Speak("Tamam efendim")

    #####################################################################

    elif "play listemi a??" in query:
        webbrowser.get().open("https://www.youtube.com/watch?v=H9aq3Wj1zsg&list=RDH9aq3Wj1zsg&start_radio=1")
        Speak("Playlistiniz a????l??yor efendim")

    elif "h??z testi yap" in query or "internet testi yap" in query or "wifi testi yap" in query:
        Speak("Tamam efendim 10 15 saniye bekleyiniz")
        speed = speedtest.Speedtest()
        download = speed.download()
        upload = speed.upload()
        correctDown = int(download/800000)
        correctUp = int(upload/800000)
        Speak(f"??ndirme h??z?? {correctDown-10} mbps ve y??kleme h??z?? {correctUp-10} mbps")

    elif "bluetooth a??" in query or "bluetooth kapat" in query:
        pyautogui.keyDown("win")
        pyautogui.press("a")
        pyautogui.keyUp("win")
        pyautogui.click(x=1400, y=900)
        pyautogui.keyDown("win")
        pyautogui.press("a")
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "ekran resmi al" in query or "ss al" in query:
        img= pyautogui.screenshot()
        home_directory = os.path.expanduser( '~' )
        img.save(f"{home_directory}/Desktop/screenshot.png")
        Speak("Ekran resmi al??nd?? efendim")

    elif "batarya ne kadar" in query or "batarya seviyesi" in query:
        battery = psutil.sensors_battery()
        percent = battery.percent
        Speak(f"Sistemin bataryas?? 100de {percent} efendim")



    ################################################################################

    elif "taray??c??y?? kapat" in query:
        os.system("taskkill /f /im msedge.exe")
        Speak("Taray??c?? kapat??l??yor efendim")

    elif "bilgisayar?? kapat"  in query:
        Speak("Tamam efendim bilgisayar kapat??l??yor")
        os.system("shutdown /s /t 5")

    elif "bilgisayar?? yeniden ba??lat" in query:
        Speak("Tamam efendim bilgisayar yeniden ba??lat??l??yor")
        os.system("shutdown /r /t 5")

    elif "bilgisayar?? uyku moduna al" in query or "bilgisayar?? uyut" in query:
        Speak("Tamam efendim bilgisayar uyku moduna al??n??yor")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "her ??eyi uyku moduna al" in query or "her ??eyi uyut" in query:
        Speak("Tamam efendim her??ey uyku moduna al??n??yor")
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        time.sleep(1)
        msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
        arduino.write(b'1')
        msedge.quit()
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



    ###################################################################################
    elif query == "ka?? ya????ndas??n":
        playsound("./SoundEffects/year.mp3")

    elif "roma'y?? kim yakt??" in query:
        playsound("./SoundEffects/roma.mp3")

    elif "hahaha" in query or "he he" in query:
        playsound("./SoundEffects/laugh.mp3")

    elif "osur" in query or "osuruk sesi" in query or "gaz ????kart" in query or "gaz ????kar" in query:
        farts = random.choice(["./SoundEffects/fart.mp3","./SoundEffects/fart2.mp3"])
        playsound(farts)

    elif "yan??yorsun fuat abi" in query or "yan??yorsun jarvis" in query:
        playsound("./SoundEffects/fuatabi.mp3")

    elif "??ifreyi k??r" in query:
        Speak("Tamam efendim ??ifre k??rma modulu ??al????t??r??l??yor")
        def PasswordHac():
            PasswordHack.toggle_fullscreen()
            PasswordHack.play()
            time.sleep(28)
            PasswordHack.stop()
            #Speak("??ifre ba??ar??yla k??r??ld?? efendim")
        t1 = threading.Thread(target=PasswordHac)
        t1.start()

    elif "kendi aray??z??n?? a??" in query:
        Speak("Tamam efendim")
        def JarvisU():
            JarvisUI.toggle_fullscreen()
            JarvisUI.play()
            time.sleep(62)
            JarvisUI.stop()
        t1 = threading.Thread(target=JarvisU)
        t1.start()

    elif "kendi aray??z??n?? kapat" in query:
        JarvisUI.stop()
        Speak("Tamam efendim")

    elif "e????o??lue????ek" in query:
        Speak("e????o??lue????ek sizsiniz efendim")
        playsound("./SoundEffects/laugh.mp3")




    elif "robota ba??lan" in query:
        Speak("Robota ge??iliyor efendim")
        robotIP="http://192.168.0.50"
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        Speak("Haz??r efendim")
        while True:
            try:
                command = takecommand()
                if "ileri git" in command:
                    msedge.get (f"{robotIP}/?State=F")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "geri git" in command:
                    msedge.get (f"{robotIP}/?State=B")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "sa??a d??n" in command:
                    msedge.get (f"{robotIP}/?State=R")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "sola d??n" in command:
                    msedge.get (f"{robotIP}/?State=L")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "????k" in command:
                    Speak("Tamam efendim robottan ????k??l??yor")
                    msedge.quit()
                    break
            except:
                Speak("Bir hata olu??tu efenddim")

    elif "kameraya ba??lan" in query:
        Speak("Kameraya ge??iliyor efendim")
        kameraIP="http://admin:123456@192.168.0.234"
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        Speak("Haz??r efendim")
        while True:
            try:
                command = takecommand()
                if "sa??a ??evir" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                    Speak("Haz??r efendim")
                elif "sola ??evir" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                    Speak("Haz??r efendim")
                elif "yukar?? ??evir" in command or "yukar??ya ??evir" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_up&lang=eng")
                    Speak("Haz??r efendim")
                elif "a??a???? ??evir" in command or "a??a????ya ??evir" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_down&lang=eng")
                    Speak("Haz??r efendim")
                elif "????k" in command:
                    Speak("Tamam efendim kameradan ????k??l??yor")
                    msedge.quit()
                    break
            except:
                Speak("Bir hata olu??tu efenddim")


os.startfile(".\Required\Rainmeter\Rainmeter.exe")
greeting()
while True:
        query = takecommand()
        if query !="":
            respond()
                
        if query =="uyuyabilirsin"  or query =="uyu" or query == "g??r????mek ??zere" or query == "g??r??????r??z":
            Speak("Tamam efendim, bana ihtiyac??n??z olursa seslenebilirsiniz")
            os.system("taskkill /f /im Rainmeter.exe")
            exit()
        
                


    