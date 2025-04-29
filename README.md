# RoadSafe_Moscow 🚦

**RoadSafe_Moscow** — это интерактивное веб-приложение на Django, предназначенное для мониторинга дорожно-транспортных происшествий (ДТП) по Москве, анализа маршрутов и визуализации опасных участков на карте.

![изображение](https://github.com/user-attachments/assets/2aeb09b7-709a-4a16-be55-2cde14e49753)


---

## ⚙️ Возможности проекта

- Добавление и отображение ДТП с указанием местоположения и типа.
- Система фильтрации аварий по степени тяжести.
- Построение условного маршрута между точками с отображением прямой линии.
- Авторизация, регистрация, личный кабинет.
- Удобный интерфейс на Bootstrap с JS.
- Локальные изображения и иконки.
- Интерактивная карта (Яндекс Карты).

---

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/alolaalola/RoadSafe.git
cd RoadSafe

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

База данных MySQL 8.0.42 
mysql -u root -p roadsafe_moscow < db_backup.sql

python manage.py makemigrations
python manage.py migrate

Запустите сервер
python manage.py runserver


