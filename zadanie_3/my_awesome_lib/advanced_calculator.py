from my_awesome_lib.basic_calculator import BasicCalculator


class AdvancedCalculator(BasicCalculator):
    """Zaawansowane operacje matematyczne (rozszerzenie klasy BasicCalculator)"""

    # Reszta z dzielenia
    def mod(self, x, y):
        return x % y

    # Dzielenie całkowite
    def floor_div(self, x, y):
        return x // y

    # Potegowanie
    def power(self, x, y):
        return x**y

    # Wartość bezwzględna
    def absolute(self, x):
        return abs(x)

    # Średnia
    def average(self, values):
        if not values:
            raise ValueError("List must not be empty")
        return sum(values) / len(values)

    # Maxymalna wartosc
    def maximum(self, values):
        return max(values)

    # Minimalna wartość
    def minimum(self, values):
        return min(values)
