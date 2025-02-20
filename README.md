# Установка 
## Как развернуть проект на локальной машине 
### Клонировать репозиторий и перейти в него в командной строке 
``` 
  git clone https://github.com/N0len-sasha/reservation_service.git
``` 
``` 
  cd reservation_service
``` 

### Установить зависимости 
``` 
  pip install poetry 
``` 
``` 
  poetry install
``` 
### Выполнить миграции
```
  cd Reservation_service_API
```
``` 
  python manage.py migrate 
```
 
### Запустить проект 
``` 
  python manage.py runserver 
``` 

# Основные запросы
## Rooms
### ```GET http://127.0.0.1:8000/api/rooms/```
```
  {
        "id": 1,
        "price": 1000.0,
        "description": "Номер отеля 1",
        "create_date": "2025-02-18",
        "bookings": [
            {
                "id": 1,
                "date_start": "2002-02-02",
                "date_end": "2002-04-02",
                "hotel_id": 1
            }
        ]
    },
```
### ```POST http://127.0.0.1:8000/api/rooms/```
### Тело запроса
```
{
    "price": 1500,
    "description": "Номер отеля 6"
}
```
### Ответ
```
{
    "id": 5
}
```
### ```GET http://127.0.0.1:8000/api/rooms/1/```
```{
    "id": 1,
    "price": 1000.0,
    "description": "Номер отеля 1",
    "create_date": "2025-02-18"
}
```
### ```GET http://127.0.0.1:8000/api/rooms/?ordering=price (сортировка по цене)```
### ```GET http://127.0.0.1:8000/api/rooms/?ordering=-price (обратная сортировка по цене)```
### ```GET http://127.0.0.1:8000/api/rooms/?ordering=date_start (сортировка по времени)```
### ```GET http://127.0.0.1:8000/api/rooms/?ordering=-date_start (обратная сортировка по времени)```
### ```DELETE http://127.0.0.1:8000/api/rooms/1/ удаление записи по id=1```

## Rooms

### ```GET http://127.0.0.1:8000/api/bookings/```
```
    {
        "id": 4,
        "date_start": "2000-01-01",
        "date_end": "2000-01-02",
        "hotel_id": 2
    },
    {
        "id": 1,
        "date_start": "2002-02-02",
        "date_end": "2002-04-02",
        "hotel_id": 1
    },
```
### ```GET http://127.0.0.1:8000/api/bookings/1/```
```
{
    "id": 1,
    "date_start": "2002-02-02",
    "date_end": "2002-04-02",
    "hotel_id": 1
}
```
### ```POST http://127.0.0.1:8000/api/bookings/```
### Тело запроса
```
{
    "date_start": "2000-01-01",
    "date_end": "2000-01-02",
    "hotel_id": 3
}
```
### Ответ
```
{
    "id": 5
}
```
### ```DELETE http://127.0.0.1:8000/api/bookings/2/ (удаление записи по id=2)```

## Автор 
Платошин Александр Игоревич 
