# api_final 
## Описание проекта 
Проект API для социальной сети Yatube. Интерфейс, через которое могут работать  
мобильное приложение или чат-бот; через него же можно передавать  
данные в любое приложение или на фронтенд. 
 
## Стек технологий 
* Django Rest Framework   
* Python   
* Django 
* SQlite3 
   
##Доступные возможности: 
 
Подписка на пользователей. 
Создание, просмотр, изменение и удаление постов. 
Создание, просмотр, изменение и удаление комментариев. 
Создание и просмотр групп.  
 
Документация по проекту после запуска сервера доступна по адресу:   
http://127.0.0.1:8000/redoc/   
 
 
### Как запустить проект: 
 
Клонировать репозиторий и перейти в него в командной строке: 
 
``` 
git clone git@github.com:Melnik-ni/api_final_yatube.git 
``` 
 
``` 
cd api_final_yatube 
``` 
 
Cоздать и активировать виртуальное окружение: 
 
``` 
python -m venv env 
``` 
 
``` 
source venv/Scripts/activate 
``` 
 
Установить зависимости из файла requirements.txt: 
 
``` 
python -m pip install --upgrade pip 
``` 
 
``` 
pip install -r requirements.txt 
``` 
 
Выполнить миграции: 
 
``` 
python manage.py migrate 
``` 
 
Запустить проект: 
 
``` 
python manage.py runserver 
``` 
 
### Пример запроса к API 
 
GET запрос http://127.0.0.1:8000/api/v1/posts/{id}/   
Пример ожидаемого ответа:   
{ 
"id": 0, 
"author": "string", 
"text": "string", 
"pub_date": "2019-08-24T14:15:22Z", 
"image": "string", 
"group": 0 
} 
 
POST запрос http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/   
payload   
{   
"text": "string"   
}   
Пример ожидаемого ответа:   
{ 
"id": 0, 
"author": "string", 
"text": "string", 
"created": "2019-08-24T14:15:22Z", 
"post": 0 
} 
