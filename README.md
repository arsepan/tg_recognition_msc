### Описание проекта

Идеей было создать простой кейс, который поможет туристам быстрее и эффективнее узнавать культурные объекты Москвы. Сейчас большинство людей сидят в telegram, поэтому я решил создать бота с нейросетью. Мною была выбрана уже готовая модель из зоопарка керас - ResNet50.
Данный telegram bot умеет распозновать 12 достопремечательностей Москвы с точностью 96% на тестовых и 98% на валидационных данных:
- Большой театр
- ГУМ
- Государственный исторический музей
- Дом Пашкова
- Здание мэрии Москвы (бывший дом генерал-губернатора)
- Иверские (Воскресенские) ворота
- Мавзолей В. И. Ленина
- Московский Кремль
- Никольская улица
- Собор Казанской иконы Божией Матери на Красной площади
- Храм Василия Блаженного
- ЦУМ

Для сбора данных были созданы два парсера:
1. По поисковой выдаче Google - однако он сгодился лишь для тестовых данных, тк не обладал полной мощностью для скачки даже 100 изображений. Однако поисковая выдача гугла и яндекса очень разнилась, поэтому для теста я решил применить именно его;
2. По поисковой выдаче Яндекса.

### Пути развития
Не судите строго за красоту представления. Первая версия скорее просто показ возможностей и работоспособности. В мыслях очень много путей развития и вот некоторые из них:
0. Нулевое, тк самое очивидное - расширить возможности;
1. На данном этапе бот берёт информацию из dict, она весьма краткая. Основная задумка в том, чтобы человек смог узнать тот максимум, который ему необходим, поэтому нужно подключить GPT;
2. Нужно учесть, что не всегда пользователю удобно задавать вопросы в текстовом виде, поэтому можно создать голосовой обработчки, который в дальнейшем будет переправлять текст в GPT;
3. Также не всегда удобно читать присланную информацию, нужно сделать "Аудио-гид", который будет переводить текст созданный GPT в голосовое сообщение.
