from random import choice, randint

with open("wordlists/nouns.txt", "r") as noun_file:
    nouns = list(noun_file.read().splitlines())
    
with open("wordlists/plurals.txt", "r") as plural_file:
    plurals = list(plural_file.read().splitlines())
    
with open("wordlists/noun_phrases.txt", "r") as noun_phrase_file:
    noun_phrases = list(noun_phrase_file.read().splitlines())
    
with open("wordlists/verbs.txt", "r") as verb_file:
    verbs = list(verb_file.read().splitlines())
    
with open("wordlists/transitives.txt", "r") as transitive_file:
    transitives = list(transitive_file.read().splitlines())
    
with open("wordlists/intransitives.txt", "r") as intransitive_file:
    intransitives = list(intransitive_file.read().splitlines())
    
with open("wordlists/adjectives.txt", "r") as adjective_file:
    adjectives = list(adjective_file.read().splitlines())
    
with open("wordlists/prepositions.txt", "r") as preposition_file:
    prepositions = list(preposition_file.read().splitlines())
    
with open("wordlists/interjections.txt", "r") as interjection_file:
    interjections = list(interjection_file.read().splitlines())
    

first_half = randint(1, 6)

if first_half == 1:
    first_half = choice(verbs)
    
elif first_half == 2:
    first_half = choice(transitives)
    
elif first_half == 3:
    first_half = choice(intransitives)
    
if first_half == 4:
    first_half = choice(adjectives)
    
elif first_half == 5:
    first_half = choice(prepositions)
    
elif first_half == 6:
    first_half = choice(interjections)


second_half = randint(1, 3)

if second_half == 1:
    second_half = choice(nouns)
    
elif second_half == 2:
    second_half = choice(plurals)
    
elif second_half == 3:
    second_half = choice(noun_phrases)
    
print first_half.upper() +" "+second_half.upper()