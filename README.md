Декоратор, который отлавливает редактируемые поля.

Полезно, если требуются дополнительные действия при изменении определенных полей

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

## Database dump/load
```sh
$ python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --indent 4 > default_data.json

$ python manage.py loaddata default_data.json
```
