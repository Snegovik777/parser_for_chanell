# -*- coding: utf-8 -*-
import requests
import datetime  # импорт обязательно с подчеркиванием
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import telebot
import urllib.request
import pytube
from pytube import YouTube


class VestiBot():

    def __init__(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Firefox(executable_path='C:\\webdriver\\geckodriver.exe')  # options=options
        self.time33 = ""
        self.time22 = ""
        self.time54 = ""
        self.time54_2 = ""
        self.time24_kras = ""
        self.time24_kras_2 = ""
        self.news_brn = ""
        self.news_nsk = ""
        self.news_kras = ""
        self.bot = telebot.TeleBot("1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM")

    def login_brn(self):
        browser = self.browser
        browser.get('https://vesti22.tv')
        time.sleep(random.randrange(2, 4))

    def login_nsk(self):
        browser = self.browser
        browser.get('https://www.nsktv.ru/news/')
        time.sleep(random.randrange(3, 6))

    def login_kras(self):
        browser = self.browser
        browser.get('http://www.vesti-krasnoyarsk.ru/news/')
        time.sleep(random.randrange(3, 6))

    def refresh_site(self):
        browser = self.browser
        time.sleep(random.randrange(390, 420))
        browser.refresh()

    def find_elem(self):
        browser = self.browser
        api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'

        # news_1 = browser.find_element_by_id("bx_651765591_25624").find_element_by_class_name("card-title").text
        # print(news_1)
        time.sleep(random.randrange(3, 6))
        divs = browser.find_elements_by_class_name("card-title")
        for div in divs:
            print(div.text)

        # кидаем в ТЕЛЕГУ уведомление через бота @BoomBarashka_Bot
        # requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        #     chat_id='-1001335233908',
        #     text=news_1
        # ))
        # requests.get('https://api.telegram.org/bot{}/sendPhoto'.format(api_token), params=dict(
        #     chat_id='-1001335233908',
        #     photo=src
        #     caption=glav_news
        # ))

    def find_links(self):  # метод собирает линки со списка ЛЕНТА (сейчас не используется)
        browser = self.browser
        links = browser.find_elements_by_class_name("news-feed__item")
        for link in links:
            pro_url = link.get_attribute("href")
            with open("links.txt", "a") as file:
                pro_url_2 = pro_url + "\n"
                file.write(pro_url_2)
            print(pro_url)

    def image_down_brn(self):  # метод находит ссылку на картинку новости и по ней скачивает иображение.
        browser = self.browser
        bot = self.bot
        time.sleep(random.randrange(3, 5))
        img = browser.find_element_by_class_name("post-page__preview")  # ДЕЛАЕМ СКРИН этого целого КЛАССА
        img2 = img.screenshot("C:\\untitled\\parser_for_chanell\\image_name_22.png")  # записываем в файл
        file = r"C:\untitled\parser_for_chanell\image_name_22.png"
        bot.send_photo(chat_id='-1001335233908', photo=open(file, 'rb'), caption=self.news_brn)

    def save_video_from_youtube_brn(self):  #  метод сохраняет видео с YOUTUBE
        browser = self.browser
        bot = self.bot
        try:
            video = browser.find_element_by_class_name("post-page__video js_video_block").find_element_by_tag_name("iframe")
        except:
            video = browser.find_element_by_tag_name("iframe")
        video_url = video.get_attribute('src')
        print("ссылка на видео:   ", video_url)
        youtube_video_url = video_url
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        # download the highest quality video
        filters.get_highest_resolution().download(filename='yt_video.mp4')
        print('Видео со страницы новости успешно загружено')
        time.sleep(random.randrange(2, 4))
        file = r"C:\untitled\parser_for_chanell\yt_videomp4.mp4"
        try:
            bot.send_video(chat_id='-1001335233908', data=open(file, 'rb'), caption=self.news_brn)
        except:
            print("Не отправил видео. Ошибка в ТЕЛЕБОТ")

    def find_link_1(self):  # метод находит первую ссылку в ЛЕНТЕ и делает по ней переход
        browser = self.browser
        bot = self.bot
        time.sleep(random.randrange(3, 6))
        links = browser.find_elements_by_class_name("news-feed__item")
        pro_url = links[0].get_attribute("href")  # ссылка на новость для КОПИРАЙТА

        # self.time22 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/a[1]/div/div[1]").text  # время выхода новости
        self.time33 = self.time22

        browser.find_element_by_class_name("mCSB_container").find_element_by_tag_name("a").click()
        time.sleep(random.randrange(3, 5))

        try:
            h1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/h1").text  # заголовок новости
        except:
            h1 = browser.find_element_by_class_name("mt-2 mb-3").text
        finally:
            print("Заголовок новости")

        buba = ""
        try:
            texta_1 = browser.find_element_by_class_name("post-page__text").find_elements_by_tag_name("p")
            for news_text in texta_1:  # печатет текст новости из всех тегов <p>
                buba1 = news_text.text
                buba = buba + buba1 + "\n"
            delta = len(buba)
            if delta > 750:
                buba = buba[:750] + "..."
        except:
            texta_1 = browser.find_element_by_class_name("post-page__info").text
            buba = texta_1
        else:
            print("Не спарсил подпись к картинке.")

        # for news_text in texta_1:  # печатет текст новости из всех тегов <p>
        #     buba1 = news_text.text
        #     buba = buba + buba1 + "\n"
        # delta = len(buba)
        # if delta > 750:
        #     buba = buba[:750] + "..."

        glav_news = h1 + "\n" + "\n" + buba + "\n" + "\n" + pro_url  # итоговая переменная с новостью
        print(glav_news)  # итоговая переменная с новостью
        self.news_brn = glav_news
        try:
            self.save_video_from_youtube_brn()  # пробует отправить видео
        except:
            self.image_down_brn()  # метод находит ссылку на картинку новости и по ней скачивает иображение.
        time.sleep(random.randrange(2, 4))
        # api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'
        # requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        #     chat_id='-1001335233908',
        #     text=glav_news
        # ))

    def image_down_nsk(self):  # метод находит ссылку на картинку новости и по ней скачивает иображение.
        browser = self.browser
        bot = self.bot
        time.sleep(random.randrange(4, 6))
        img = browser.find_element_by_class_name("media-block")  # ДЕЛАЕМ СКРИН этого целого КЛАССА
        img2 = img.screenshot("C:\\untitled\\parser_for_chanell\\image_name_54.png")  # записываем в файл
        file = r"C:\untitled\parser_for_chanell\image_name_54.png"
        bot.send_photo(chat_id='-1001335233908', photo=open(file, 'rb'), caption=self.news_nsk)

    def save_video_from_youtube_nsk(self):  #  метод сохраняет видео с YOUTUBE
        browser = self.browser
        bot = self.bot
        try:
            video = browser.find_element_by_class_name("yt-player-block").find_element_by_tag_name("iframe")
        except:
            video = browser.find_element_by_tag_name("iframe")
        video_url = video.get_attribute('src')
        print("ссылка на видео:   ", video_url)
        youtube_video_url = video_url
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        # download the highest quality video
        filters.get_highest_resolution().download(filename='yt_video.mp4')
        print('Видео со страницы новости успешно загружено')
        time.sleep(random.randrange(2, 4))
        file = r"C:\untitled\parser_for_chanell\yt_videomp4.mp4"
        try:
            bot.send_video(chat_id='-1001335233908', data=open(file, 'rb'), caption=self.news_nsk)
        except:
            print("Не отправил видео. Ошибка в ТЕЛЕБОТ")

    def find_link_1_nsk(self):  # метод находит первую ссылку в ЛЕНТЕ НОВОСИБИРСК и делает по ней переход
        browser = self.browser
        bot = self.bot
        time.sleep(random.randrange(3, 6))
        links = browser.find_elements_by_class_name("news_block")
        pro_url = links[0].get_attribute("href")  # ссылка на новость для КОПИРАЙТА

        # self.time22 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/a[1]/div/div[1]").text  # время выхода новости
        self.time54_2 = self.time54

        try:
            browser.find_element_by_xpath("/html/body/section/div[2]/div[2]/ul/a[1]").click()
        except:
            browser.find_element_by_class_name("append_news_wrap").find_element_by_class_name("news-page-list date-filter").find_element_by_tag_name("a").click()
        time.sleep(random.randrange(3, 5))

        try:
            h1 = browser.find_element_by_xpath("/html/body/section/div[2]/h1").text  # заголовок новости
        except:
            h1 = browser.find_element_by_tag_name("h1").text
        finally:
            print("Заголовок новости")

        buba = ""
        texta_1 = ""

        try:
            texta_1 = browser.find_element_by_class_name("block2__wrap__text").find_elements_by_tag_name("p")
        except:
            print("Текст новости.")
        texta_2 = browser.find_element_by_class_name("block2__wrap__text").text
        print("texta_2 до обрезания:", texta_2)
        delta = len(texta_2)
        if delta > 750:
            texta_2 = texta_2[:750] + '...'
            print("После обрезания:", texta_2)
        if not texta_1:
            buba = texta_2 + "\n"
        else:
            for news_text in texta_1:  # печатает текст новости из всех тегов <p>
                buba1 = news_text.text
                buba = buba + buba1 + "\n" + "\n"
            delta2 = len(buba)
            if delta2 > 750:
                buba = buba[:750] + "..."
        glav_news = h1 + "\n" + "\n" + buba + "\n" + pro_url  # итоговая переменная с новостью
        print(glav_news)  # итоговая переменная с новостью
        self.news_nsk = glav_news
        try:
            self.save_video_from_youtube_nsk()
        except:
            self.image_down_nsk()  # если нет видео, метод находит ссылку на картинку новости и по ней скачивает иображение.
        time.sleep(random.randrange(3, 7))

    def image_down_kras(self):  # метод находит ссылку на картинку новости и по ней скачивает иображение.
        browser = self.browser
        bot = self.bot
        time.sleep(random.randrange(3, 5))
        img = ""
        file = ""
        try:
            img = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/div/div[1]/div/article/div[1]/div[1]/iframe")  # ДЕЛАЕМ СКРИН этого целого КЛАССА
            img2 = img.screenshot("C:\\untitled\\parser_for_chanell\\image_name_24.png")  # записываем в файл
            file = r"C:\untitled\parser_for_chanell\image_name_24.png"
        except NoSuchElementException:
            print("По xpath не нашли картинку.")
        try:
            img = browser.find_element_by_class_name("video video--16x9")
            img2 = img.screenshot("C:\\untitled\\parser_for_chanell\\image_name_24.png")  # записываем в файл
            file = r"C:\untitled\parser_for_chanell\image_name_24.png"
        except:
            print("И по классу не нашли картинку.")

        # img2 = img.screenshot("C:\\untitled\\parser_for_chanell\\image_name_22.png")  # записываем в файл
        if not img:
            file = r"C:\untitled\parser_for_chanell\image_name_kras.png"
        else:
            file = r"C:\untitled\parser_for_chanell\image_name_24.png"

        bot.send_photo(chat_id='-1001335233908', photo=open(file, 'rb'), caption=self.news_kras)

    def save_video_from_youtube_kras(self):  #  метод сохраняет видео с YOUTUBE
        browser = self.browser
        bot = self.bot
        try:
            video = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/div/div[1]/div/article/div[1]/div[1]/iframe")
            print("нашли xpath")
        except Exception:
            video = browser.find_element_by_class_name("publication__desc text").find_element_by_tag_name("iframe")
            print("нашли класс")
        finally:
            print("Искал видео...")
        video_url = video.get_attribute('src')
        print("ссылка на видео:   ", video_url)
        youtube_video_url = video_url
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        # download the highest quality video
        filters.get_highest_resolution().download(filename='yt_video.mp4')
        print('Видео со страницы новости успешно загружено')
        time.sleep(random.randrange(2, 4))
        file = r"C:\untitled\parser_for_chanell\yt_videomp4.mp4"
        try:
            bot.send_video(chat_id='-1001335233908', data=open(file, 'rb'), caption=self.news_kras)
        except:
            print("Не отправил видео. Ошибка в ТЕЛЕБОТ.")

    def find_link_1_kras(self):  # метод находит первую ссылку в ЛЕНТЕ НОВОСИБИРСК и делает по ней переход
        browser = self.browser
        bot = self.bot
        time.sleep(random.randrange(3, 6))
        links = browser.find_elements_by_class_name("newsside__link")
        pro_url = links[0].get_attribute("href")  # ссылка на новость для КОПИРАЙТА

        # self.time22 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/a[1]/div/div[1]").text  # время выхода новости
        self.time24_kras_2 = self.time24_kras

        try:
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/div/div[2]/div[4]/div/div[1]/div[1]/a").click()
        except:
            browser.find_element_by_class_name("newsside__item").find_element_by_tag_name("a").click()
        time.sleep(random.randrange(3, 5))

        try:
            h1 = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/div/div[1]/div/article/h1").text  # заголовок новости
        except:
            h1 = browser.find_element_by_tag_name("h1").text
        finally:
            print("Заголовок новости")

        elem1 = browser.find_element_by_id("vgtrk-mini-player")  # закрываем окошко стрима Россия1
        browser.execute_script("arguments[0].setAttribute('style','display:none;');", elem1)
        time.sleep(random.randrange(2, 4))
        buba = ""
        try:
            texta_1 = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/div/div[1]/div/article/div[1]").find_elements_by_class_name("h-talign_justify")
        except:
            texta_1 = browser.find_element_by_class_name("publication__desc text").find_elements_by_class_name("h-talign_justify")
            print("Текст новости.333", texta_1)
        try:
            texta_2 = browser.find_element_by_class_name("publication__desc text").text
        except:
            texta_2 = h1
            print("texta_2 пустая. И будет как заголовок")
        print("texta_2 до обрезания:", texta_2)
        delta = len(texta_2)
        if delta > 750:
            texta_2 = texta_2[:750] + '...'
            print("После обрезания:", texta_2)
        if not texta_1:
            buba = texta_2 + "\n"
        else:
            for news_text in texta_1:  # печатает текст новости из всех тегов <p>
                buba1 = news_text.text
                buba = buba + buba1 + "\n" + "\n"
            delta2 = len(buba)
            if delta2 > 750:
                buba = buba[:750] + "..."
        glav_news = h1 + "\n" + "\n" + buba + "\n" + pro_url  # итоговая переменная с новостью
        print(glav_news)  # итоговая переменная с новостью
        self.news_kras = glav_news
        try:
            self.save_video_from_youtube_kras()
            print("Будет видео")
        except:
            self.image_down_kras()  # если нет видео, метод находит ссылку на картинку новости и по ней скачивает иображение
            print("Будет картинка")
        time.sleep(random.randrange(3, 7))


my_bot = VestiBot()
my_bot.time33 = ""
my_bot.time54_2 = ""
my_bot.time24_kras_2 = ""
green = True
while green:
    time.sleep(random.randrange(3, 7))
    my_bot.login_brn()  # ==================  БАРНАУЛ  ==========================
    try:
        my_bot.time22 = my_bot.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/a[1]/div/div[1]").text  # время выхода новости
    except:
        print("Не спарсил время Барнаул.")
    if my_bot.time33 == my_bot.time22:
        print("Нет новостей в Барнауле")
        my_bot.refresh_site()
    else:
        my_bot.find_link_1()
        my_bot.login_brn()
    time.sleep(random.randrange(3, 5))

    my_bot.login_nsk()  # =====================  НОВОСИБИРСК  ==================================
    time.sleep(random.randrange(3, 5))
    try:
        my_bot.time54 = my_bot.browser.find_element_by_xpath("/html/body/section/div[2]/div[2]/ul/a[1]/div[1]/p[1]").text
    except:
        print("Не спарсил заголовок новости НСК")
    if my_bot.time54_2 == my_bot.time54:
        print("В НСК нет новостей")
        my_bot.refresh_site()
    else:
        my_bot.find_link_1_nsk()
        my_bot.login_nsk()
    time.sleep(random.randrange(3, 5))

    my_bot.login_kras()  # =====================  КРАСНОЯРСК  ==================================
    time.sleep(random.randrange(3, 5))
    try:
        my_bot.time24_kras = my_bot.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/main/div/div/div[2]/div[4]/div/div[1]/div[1]/a").text
    except:
        print("Не спарсил заголовок новости КРАС")
    if my_bot.time24_kras_2 == my_bot.time24_kras:
        print("В Красноярске нет новостей")
        my_bot.refresh_site()
    else:
        my_bot.find_link_1_kras()
        my_bot.login_kras()
    time.sleep(random.randrange(3, 5))

    if not green:
        break