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

# Основные функции библиотеки и их описания


<a href="triangle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `triangle.py`





---

<a href="triangle.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(a, h)
```

Возвращает площадь треугольника с заданными сторонаой и высотой, проведенной к этой стороне. 





**Args:**
 
     - <b>а</b> (float):  длина стороны треугольника 
     - <b>h</b> (float):  длина высоты, проведенной к этой стороне 



**Returns:**
 
     - <b>triangle_area</b> (float):   площадь треугольника по стороне и проведенной к ней высоте 



**Examples:** 
> area(2.3, 2.2)  # -> 2.53 


---

<a href="triangle.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(a, b, c)
```

Возвращает периметр треугольника с заданными сторонами. 



**Args:**
 
     - <b>a</b> (float):  длины 1 стороны треугольника соответственно 
     - <b>b</b> (float):  длины 2 стороны треугольника соответственно 
     - <b>c</b> (float):  длины 3 стороны треугольника соответственно 





**Returns:**
 
     - <b>triangle_perimetr</b> (float):   периметр треугольника с заданными сторонами 



**Examples:** 
> perimeter(2, 2, 2)      # -> 6.0 




<a href="rectangle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rectangle.py`





---

<a href="rectangle.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(a, b)
```

Возвращает площадь прямоугольника с заданными сторонами. 



**Args:**
 
     - <b>а</b> (float):  длина 1-й стороны прямоугольника 
     - <b>b</b> (float):  длина 2-й стороны прямоугольника 



**Returns:**
 
     - <b>rectangle_area</b> (float):   площадь прямоугольника со сторонами a, b 



**Examples:** 
> area(4.5, 5.5)  # -> 24.75 


---

<a href="rectangle.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(a, b)
```

Возвращает периметр прямоугольника с заданными сторонами. 



**Args:**
 
     - <b>а</b> (float):  длина 1-й стороны прямоугольника 
     - <b>b</b> (float):  длина 2-й стороны прямоугольника 



**Returns:**
 
     - <b>rectangle_perimetr</b> (float):   периметр прямоугольника со сторонами a, b 



**Examples:** 
> perimetr(4.5, 5.5)  # -> 20.0 




<a href="circle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `circle.py`





---

<a href="circle.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(r)
```

Возвращает площадь круга заданного радиуса. 



**Args:**
 
     - <b>r</b> (float):  радиус круга 



**Returns:**
 
     - <b>circle_area</b> (float):   площадь круга радиуса r 



**Examples:** 
> area(2.3)      # -> ~ 16.62 


---

<a href="circle.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(r)
```

Возвращает периметр круга заданного радиуса. 



**Args:**
 
     - <b>r</b> (float):  радиус круга 



**Returns:**
 
     - <b>circle_perimeter</b> (float):   периметр круга радиуса r 



**Examples:** 
> perimeter(2.3)      # -> ~ 14.45 




<a href="square.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `square.py`





---

<a href="square.py#L1"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `area`

```python
area(a)
```

Возвращает площадь квадрата с заданной стороной. 



**Args:**
 
     - <b>а</b> (float):  длина стороны квадрата 



**Returns:**
 
     - <b>square_area</b> (float):   площадь квадрата со стороной a 



**Examples:** 
>  area(2.3)      # -> 5.29 


---

<a href="square.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `perimeter`

```python
perimeter(a)
```

Возвращает периметр квадрата с заданной стороной. 



**Args:**
 
     - <b>а</b> (float):  длина стороны квадрата 



**Returns:**
 
     - <b>square_perimeter</b> (float):   периметр квадрата со стороной a 



**Examples:** 
 > perimeter(2.3)      # -> 9.2 



# История изменений проекта

> [!NOTE]
> Все изменения расположены в обратном хронологическом порядке 



## 0071c9e 

> Func docs upgraded

- Исправлено README.md

## e3b3a5c

> Docs modified

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
