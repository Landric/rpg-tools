from random import choice
import pickle

def reset_names():
    names = {
            'part1':
            [
                'Ae',
                'Di',
                'Mo',
                'Fam',
            ],
            'part2':
            [
                'dar',
                'kil',
                'glar',
                'tres',
            ],
        }

    save_names(names)

def custom_names():
    pass

def save_names(names):
    name_file = open('names','w')
    pickle.dump(names, name_file)
    name_file.close()

def load_names():
    name_file = open('names')
    names = pickle.load(name_file)
    name_file.close()
    return names

def reset_titles():
    titles = {
            'adjective':
            [
                'adorable',
                'grotesque',
                'muddy',
                'screeching',
            ],
            'noun':
            [
                'apple',
                'hawk',
                'velvet',
                'wind',
            ],
        }

    save_titles(titles)

def custom_titles():
    pass

def save_titles(titles):
    title_file = open('titles','w')
    pickle.dump(titles, title_file)
    title_file.close()

def load_titles():
    title_file = open('titles')
    titles = pickle.load(title_file)
    title_file.close()
    return titles

def gen_name(race = None):
    names = load_names()
    return "{0}{1}".format(choice(names['part1']), choice(names['part2']))

def gen_title():
    titles = load_titles()
    return "the {0} {1}".format(choice(titles['adjective']), choice(titles['noun']))

def gen_name_and_title(race = None):
    return "{0}, {1}".format(gen_name(race), gen_title())
