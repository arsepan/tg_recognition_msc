from YandexImagesParser.ImageParser import YandexImage
import requests

parser = YandexImage()
counter = 0

additional_words = ['', 'ночью', 'утром', 'днём', 'вечером',
                    'в пасмурную погоду', 'в дождь',
                    'башни', 'внутри', 'снаружи', 'с людьми', 'фото с телефона', 'на снимке с телефона',
                    'летом', 'зимой', 'осенью', 'весной']

for additional_word in additional_words:
    print(additional_word)
    for item in parser.search('Московский кремль' + ' ' + additional_word):
        counter += 1
        print(counter)
        try:
            img = requests.get(item.url)
            img_option = open('C:/Users/Legion 5/Desktop/Учёба/Стажки/Портфолио/Телеграмм бот для распознования Московских достопремичательностей/data/train/Московский кремль' + '/' + str(counter) + '.jpg', 'wb')
            img_option.write(img.content)
            img_option.close()
        except:
            pass