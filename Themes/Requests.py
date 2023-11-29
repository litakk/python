# Что такое запросы
# Requests — это библиотека с открытым исходным кодом , которая упрощает процесс создания (отправки и получения) 
# HTTP-запросов с помощью Python.

# Он очень прост в использовании и красиво спроектирован, что избавляет нас от скучных, утомительных и болезненных
# процессов, необходимых при выполнении HTTP-запросов.

# Запросы: HTTP для людей™

# Запросы используются для отправки и получения данных через Интернет, будь то веб-сайт, API или другой доступный
# в Интернете ресурс и обратно.

# Это незаменимый инструмент в наборе инструментов программиста или специалиста по обработке данных.
# Если вашему приложению необходимо очищать Интернет, искать курсы валют, получать информацию о погоде, 
# извлекать данные из API, передавать данные в API или загружать файлы, запросы — это то, что вам нужно!


import requests

url = 'https://example.com'
r = requests.get(url)