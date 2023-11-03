# Quiz_API

### Описание
Благодаря этому проекту можно запрашивать англоязычные вопросы для викторин.
### Технологии
- Python 3.11
- Django 4.2.7
- DRF
- PostgreSQL
- Docker

### Запуск проекта
- Клонируйте проект
```
git clone https://github.com/NikLukyan/Quiz_API.git
``` 
- Из директории Quiz_API выполните команды для запуска контейнеров, выполнения миграций и сбора статики:
```
docker-compose up -d --build
```
```
docker-compose exec web python manage.py migrate
```
```
docker-compose exec web python manage.py collectstatic --no-input
```
- Теперь проект доступен по адресу http://localhost/
- В сервисе реализовано REST API, принимающее на вход 
POST запросы на эндпоинте  http://localhost/api/ с содержимым вида {"questions_num": integer}  ;

- После получения запроса сервис, в свою очередь, 
запрашивает с публичного API (англоязычные вопросы для викторин) 
https://jservice.io/api/random?count=1 указанное в полученном 
запросе количество вопросов.
- Далее сохраняется в базе данных следующая информация:
 1. ID вопроса
2. Текст вопроса
3. Текст ответа
4. Дата создания вопроса. 
- В случае, если в БД имеется такой же вопрос, к публичному API 
с викторинами выполняются дополнительные запросы до тех пор, 
пока не будет получен уникальный вопрос для викторины.
- Ответом на POST запрос является предыдущий сохранённый вопрос для викторины. 
В случае его отсутствия - пустой объект.
### Пример запроса
- На эндпоинт http://localhost/api/ отправим следующий POST запрос:
```
{
    "questions_num":2
}
```
В результате в БД сохранится 2 вопроса для викторины и в ответе
вернется последний добавленный в БД вопрос.
### Авторы
Никита Лукьянчук