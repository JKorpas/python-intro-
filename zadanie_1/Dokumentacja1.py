# Opis funkcji wbudowanej

# https://docs.python.org/3/library/functions.html#zip
# zip() łączy elementy z dwóch zbiorów
print(zip.__doc__)

# https://docs.python.org/3/library/functions.html#sum
# sum() oblicza sumę wszystkich elementów liczbowych w danym zbiorze
print(sum.__doc__)

# https://docs.python.org/3/library/functions.html#abs
# abs() zwraca wartość bezwzględną pojedyńczej liczby
print(abs.__doc__)


# Opis modułu z biblioteki standardowe
import os
import random
import time

# https://docs.python.org/3/library/os.html
# os pozwala na interakcję z systemem operacyjnym, np. pracę z plikami i katalogami
print(os.__doc__)
# https://docs.python.org/3/library/random.html
# random służy do generowania liczb losowych oraz losowego wyboru elementów ze zbioru
print(random.__doc__)
# https://docs.python.org/3/library/time.html
# time umożliwia pracę z czasem, np. mierzenie czasu wykonania programu lub wstrzymywanie jego działania
print(time.__doc__)

# Opis wyjątku

# TypeError wyskakuje przy operacji na niepasujących typach danych np. string + int
# https://docs.python.org/3/library/exceptions.html#TypeError
print(TypeError.__doc__)
# ZeroDivisionError wyskakuje przy próbie dzielenia przez zero
# https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
print(ZeroDivisionError.__doc__)
# https://docs.python.org/3/library/exceptions.html#IndexError
# IndexError wyskakuje gdy odwołujemy się do nieistniejącego indeksu ze zbioru
print(IndexError.__doc__)
