
def image_down_nsk(self):  # метод находит ссылку на картинку новости и по ней скачивает иображение.
    # get the image source
    browser = self.browser
    time.sleep(random.randrange(3, 5))
    img = browser.find_element_by_class_name("post-page__preview")
    src = img.get_attribute('style')
    print('Это еще атрибут:', src)
    src = src.rstrip('\");')
    src = src.lstrip('background-image: url("')
    print('Это еще часть ссылки на картинку:', src)
    src = 'https://vesti22.tv' + src
    print('Это должен быть уже готовый адрес:', src)
    # download the image
    img_data = requests.get(src).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'
    requests.get('https://api.telegram.org/bot{}/sendPhoto'.format(api_token), params=dict(
        chat_id='-1001335233908',
        photo=src
    ))

    def find_link_1_nsk(self):  # метод находит первую ссылку в ЛЕНТЕ и делает по ней переход
        browser = self.browser
        time.sleep(random.randrange(3, 6))
        links = browser.find_elements_by_class_name("news-feed__item")
        pro_url = links[0].get_attribute("href")  # ссылка на новость для КОПИРАЙТА

        # self.time22 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/a[1]/div/div[1]").text  # время выхода новости
        self.time33 = self.time22

        browser.find_element_by_class_name("mCSB_container").find_element_by_tag_name("a").click()
        time.sleep(random.randrange(3, 5))

        self.image_down()  # метод находит ссылку на картинку новости и по ней скачивает иображение.

        try:
            h1 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/h1").text  # заголовок новости
        except:
            h1 = browser.find_element_by_class_name("mt-2 mb-3").text
        finally:
            print("Новость без зоголовка")

        buba = ""
        texta_1 = ""
        try:
            texta_1 = browser.find_element_by_class_name("post-page__text").find_elements_by_tag_name("p")
        except:
            print("Новость без текста.")
        for news_text in texta_1:  # печатет текст новости из всех тегов <p>
            buba1 = news_text.text
            buba = buba + buba1 + "\n"
#            print(pro_url)
        glav_news = self.time22 + "\n" + h1 + "\n" + buba + "\n" + pro_url  # итоговая переменная с новостью
        print(glav_news)  # итоговая переменная с новостью
        time.sleep(random.randrange(3, 7))
        api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
            chat_id='-1001335233908',
            text=glav_news
        ))
