#!/usr/bin/env python3

from random import choice

def percent(total, seen):
	return 100 - int((100 / len(total)) * len(seen))

with open("NFR.txt") as file:
	films = [line.split("\t") for line in file]

unseen_films = [film for film in films if not film[0]]

print(	"",
		f"Total Films: {len(films)}",
		f"Remaining Films: {len(unseen_films)}",
		f"Percent of films seen: {percent(films, unseen_films)}%",
		"Here is a random suggestion from the remaining films.",
		"{1} - {2}".format(*choice(unseen_films)),
		sep="\n")


