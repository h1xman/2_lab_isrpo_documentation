# Введение
**Geometric lib** -- это библиотека, разработанная на Python, для проведения самых разнообразных вычислений, касающихся геометрических фигур. 
Текущая версия библиотеки поддержиает базовые вычисления, касающиеся простейших геометрических фигур. В дальнейшем, этот спектр будет расширяться.

## Подключение библиотеки

Для подключения библиотеки (а также во всех дальнейших примерах) используется `import geometric_lib`

## Поддержка библиотеки

На данный момент библиотека поддерживается на всех версиях Python на любых устройствах.

# Описание проекта

## Структура библиотеки

```
.
├── circle.py
├── docs
│   └── README.md
├── rectangle.py
├── square.py
└── triangle.py
```

## Основные функции библиотеки и их описания

[geometric_lib.rectangle.area(width, height)](#rect-ar)\
[geometric_lib.rectangle.perimetr(width, height)](#rect-per)\
[geometric_lib.circle.area(ratio)](#cir-ar)\
[geometric_lib.circle.perimeter(ratio)](#cir-per)\
[geometric_lib.square.area(width)](#sq-ar)\
[geometric_lib.square.perimeter(width)](#sq-per)\
[geometric_lib.triangle.area(basis, height)](#tr-ar)\
[geometric_lib.triangle.perimeter(side_a, side_b, side_c)](#tr-per)


## Подробные описания функций

### <a id = "rect-ar"></a>geometric_lib.rectangle.area(width, height)

Вычисляет площадь прямоугольника с заданными сторонами

1. **width** - int/float
2. **height** - int/float
3. **returns** - float

Вычисления происходят по формуле:
> area = width * height

Пример использования:
```
import geometric_lib 

geometric_lib.rectangle.area(2, 5)      # -> 10.0
geometric_lib.rectangle.area(2, 5.5)    # -> 11.0
geometric_lib.rectangle.area(4.5, 5.5)  # -> 24.75
```

### <a id = "rect-per"></a>geometric_lib.rectangle.perimetr(width, height)

Вычисляет периметр прямоугольника с заданными сторонами

1. **width** - int/float
2. **height** - int/float
3. **returns** - float

Вычисления происходят по формуле:
> perimeter = 2 * (width + height)

Пример использования:
```
import geometric_lib 

geometric_lib.rectangle.perimetr(2, 5)      # -> 14.0
geometric_lib.rectangle.perimetr(2, 5.5)    # -> 15.0
geometric_lib.rectangle.perimetr(4.5, 5.5)  # -> 20.0
```

### <a id = "cir-ar"></a>geometric_lib.circle.area(ratio)

Вычисляет площадь круга с заданным радиусом

1. **ratio** - int/float
2. **returns** - float

Вычисления происходят по формуле:
> area = pi * ratio * ratio
> (Значение pi импортируется из модуля math)

Пример использования:
```
import geometric_lib 

geometric_lib.circle.area(2)      # -> ~ 12.56
geometric_lib.circle.area(2.3)      # -> ~ 16.62
```

### <a id = "cir-per"></a>geometric_lib.circle.perimeter(ratio)

Вычисляет площадь круга с заданным радиусом

1. **ratio** - int/float
2. **returns** - float

Вычисления происходят по формуле:
> area = pi * ratio * 2
> (Значение pi импортируется из модуля math)

Пример использования:
```
import geometric_lib 

geometric_lib.circle.perimeter(2)      # -> ~ 12.56
geometric_lib.circle.perimeter(2.3)      # -> ~ 14.45
```

### <a id = "sq-ar"></a>geometric_lib.square.area(width)

Вычисляет площадь квадрата с заданной стороной

1. **width** - int/float
2. **returns** - float

Вычисления происходят по формуле:
> area = width * width

Пример использования:
```
import geometric_lib 

geometric_lib.square.area(2)      # -> 4.0
geometric_lib.square.area(2.3)      # -> 5.29
```

### <a id = "sq-per"></a>geometric_lib.square.perimeter(width)

Вычисляет периметр квадрата с заданной стороной

1. **width** - int/float
2. **returns** - float

Вычисления происходят по формуле:
> area = width * 4

Пример использования:
```
import geometric_lib 

geometric_lib.square.perimeter(2)      # -> 8.0
geometric_lib.square.perimeter(2.3)      # -> 9.2
```

### <a id = "tr-ar"></a>geometric_lib.triangle.area(basis, height)

Вычисляет площадь треугольника с заданными основанием и высотой, проведенной к этому основанию

1. **basis** - int/float
2. **height** - int/float
3. **returns** - float

Вычисления происходят по формуле:
> area = basis * height / 2

Пример использования:
```
import geometric_lib 

geometric_lib.triangle.area(2, 2)      # -> 2.0
geometric_lib.triangle.area(2.3, 2)    # -> 2.3
geometric_lib.triangle.area(2.3, 2.2)  # -> 2.53
```

### <a id = "tr-per"></a>geometric_lib.triangle.perimeter(side_a, side_b, side_c)

Вычисляет периметр треугольника с заданными сторонами

1. **side_a, side_b, side_c**,  - int/float
2. **returns** - float

Вычисления происходят по формуле:
> perimeter = side_a + side_b + side_c 

Пример использования:
```
import geometric_lib 

geometric_lib.triangle.perimeter(2, 2, 2)      # -> 6.0
geometric_lib.triangle.perimeter(2.3, 2, 2)    # -> 6.3
...
```

# История изменений проекта

> [!NOTE]
> Все изменения расположены в обратном хронологическом порядке 

## 6b2a9d8

> Triangle.py added & commented

- Добавлен модуль вычислений для треугольника
- Добавлены комментарии к модулю

## a2795db

> Rectangle.py added & commented

- Добавлен модуль вычислений для прямоугольника
- Добавлены комментарии к модулю

## 3b1bd85

> Сomment to circle.py and square.py added

- Добавлены комментарии к модулю 
