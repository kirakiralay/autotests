# QA Autotests

Автотесты для API тестирования сайта demoblaze.com

## Стек
- Python 3.14
- pytest
- requests

## Что тестируется

### test_login.py
- Авторизация с верными данными — проверка статус кода 200 и наличия токена
- Авторизация с неверным паролем — автотест воспроизводит баг TES-5 
  (сервер возвращает 200 вместо 401 Unauthorized)
- Получение списка товаров — проверка эндпоинта /entries

## Как запустить

```bash
pip install pytest requests
py -m pytest test_login.py -v
```

## Связанные репозитории
- [demoblaze-testing](https://github.com/kirakiralay/demoblaze-testing) — 
  ручное тестирование, баг-репорты, чек-листы
