# Ближайшие бары

Программа для вывода самого большого, маленького и ближайшего бара в Москве.


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <Имя файла> # possibly requires call of python3 executive instead of just python

```

Запуск на Windows происходит аналогично.

# Пример вывода

> Biggest bar in Moscow is Спорт бар «Красная машина»
> Smallest bar in Moscow is БАР. СОКИ
> Please input your latitude:55
> Please input your longitude:55
> Closest bar in Moscow to you is Таверна

# Функции

```python
load_data(file_path) # Загружает данные из файла.
```

```python
get_biggest_bar(json_decoded) # Выдает крупнейший бар.
```

```python
get_smallest_bar(json_decoded) # Выдает самый маленький бар.
```

```python
get_closest_bar(json_decoded, latitude, longitude) # Выдает ближайший бар.
```

# Пример использования

```python
import json
import bars
json_content = bars.load_data('bars.json')
json_decoded = json.loads(json_content)
json_decoded = json_decoded['features']
print(bars.get_closest_bar(json_decoded, 33, 55))
```
Вывод будет:
>{'geometry': {'coordinates': [36.900000000253, 55.303299999814], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'bb9eb30d-d16b-4821-8d9c-894b581ac762', 'Attributes': {'global_id': 281494712, 'Name': 'Staropramen', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Центральный административный округ', 'District': 'Красносельский район', 'Address': 'Садовая-Спасская улица, дом 19, корпус 1', 'PublicPhone': [{'PublicPhone': '(985) 069-34-47'}], 'SeatsCount': 50, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
