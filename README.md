[![Actions Status](https://github.com/GoddessEyes/vacation_visualiser/workflows/vacation_visualiser%20build/badge.svg)](https://github.com/GoddessEyes/vacation_visualiser/actions)


# Vacation_Visualizer

#### Запуск "production" сборки

```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

__Команда для создания суперпользователя:__

```bash
docker-compose -f docker-compose.prod.yml exec app /usr/local/bin/python manage.py createsuperuser
```
