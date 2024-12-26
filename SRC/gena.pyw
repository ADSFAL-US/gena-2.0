import speech_recognition as sr
import json
import pyttsx3
import webbrowser as WB
import os
import getpass
import sys
import pyjokes as pj
from googletrans import Translator
import time
search = 0
listes = 0
steam_start = 0

commands = {"say_hello": ["привет","здравствуй","хай","hi","hello","здравия желаю","здравия тебе","желаю здравия"],
            "name": ["гена","генадий","геннадий","геняша","геша","геночка","ген"],
            "web": ["браузер","хром","гугл","гуглхром","гугл хром","browser","web browser","google","chrome","google chrome"],
            "mostes": ["какие у тебя возможности","что ты умеешь","что ты знаешь"],
            "open": ["открой","запусти","выведи","покажи"],
            "youtube": ["ютуб","youtube","ютьюб","утуб"],
            "explorer": ["проводник","файлы","файл менеджер","менеджер файлов","file manager","explorer"],
            "downloads": ["папку загрузок","загрузки","скачанное","загруженное","папку downloads","downloads","папку скачанное"],
            "say": ["скажи","расскажи","поясни","отвесь"],
            "joke": ["шутку","анекдот","прикол","смешнявку"],
            "search": ["поищи","найди","загугли","нагугли","погугли","отищи"],
            "steam":["steam", "стим"],
            "start_app": ["запусти игру", "запусти", "start", "запускай игру", "включи игру"]}

steamapps = {"1818450":["stalcraftx", "stalcraft", "сталкрафт", "сталкрафтx"],
             "387990":["scrap mechanic", "скрап механик", "скраб механик"],
             "252490":["rust", "раст"],
             "730":["cs2", "csgo", "conter strike", "кс2","ксго","кс","cs","каэс","контру"],
             " ":["стим", "steam"]
             }



def say(word):
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty("voice", "ru")

    for voice in voices:
        if voice.name == "Pavel":
            tts.setProperty("voice", voice.id)
    tts.say(word)
    print(word)
    tts.runAndWait()

trr = Translator()

def start_steamapp(app):
    for steamapp in commands["start_app"]:
        for steams in commands["steam"]:
            if str(steamapp) + str(steams) in app:
                say("уже запускаю steam")
                WB.open_new("steam://rungameid")
                return(0)
            else:
                for steamapp in steamapps:
                    for appnames in steamapps[steamapp]:
                        if app in appnames:
                            say("уже запускаю "+str(app))
                            WB.open_new("steam://rungameid/"+str(steamapp))
                            return(0)
                say("извините, я не знаю эту игру")
                return(1)
                        

def get_anekdot():
    joke = pj.get_joke()
    print(joke)
    joke_result = trr.translate(joke, dest = "ru")
    return(joke_result.text)


r = sr.Recognizer()


def comm_out(cout, search, steam_start):
    
    for steam in commands["start_app"]:
        if str(steam) in cout:
            say("что вам запустить, повелитель?")
            with sr.Microphone() as src:
                r.adjust_for_ambient_noise(src, duration=0.25)
                aud = r.listen(src,phrase_time_limit=5)
            cout = r.recognize_google(aud, language="ru-RU").lower()
            steam_start = 1
            
    if steam_start == 1:
        start_steamapp(cout)
        steam_start = 0
    
    
    
    for s in commands["search"]:
        for d in commands["web"]:
            if search == 0:
                if ("за"+str(d)+"и") == cout or (str(s)) == cout:
                    say("что вам найти, повелитель?")
                    with sr.Microphone() as src:
                        r.adjust_for_ambient_noise(src, duration=0.25)
                        aud = r.listen(src,phrase_time_limit=5)
                    cout = r.recognize_google(aud, language="ru-RU").lower()
                    search = 1

        

    if search == 1:
        WB.open("https://www.google.com/search?q="+cout)
        say("уже ищу, мой повелитель")
        search = 0


    



        
    print("you => " + str(cout))
    for b in commands["say_hello"]:
        if (str(b)) == cout:
            say("приветствую вас о повелитель")


    for c in commands["mostes"]:
        if (str(c)) == cout:
            say("генадий умеет: повелевать судьбой человечества по собственному желанию")
            say("владеет всеми кольцами саурона и камнями бесконечности")
            say("и так же по мелочи: делать за вас недостойную работу по-типу: откртие браузера, загрузок, youtube. к этому относится и использование поиска браузера.")
            say("просто скажите мне 'гена загугли', и я с радостью найду для вас необходимую информацию")

       
    for d in commands["web"]:
        for e in commands["open"]:
            if (str(e) + " " + str(d)) == cout:
                say("уже повелеваюсь")
                WB.open_new_tab("google.com")

       
    for f in commands["youtube"]:
        for e in commands["open"]:
            if (str(e) + " " + str(f)) == cout:
                say("уже открываю")
                WB.open_new_tab("m.youtube.com")


       
    for g in commands["explorer"]:
        for e in commands["open"]:
            if (str(e) + " " + str(g)) == cout:
                say("уже открываю")
                os.system(r"explorer.exe c:\\")



    for h in commands["downloads"]:
        for e in commands["open"]:
            if (str(e) + " " + str(h)) == cout:
                say("уже открываю")
                downl1 = "\\Downloads"
                username = getpass.getuser()
                downl_folder = "explorer.exe C:\\Users\\"
                    
                os.system(downl_folder+str(username)+downl1)


        
    for h in commands["say"]:
        for e in commands["joke"]:
            if (str(h) + " " + str(e)) == cout:
                say("сейчас расскажу.")
                say(str(get_anekdot()))

        
    if "отключись" == cout:
        say("отключаюсь. надеюсь я был вам полезен")
                
        sys.exit(0)








say("гена готов к работе, что прикажете повелитель?")


while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.25)
        audio = r.listen(source,phrase_time_limit=5)
        
    try:
        
        cin = r.recognize_google(audio, language="ru-RU").lower()

        
        if listes == 1:
            comm_out(cin, search, steam_start)

        listes = 0

        if listes == 0:
            for n in commands["name"]:
                if (n in cin) and listes == 0:
                    say("слушаю, повелитель")
                    listes = 1
        
        
                
    except sr.UnknownValueError:
        print("...")