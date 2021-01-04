
def byYear(film):
    if film:
        return film[2]

with open("NFR.txt") as file:
	films = [line.split("\t") for line in file]

films.sort(reverse=True, key=byYear)
unseen_films = [film for film in films if not film[0]]

print(*(f"{film[1]} - {film[2]}" for film in unseen_films), sep="\n")