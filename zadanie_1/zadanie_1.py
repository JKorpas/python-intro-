# Napisanie programu w Pythonie

dc_heroes = ["Batman", "Superman", "Wonder Woman", "Flash"]
cities = ["Gotham", "Metropolis", "Themyscira", "Central City"]


try:
    # Funkcja zip wykorzystana do złączania dwóch list  https://docs.python.org/3/library/functions.html#zip
    hero_city = list(zip(dc_heroes, cities))
    print(f"Bohaterowie i miasta: ", hero_city)

# Wyjątek TypeError do sprawdzenia czy oba zbiory są listami https://docs.python.org/3/library/exceptions.html#TypeError
except TypeError:
    print("Jednen ze zbirów nie jest listą")
# Funkcja len do sprawdzenia długości listy https://docs.python.org/3/library/functions.html#len
print("Ilość elementów w liscie: ", len(hero_city))
