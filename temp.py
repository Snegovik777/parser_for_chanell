img = browser.find_element_by_class_name("post-page__preview")
src = img.get_attribute('style')
print('Это еще атрибут:', src)
src = src.rstrip('\");')
src = src.lstrip('background-image: url("')
print('Это еще часть ссылки на картинку:', src)
src = 'https://vesti22.tv' + src
print('Это должен быть уже готовый адрес КАРТИНКИ:', src)
# download the image
img_data = requests.get(src).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)


==========


api_token = '1431354839:AAHc0xVFBva7VVZ0UzR39LlHTJY_UfyRazM'
requests.get('https://api.telegram.org/bot{}/sendPhoto'.format(api_token), params=dict(
    chat_id='-1001335233908',
    photo=src,
    caption=self.news_brn
))
