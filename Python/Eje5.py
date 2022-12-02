# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def is_leap_year(year):
    return True if (year%4)==0 else False

print(is_leap_year(2024))