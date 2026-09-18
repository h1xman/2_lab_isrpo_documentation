import math


def area(r):
    '''
    Возвращает площадь круга заданного радиуса.
    
        Параметры:
            - r (float): радиус круга

        Возвращаемое значение:
            - circle_area (float):  площадь круга радиуса r
    '''
    
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга заданного радиуса.
    
        Параметры:
            - r (float): радиус круга

        Возвращаемое значение:
            - circle_perimeter (float):  периметр круга радиуса r
    '''

    return 2 * math.pi * r

