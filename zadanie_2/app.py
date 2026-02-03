# Link do repo: https://github.com/JKorpas/python-intro-
def check_email(email):
    # czy email jest stringiem
    if not isinstance(email, str):
        return False
    # czy email posiada znak "@"
    if email.count("@") != 1:
        return False
    # rozdzielenie emaila w miejscu znaku "@" oraz sprawdzenie czy czesci nie sa puste
    nazwa, domena = email.split("@")
    if nazwa == "" or domena == "":
        return False
    # czy jest kropka w czesci po @
    if "." not in domena:
        return False
    return True


def area(width, height):
    # czy wartosci ktore podajemy sa liczbami
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("The width and height must be type of in or float.")
    # czy te liczby sa większe od zera
    if not (width > 0 and height > 0):
        raise ValueError("The width and height must be positive.")
    return width * height


def sort_numbers(numbers):
    # czy zmiennna to lista
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    # czy zawawrtosc listy to float lub int
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("All elements in the list must be int or float.")
    return sorted(numbers)


def is_palindrome(text):
    # czy string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # usuwamy spacje i zmieniamy na małe litery do sprawdzenia
    cleaned_text = "".join(text.lower().split())

    return cleaned_text == cleaned_text[::-1]
