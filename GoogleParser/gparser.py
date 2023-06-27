from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/Legion 5/Desktop/Учёба/Стажки/Портфолио/Телеграмм бот для распознования Московских достопремичательностей/test/Иверские (Воскресенские) ворота'})

print('Введите запрос')
name = input()
print('Введите количество фотографий')
number = int(input())

crawler.crawl(keyword=name, max_num=number)