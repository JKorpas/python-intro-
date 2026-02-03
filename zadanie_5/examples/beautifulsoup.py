# Link do repo: https://github.com/JKorpas/python-intro-
# Potrzebny lxml bo to parser którego będziemy wykorzystywać
import bs4
import requests

URL = "https://realpython.github.io/fake-jobs/"

# wysyłamy żadanie GET do servera i zapisujemy w zmiennej bs_response
bs_response = requests.get(URL)
# sprawdzenie czy udało się pobrać
bs_response.raise_for_status()
# tworzymy obiekt typu beautifulsoup który pozwala na parsowanie HTML, bs_response.text zawiera surowy kod
soup = bs4.BeautifulSoup(bs_response.text, "lxml")


print(soup.title.text)

# wyswietlimy pierwsze wystąpienie czyli zawartosc pierwszego ogłoszenia
first_job = soup.find("div", class_="card-content")
print(first_job.text)

# teraz zbierzemy wszystkie stanowiska i je wyswietlimy
job_titles = soup.find_all("h2", class_="title is-5")
print(job_titles)

# wyciagamy tekst z tagu oraz białę znaki
for job in job_titles:
    print(f"{job.text.strip()}")
