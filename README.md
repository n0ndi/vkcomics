# Публикация комиксов

Программа публикует комиксы с сайта [xkcd.com](https://xkcd.com/) и делает пост в сообществе сайта [vk.com](https://vk.com/) 

### Как установить

Для работы программы требуются данные с API [ВК](https://vk.com/), требуется создать [приложение](https://vk.com/dev/vk_how_to_start)


Получить личный ключ по ссылке:

```https://oauth.vk.com/authorize?client_id=ID ВАШЕГО ПРИЛОЖЕНИЯ&scope=photos,groups,wall,offline&display=page&response_type=token&v=5.131&state=123456```  

И вписать данные в фаил( ```.env``` ):



```
VK_ACCESS_TOKEN = личный ключ
VK_GROUP_ID = ID сообщества
VK_USER_ID = ID вашей страницы

```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Пример запуска
Запустите программу следуещей строкой:

```
python main.py
```

На стене группы появится новая запись.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).