from random import choice, randint
from string import punctuation

adjectives = [
    "physiological",
    "colossal",
    "adorable",
    "amused",
    "uncomplicated",
    "comfortable",
    "determined",
    "effortless",
    "straightforward",
    "embarracing",
    "impossible"
]

nouns = [
    "apple", "guitar", "piano",
    "pizza", "helicopter", "planet",
    "pillow", "hair", "answer",
]

result = choice(adjectives) + choice(nouns) + str(randint(0, 9)) + choice(punctuation)

print(result)