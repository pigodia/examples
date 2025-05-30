В Python встроенные функции — это функции, доступные сразу "из коробки", без необходимости их импорта из модулей. Они охватывают широкий спектр задач: работа с числами, последовательностями, логикой, типами, преобразованиями и др.

Вот **полный список всех встроенных функций Python (на май 2025)** с кратким описанием:

---

### 🔢 Работа с числами

| Функция                    | Описание                                 |
| -------------------------- | ---------------------------------------- |
| `abs(x)`                   | Абсолютное значение                      |
| `divmod(a, b)`             | Возвращает кортеж `(a // b, a % b)`      |
| `max()`                    | Максимум                                 |
| `min()`                    | Минимум                                  |
| `pow(x, y[, z])`           | Возведение в степень (с mod, если задан) |
| `round(number[, ndigits])` | Округление                               |
| `sum(iterable[, start])`   | Суммирование элементов                   |

---

### 🧪 Проверка типов и логика

| Функция                           | Описание                                             |
| --------------------------------- | ---------------------------------------------------- |
| `all(iterable)`                   | Возвращает `True`, если все элементы истинны         |
| `any(iterable)`                   | Возвращает `True`, если хотя бы один элемент истинен |
| `bool(x)`                         | Преобразует в логическое значение                    |
| `callable(x)`                     | Проверяет, вызываем ли объект                        |
| `isinstance(obj, type)`           | Проверяет, является ли объект экземпляром типа       |
| `issubclass(cls, class_or_tuple)` | Является ли класс подклассом                         |
| `type(obj)`                       | Возвращает тип объекта                               |

---

### 🔁 Итерации и коллекции

| Функция                        | Описание                      |
| ------------------------------ | ----------------------------- |
| `enumerate(iterable, start=0)` | Индексация элементов          |
| `filter(function, iterable)`   | Фильтрация по условию         |
| `map(function, iterable, ...)` | Применение функции            |
| `zip(*iterables)`              | Объединение в кортежи         |
| `reversed(seq)`                | Обратный итератор             |
| `len(s)`                       | Длина объекта                 |
| `sorted(iterable, ...)`        | Сортировка                    |
| `next(iterator[, default])`    | Получение следующего элемента |
| `iter(obj[, sentinel])`        | Получение итератора           |

---

### 📦 Работа с коллекциями и структурами данных

| Функция                                  | Описание               |
| ---------------------------------------- | ---------------------- |
| `list()`                                 | Создание списка        |
| `tuple()`                                | Кортеж                 |
| `set()`                                  | Множество              |
| `frozenset()`                            | Неизменяемое множество |
| `dict()`                                 | Словарь                |
| `range(start, stop[, step])`             | Диапазон               |
| `slice(start, stop[, step])`             | Срез                   |
| `bytes()`, `bytearray()`, `memoryview()` | Работа с байтами       |

---

### 🔣 Преобразование типов

| Функция                        | Описание                        |
| ------------------------------ | ------------------------------- |
| `int(x[, base])`               | Преобразование в целое число    |
| `float(x)`                     | Вещественное число              |
| `complex([real[, imag]])`      | Комплексное число               |
| `str(x)`                       | Строка                          |
| `chr(i)`                       | Символ из Unicode по номеру     |
| `ord(c)`                       | Unicode-код символа             |
| `hex(x)`                       | Шестнадцатеричная строка        |
| `oct(x)`                       | Восьмеричная строка             |
| `bin(x)`                       | Двоичная строка                 |
| `ascii(x)`                     | Строка с ASCII-экранированием   |
| `repr(x)`                      | Строковое представление объекта |
| `format(value[, format_spec])` | Форматирование строки           |

---

### 🗃️ Ввод-вывод и взаимодействие

| Функция                                   | Описание                  |
| ----------------------------------------- | ------------------------- |
| `input([prompt])`                         | Чтение ввода пользователя |
| `print(*objects, sep=' ', end='\n', ...)` | Вывод на экран            |
| `open(file, mode='r', ...)`               | Открытие файла            |

---

### 🧱 Работа с объектами и классами

| Функция                         | Описание                      |
| ------------------------------- | ----------------------------- |
| `getattr(obj, name[, default])` | Получение атрибута            |
| `setattr(obj, name, value)`     | Установка атрибута            |
| `delattr(obj, name)`            | Удаление атрибута             |
| `hasattr(obj, name)`            | Проверка наличия атрибута     |
| `vars([obj])`                   | Словарь атрибутов объекта     |
| `dir([object])`                 | Список атрибутов и методов    |
| `help([object])`                | Встроенная справка            |
| `object()`                      | Базовый объект                |
| `super()`                       | Доступ к родительскому классу |

---

### 🛠️ Модульные и системные функции

| Функция                                | Описание                         |
| -------------------------------------- | -------------------------------- |
| `__import__(name, ...)`                | Динамический импорт              |
| `eval(expression, ...)`                | Вычисление выражения             |
| `exec(object, ...)`                    | Выполнение кода                  |
| `compile(source, filename, mode, ...)` | Компиляция кода                  |
| `globals()`                            | Глобальные переменные            |
| `locals()`                             | Локальные переменные             |
| `id(obj)`                              | Уникальный идентификатор объекта |
| `hash(obj)`                            | Хеш-значение объекта             |
| `memoryview(obj)`                      | Представление памяти             |

---

Если хочешь, я могу:

* Привести примеры использования каждой функции.
* Сгруппировать по задачам (например, работа со строками, с файлами и т.д.).
* Или сохранить это в виде PDF/таблицы/файла.
