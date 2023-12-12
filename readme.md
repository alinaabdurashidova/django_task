# Документация по проекту

## 1. Создание базы данных

Для этого необходимо зайти через терминал в PostgreSql и создать базу данных по следующей команде:

```
CREATE DATABASE <Наименование базы данных>
```

(в данном проекте название БД - django_task)


## 2. Активация виртуального окружения

Виртуальное окружение создается в папке, где будет реализован проект. Далее необходимо набрать команды на терминале для создания и активации:

```
python3 -m venv venv

. venv/bin/activate
```


## 3. Установка расширений

Для установки сразу нескольких расширений создается текстовый файл **requirements.txt** и все их наименования прописываются в данном файле. Далее через терминал производится их установка по команде:

```
pip install -r requirements.txt
```

## 4. Создание самого проекта

На терминале необходимо прописать следующую команду:

```
django-admin startproject config . 
```

После чего в папке нашего будет создан проект **config** со встроенными папками и файлами


## 5. Создания приложений ***Author*** и ***Book***

Для создания новых приложений необходимо написать на терминале следующие команды:

```
python3 manage.py startapp Author
python3 manage.py startapp Book
```
## 6. Создание моделей для каждого приложения

Создание моделя для приложения **Author** в файле models.py (Author/models.py):

```python
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length = 40)
    born_on = models.DateField()
    psevdonim = models.CharField(max_length = 40)
    
    def __str__(self) -> str:
        return self.name
```


Создание моделя для приложения **Book** в файле models.py (Book/models.py):

```python
from django.db import models
from Author.models import Author
class Book(models.Model):
    title = models.CharField(max_length = 40)
    created_at = models.DateField()
    genre = models.CharField(max_length = 40)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='books'
    )
    
    def __str__(self) -> str:
        return self.title

```

## 7. Загрузка приложений в файле settings.py

В данном файле необходимо добавить наши приложения в раздел **INSTALLED_APPS**:
```python
INSTALLED_APPS = [
    ...
    'Author',
    'Book'
]
```

## 8. Миграции

Миграция является способом отслеживания изменений в структуре базы данных. В терминале необходимо будет прописать следующие команды:

```
python manage.py makemigrations
python manage.py migrate
```

## 9. Выполнение CRUD

Необходимо прописать в терминале следующую команду:

```
python manage.py shell
```
таким образом мы запускаем интерактивную консоль, где будет прописываться CRUD функционал.


В первую очередь будет производится импорт моделей:

```
>>>from Author.models import Author
>>>from Book.models import Book
```

***Create:***

Для создания данных в Author:

```
Author.objects.create(name = '<имя автора>', born_on = '<дата рождения>', psevdonim = '<псевдоним>')
```

Для создания данных в Book:
```
Book.objects.create(title = '<наименование произведения>', created_at = '<дата выпуска>', genre = '<жанр>', author = <автор>)
```

***Read:***

Для вывода всех данных необходимо прописать следующее:
```
Author.objects.all()
Book.objects.all()
```
(* в моем проекте для Author будут возвращатся только имена авторов, для Book только наименование произведений, так как так было прописано в коде)

Для вывода по определенному значению (retrieve) необходимо написать следующую команду:

```
Author.objects.get(field = '<значение поля>')
Book.objects.get(field = '<значение поля>')
```

***Update:***

Для обновления можете написать следующие команды:

```
author = Author.objects.get(field='<значение поля>')
author.field = '<новое значение>'
author.save()

book = Book.objects.get(field='<значение поля>')
book.field = '<новое значение>'
book.save()
```

где field поле, значение которого хотите обновить

Можно также произвести обновление по команде:

Book.objects.filter(field = '<значение поля>').update(firld = '<новое значение>') 

***Delete:***

Удалить данные можете по следующим командам:
```
author = Book.objects.get(field = '<значение поля>')
author.delete()
```
```
book = Book.objects.get(field = '<значение поля>')
book.delete()
```

##### Более подробные действия можете посмотреть в файле zametki.txt