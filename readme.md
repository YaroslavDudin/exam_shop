# 1 этап Быстрый старт
Создать виртуальное окружение

```bash
python -m venv venv
```
Активировать виртуальное окружение


## Windows
```bash
venv\Scripts\activate
```

Обновить pip

```bash
python.exe -m pip install --upgrade pip
```
Установить зависимости

```bash
pip install django openpyxl Pillow
```
Создать Django проект

```bash
django-admin startproject config .
```
Создать приложение products

```bash
python manage.py startapp products
python manage.py startapp orders
python manage.py startapp users 
```