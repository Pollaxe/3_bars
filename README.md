# Ближайшие бары

Программа для вывода самого большого, маленького и ближайшего бара в Москве.


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py <Имя файла> # возможно вам потребуется написать python3, а не просто python.

```

Запуск на Windows происходит аналогично.

Файл для примера можно взять с сайта [Devman.org](https://devman.org/fshare/1503831681/4/)

# Пример вывода
```
> Самый большой бар в Москве: Спорт бар «Красная машина»
> Самый маленький бар в Москве: БАР. СОКИ
> Введите вашу широту:55
> Введите вашу долготу:55
> Самый ближайший к вам бар: Таверна
```
# Функции

```python
load_data(file_path) # Загружает данные из файла.
```

```python
get_biggest_bar(bars) # Выдает крупнейший бар.
```

```python
get_smallest_bar(bars) # Выдает самый маленький бар.
```

```python
get_closest_bar(bars, latitude, longitude) # Выдает ближайший бар.
```
```python
print_closest_bar(bars) # - Печатает в консоль ближайший бар.
```
```python
print_smallest_and_biggest_bar(bars) # - Печатает в консоль самый маленький и самый большой бар.
```

# Пример использования

```python
import json
import bars
bars_json = bars.load_data('bars.json')
bars_json = bars_json['features']
print(bars.get_closest_bar(bars_json, 33, 55))
```
Вывод будет:
```
> {'geometry': {'coordinates': [36.900000000253, 55.303299999814], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'bb9eb30d-d16b-4821-8d9c-894b581ac762', 'Attributes': {'global_id': 281494712, 'Name': 'Staropramen', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Центральный административный округ', 'District': 'Красносельский район', 'Address': 'Садовая-Спасская улица, дом 19, корпус 1', 'PublicPhone': [{'PublicPhone': '(985) 069-34-47'}], 'SeatsCount': 50, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
