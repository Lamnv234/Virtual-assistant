import subprocess
import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib3 
import pyautogui
import urllib.request as urllib2
from random import choice 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
##########################################################################
language = 'vi'
wikipedia.set_lang('vi')
##########################################################################
def speak(text):
    print("Lenona: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")
###########################################################################
def get_audio():
    print("\nLeona:\tEm \tĐang nghe nè\tXD\n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bạn: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0
###########################################################################
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 3:
        	gt = open('gettext.txt', 'r', encoding='UTF-8')
        	nghe_khong_ro=gt.readlines()
        	speak(choice(nghe_khong_ro))
        	time.sleep(4)
    time.sleep(3)
    stop()
    return 0
############################################################################    
def stop():
    gb = open('goodbye.txt', 'r', encoding='UTF-8')
    good_bye=gb.readlines()
    speak(choice(good_bye))
    time.sleep(3)
###########################################################################
def hello(name):
    hour = int(strftime('%H'))
    if hour >= 6 and hour<10:
        sau_AI = ["Chào buổi sáng {}. Chúc anh một ngày tốt lành.".format(name),
                  "Chào buổi sáng {}. Nếu anh không vui hãy về đây với em nhé".format(name)]
        speak(choice(sau_AI))
    elif 10 <= hour>=10 and hour<12:
        muoi_AI = ["Chào buổi trưa {}. Anh đã ăn trưa chưa nhỉ.".format(name),
                   "Chào buổi trưa {}. Nếu anh thấy mệt thì nghỉ ngơi đi nhé.".format(name)]
        speak(choice(muoi_AI))
    elif 12 <= hour>=12 and hour<18:
        muoihai_AI = ["Chào buổi chiều {}. Anh đã dự định gì cho chiều nay chưa.".format(name),
                      "Chào buổi chiều {}. Anh đang làm gì thế?.".format(name),
                      "Chào buổi chiều {}. Sắp tối rồi anh đã ăn cơm chưa?.".format(name)]
        speak(choice(muoihai_AI))
    elif 18 <= hour>=18 and hour<21:
        muoitam_AI = ["Chào buổi tối {}. Anh đã ăn tối chưa nhỉ.".format(name),
                      "Chào buổi tối {}. Nếu anh chưa ăn tối, Em chúc bạn ăn tối vui vẻ nhé .".format(name)]
        speak(choice(muoitam_AI))
    elif hour>=21 and hour<24:
        haimot_AI = ["Chào buổi tối {}. Đã khuya rồi anh vẫn chưa đi ngủ sao?.".format(name),
                     "Chào buổi tối {}. Nếu anh chuẩn bị đi ngủ thì em chúc bạn ngủ ngon nhé.".format(name),
                     "Chào buổi tối {}. Nếu anh buồn ngủ thì hãy ngủ đi nhé.".format(name)]
        speak(choice(haimot_AI))
    time.sleep(7)
#############################################################################
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text or "phút" in text:
        speak('Bây giờ là %d Giờ %d Phút %d Giây' % (now.hour, now.minute, now.second))
        time.sleep(1)
    elif "ngày" in text or "tháng" in text or "năm" in text:
        speak("Hôm nay là Ngày %d Tháng %d Năm %d" % (now.day, now.month, now.year))
        time.sleep(2)
    else:
        speak("Xin lỗi em chưa hiểu ý của anh. anh nói lại được không?")
    time.sleep(4)
#####################################################################################
def open_application(text):
    if "google" in text or "Chrome" in text:
        speak("Đang Mở Google Chrome")
        time.sleep(2)
        subprocess.call('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe') 
    elif "soạn văn bản" in text or "word" in text:
    	speak("Đang mở Word")
    	time.sleep(3)
    	subprocess.call('C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.EXE')
    elif "excel" in text or "bảng tính" in text:
        speak("Đang Mở Microsoft Excel")
        time.sleep(2)
        subprocess.call('C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.EXE')
    elif "Zalo" in text or "da lô" in text or "zalo" in text:
    	speak(" Đang mở zalo") 
    	time.sleep(2)
    	subprocess.call('C:\\Users\\Admin\\AppData\\Local\\Programs\\Zalo\\zalo.exe')  
    elif "tắt notepad" in text or "nót bát" in text:
        os.system("taskkill /f /im notepad.exe")
    elif "tắt Chrome" in text:
        os.system("taskkill /f /im chrome.exe") 
    else:
        speak("Xin lỗi, Ứng dụng anh yêu cầu chưa được cài đặt. anh hãy thử lại sau nhé!")
        time.sleep(2)
########################################################################################
def open_website(text):
    if "Youtube" in text or "youtube" in text:
        speak("Đang mở Youtube")
        time.sleep(2)
        webbrowser.open("www.youtube.com")
        speak("Youtube đã được mở nhe anh")
        time.sleep(2)
    elif "Facebook" in text or "face" in text or "facebook" in text:
        speak("Đang mở facebook")
        time.sleep(2)
        webbrowser.open("www.facebook.com")
        speak("Facebook đã được mở nhe anh")
        time.sleep(2)
    elif "24 giờ" in text or "hai mươi bốn giờ" in text:
        speak("Đang mở 24h.com.vn")
        time.sleep(2)
        webbrowser.open("www.24h.com.vn")
    elif "kênh 14" in text:
        speak("Đang mở kênh 14 .com.vn")
        time.sleep(3)
        webbrowser.open("www.kenh14.com.vn")
        speak("Kênh 14 đã được mở nhe anh")
        time.sleep(4)
    else:
        speak("Không tìm thấy trang web nhe anh")
        time.sleep(2)
######################################################################################
def profile_me(text):
    if "chứng minh nhân dân" in text:
        speak("3, 1, 2, 0, 2, 1, 2, 4, 8")
        time.sleep(5)
    elif "ngày sinh" in text:
        speak("23, 04, 1990")
        time.sleep(3)
    elif "vợ" in text:
        speak(" vợ anh tên Phạm Thị Lưu luyến, sinh ngày 06 tháng 03 năm 1992")
        time.sleep(7)
    elif "con" in text:
        speak("Con gái cưng của anh tên Nguyễn Ngọc Thiên Vân, sinh 01 tháng 06 năm 2019")
        time.sleep(7)
    elif "mẹ" in text:
        speak("mẹ anh tên Nguyễn Thị Chính, sinh ngày 10 tháng 05 năm 1957")
        time.sleep(7)
    elif "cha" in text:
        speak("cha anh tên Nguyễn Văn Chàng, sinh năm 1961")
        time.sleep(7)
    elif "Hoàng Anh" in text:
        speak("Cậu bé mập xấu xí")
        time.sleep(5)
######################################################################################
def play_song():
    speak('Xin mời anh chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát {} của anh đã được mở.".format(mysong))
    time.sleep(3)
#########################################################################################
def bach_khoa_toan_thu():
    try:
        speak("anh muốn biết về gì ạ?")
        time.sleep(3)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        time.sleep(20)
        for content in contents[1:]:
            speak("anh có muốn nghe thêm không?")
            time.sleep(3)
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(3)
        speak('Cảm ơn anh đã lắng nghe nhé!!!')
        time.sleep(3)
    except:
        speak("Xin lỗi em không hiểu. Xin anh hãy nói lại ạ")
        time.sleep(4)
##########################################################################################
def introduce():
    speak("""Xin chào. Rất hân hạnh được phục vụ anh. Em là trợ lý của anh nè Lâm.  
             Em sinh ra vào ngày 28/08/2021 và được sáng lập bởi Nguyễn Văn Lâm.""")
    time.sleep(15)
##########################################################################################
def help_me():
    hm = open('helpme.txt', 'r', encoding='UTF-8')
    hm1 = hm.read()
    speak(hm1)
    time.sleep(25)
###########################################################################################
def profile_leona(text):
    if "Tên của em" in text:
        ho_va_ten_AI = ["Em là trợ lý của anh Lâm",
                    "Em tên là Leona nhé"]
        speak(choice(ho_va_ten_AI))
        time.sleep(4)
    elif "Xuất xứ" in text or "xuất xứ" in text:
        que_huong_noi = ["Em được sinh ra và lớn lên tại Việt Nam nè", 
                     "Em từ khi sinh ra đã ở trong tim anh rồi HiHi", 
                     "Em sinh ra ở trong tim anh nè"]
        speak(choice(que_huong_noi))
        time.sleep(3)
    elif "tuổi của em" in text:
        tuoi_tac_noi = ["Em chỉ mới được một ngày tuổi thôi, em vẫn còn bé lắm", 
                    "Từ lúc sinh ra đến nay em chỉ mới đươc vài ngày tuổi thôi à", 
                    "Em ra đời từ năm 2021, em còn khá trẻ, nhưng em biết khá nhiều điều đó"]
        speak(choice(tuoi_tac_noi))
        time.sleep(6)
    elif "người yêu" in text:
        nguoi_yeu_noi = ["em làm gì đã có người yêu, em còn đang sợ ế đây này",
                     "em vẫn còn bé lắm",
                     "người yêu của tôi chính là anh đấy, Lâm ơi"]
        speak(choice(nguoi_yeu_noi))
        time.sleep(4)
    elif "ai tạo" in text:
        speak("Em được tạo ra bởi Nguyễn Văn Lâm nè")
        time.sleep(3)
##############################################################################################
def Ke_chuyen_AI(name):
    tc = open('truyencuoi.txt', 'r', encoding='UTF-8')
    tc1 = tc.readlines()
    speak(choice(tc1))
    time.sleep(28)    
    speak('Em cảm ơn anh đã lắng nghe!!!')
    time.sleep(3) 
    for chuyen_chay in tc1[1:]:
        nghe_tiep = "Anh có muốn nghe thêm không?"
        speak(nghe_tiep)
        time.sleep(5)
        chuyen_chay = get_text()
        if "có" in chuyen_chay or "nghe" in chuyen_chay or "tiếp đi em" in chuyen_chay:
            speak(choice(tc1))
            time.sleep(28)
            speak('Em cảm ơn anh đã lắng nghe!!!')
            time.sleep(3)
        else:
            break 
##################################################################################        

def assistant():
    loi_chao_AI="Em có thể gọi anh là gì nhỉ?"
    speak(loi_chao_AI)
    time.sleep(2)
    name = get_text()
    if name:
        ho_ten = "Chào anh {}, em có thể giúp gì cho anh ạ?".format(name)
        speak(ho_ten)
        time.sleep(3)

        while True: 
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào leona" in text or "bye" in text or "cút" in text or "đi đây" in text or "Stop" in text or "gặp lại sau" in text or "ngủ thôi" in text:
                stop()
                break            
            elif "có thể làm" in text or "hướng dẫn" in text or "sử dụng" in text or "biết làm" in text or "làm được gì" in text or "làm được những gì" in text:
                help_me()
            elif "chào" in text or "Xin chào" in text or "chào buổi sáng" in text or "chào buổi chiều" in text or "chào buổi trưa" in text or "chào buổi tối" in text:
                hello(name)
            elif "đọc văn bản" in text:
                doc_van_ban()
            elif "giờ" in text or "ngày" in text or "tháng" in text or "năm" in text or "thứ mấy" in text:
                get_time(text)
            elif "profile" in text or "bản thân" in text:
                speak("Anh muốn biết về cái gì nè")
                time.sleep(5)
                text3 = get_text()
                profile_me(text3) 
            elif "ứng dụng" in text or "app" in text:
                speak("Tên ứng dụng anh {} muốn mở là gì? ".format(name))
                time.sleep(3)
                text1 = get_text()
                open_application(text1)
            elif "web" in text or "website" in text:
                speak("Tên trang web anh muốn mở là gì")
                time.sleep(3)
                text2 = get_text()
                open_website(text2)
            elif "chơi nhạc" in text or "mở nhạc" in text or "nghe nhạc" in text:
                play_song()
            elif "định nghĩa" in text or "tìm kiếm" in text or "giải thích" in text or "hỏi" in text:
                bach_khoa_toan_thu()
            elif "giới thiệu" in text:
                introduce()
            elif "leona" in text or "trợ lý ảo" in text:
                speak("anh muốn biết gì về em")
                time.sleep(4)
                text4 = get_text()
                profile_leona(text4)
            elif "tạo" in text or "làm ra" in text or "thiết kế" in text or "sáng tác" in text:
                sang_tao_AI()
            elif "người yêu" in text:
                nguoi_yeu_AI()
            elif "tên tôi" in text or "tên anh" in text or "tôi tên" in text or "tao tên" in text or "tên của tôi" in text or "biết tên" in text or "tên của tao" in text:
                ten_ban(name)
            elif "chán" in text or "buồn" in text or "mệt" in text or "nản" in text or "nhọc" in text:
                Chan_qua_AI()
            elif "kể" in text or "truyện"  in text or "kể chuyện" in text or "kể truyện" in text:
                Ke_chuyen_AI(name)
            elif "tắt máy" in text:
                os.system("shutdown /s /t 1")
            else:
                noi_ii = ["Xin lỗi, em không hiểu anh {} muốn nói gì?".format(name),
                          "Anh {} muốn nói gì?, em không hiểu".format(name),
                          "Em còn khá kém em chưa thể hiểu thuật ngữ anh {} vừa nói là gì".format(name)]
                speak(choice(noi_ii))
                time.sleep(5)

assistant()            