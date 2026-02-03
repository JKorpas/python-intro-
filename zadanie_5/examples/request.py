# Link do repo: https://github.com/JKorpas/python-intro-
import bs4
import requests

# Zapisujemy do zmiennej URL adres z którego bedziemy pobierać dane, w naszym przypadku jest to API, który dostarcza pytania do quizów z bazy Open Trivia Database (OTDB).
# https://opentdb.com/api_config.php
# można użyc do wygenerowania stałego URL np https://opentdb.com/api.php?amount=10&category=23&difficulty=hard&type=boolean
URL = "https://opentdb.com/api.php"

# Dla czytelnosci tutaj wpisujemy parametry, ile tych pytań oraz typ,
# w naszym przypadku 7 pytan typu prawda/fałsz
parameters = {
    "amount": 7,
    "type": "boolean",
}

# requests.get wysyła żadanie GET do servera
response = requests.get(URL, params=parameters)
# tutaj zmiany podpowiedź serwera w pythonowy słownik który pozwala na odwoływać się do odpowiednich pól
data = response.json()
# print(data) do wyswietlenia json'a
questions = data["results"]

# for i, q in enumerate(questions, start=1):
#     print(f"\nQuestion {i}: {q['question']}")
#     print("Correct answer:", q["correct_answer"])

bs_response = requests.get("https://realpython.github.io/fake-jobs/")
bs_response.raise_for_status()
soup = bs4.BeautifulSoup(bs_response)
