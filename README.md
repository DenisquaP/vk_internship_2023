# Django-сервис друзей
***
Оглавление
* [Как запустить сервис](#Запуск-сервиса)
* [Какие есть endpoints](#Endpoints)

***
# Запуск сервиса
_Перед запуском убедитесь, что порт 8000 не используется на вашем компьютере._

Запустить сервис можно с помощью:
* Терминала (В случае использования Linux заменить python на python3)
```
pip install -r requirements.txt
cd vk_internship
python manage.py makemigrations friends
python manage.py migrate
python manage.py runserver
```
* Docker-контейнера

Для Linux 
```
sudo docker compose -f docker-compose.yaml up -d
```
Для Windows 
```
docker compose -f docker-compose.yaml up -d
```
# Endpoints

| Endpoint                     | Что делает                                   |
|--------------------------|----------------------------------------------|
| __GET__ users/                         | Получить список пользователей|
| __POST__ users/                         | Создать пользователя | 
| __GET__ users/{user_id}/           | Получить пользователя                |
| __GET__ users/{user_id}/friends/requests/{type_of}   | Получить исходящие/входящие запросы дружбы  |
| __DELETE__ users/{user_id}/friends/{friend_id}/delete/   | Удалить из друзей пользователя  | 
| __GET__ users/{user_id}/friends/{friend_id}/status/   | Посмотреть статус дружбы | 
| __POST__ users/{user_id}/friends/{friend_id}/send_request/   | Отправить запрос дружбы |
| __POST__ users/{user_id}/friends/{friend_id}/answer_request/{type_of}/   | Ответить на запрос дружбы |

