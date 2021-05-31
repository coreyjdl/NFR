from collections import Counter

def by_year(film):
    if film:
        return film[2][-4:]

def decade_of_film(film):
    film_year = int(by_year(film))
    return (film_year // 10) * 10

with open("NFR.txt") as file:
	films = [line.split("\t") for line in file]

unseen_films = [film for film in films if not film[0]]

decades_count = Counter([decade_of_film(film) for film in unseen_films])

for decade in sorted(decades_count, reverse=True):
    print(decade, decades_count[decade])