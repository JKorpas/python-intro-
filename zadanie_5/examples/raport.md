# Link do repo: https://github.com/JKorpas/python-intro-
# Request 
https://realpython.com/python-requests/
https://requests.readthedocs.io/en/latest/
Biblioteka request umożlwia prosto i szybko pobrać dane z internetu. Kilka linijek kodu pozwala pobrać zawartość strony albo dane z API. Kod jest czytelny, łatwo go zrozumieć a do tego w sieci jest masa przykładów i poradników. 

To nie jest biblioteka standardowa, więc trzeba ją wcześniej pobrac i zainstalować. Biblioteka request jest ogarniczona pod względem stron na którch można ją wykorzystać, mianowicie nie można użyć na witrynach w których treść jest tworzona, aktualizowana lub modyfikowana w przeglądarce użytkownika w czasie rzeczywistym.
Requests było wspierane w Pythonie 2, jednak obecnie jest rozwijane wyłącznie dla Pythona 3

# Beautiful soup 
https://realpython.com/beautiful-soup-web-scraper-python/
https://tedboy.github.io/bs4_doc/

Jest to biblioteka która stanowi duet razem z biblioteką reqest. Sama z siebie niczego nie pobiera, a robi się to właśnie dzieki bibliotece request. Beautiful soup służy do analizowania kodu i wyszukiania rzeczy, co przy sporej ilosci kodu powoduję że może spowolnić działanie, gdyż wczytuje cały dokument HTML do pamięci.
Jeżeli chodzi o minusy to takie same jak przy request, czyli nie czyta stron dynamicznych oraz jest rozwijana aktualnie tylko dla Pythona3. 

# Lxml 
https://pypi.org/project/lxml/

To biblioteka przeznaczoną do parsowania HTML i XML. Dobrze radzi sobie z dużymi stronami i dużą ilością danych. Zaawansowany odpowiednik wbudowanego parsersa w biblioteke beautiful soup. Jedyny minus to trzeba go zainstalować gdyż jest to zewnetrzne narzedzie.