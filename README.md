# Notes
RESTful API сервис работы с заметками
## Зависимости
Для запуска проекта небходимы open-source библиотеки, указанные в файле requirements.txt:
```text
Django==3.1.7
djangorestframework==3.12.2
drf-yasg==1.20.0
``` 
Для установки библиотек необходимо в корневом каталоге выполнить команду
```shell script
pip install -r requirements.txt
```
## Запуск проекта
Для запуска необходимо в корневом каталоге выполнить команду 
```shell script
python manage.py runserver
```
Запущенный сервис будет доступен по адресу http://127.0.0.1:8000
## Документация
Документация в формате Swagger доступна по адресу http://127.0.0.1:8000/swagger/
