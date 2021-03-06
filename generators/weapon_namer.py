import os
import random
from namegen import lc, new_word

#    singular    possesive     "of"...
targets = (
    ('ancient', 'ancient\'s', 'the ancients',),
    ('bandit',  'bandit\'s',  'the bandits',),
    ('beast',   'beast\'s',   'beasts',),
    ('chaos',   'chaos\'',    'chaos',),
    ('death',   'death\'s',   'death',),
    ('demon',   'demon\'s',   'demons',),
    ('dragon',  'dragon\'s',  'the dragon',),
    ('dream',   'dream\'s',   'dreams',),
    ('doom',    'doom\'s',    'doom',),
    ('dwarf',   'dwarves',    'the dwarves',),
    ('elf',     'elves',      'the elves',),
    ('fairy',   'fae\'s',     'the fae',),
    ('foe',     'foe\'s',     'the foe',),
    ('gnome',   'gnome\'s',   'the gnomes',),
    ('goblin',  'goblin\'s',  'the goblins',),
    ('god',     'god\'s',     'gods',),
    ('heart',   'heart\'s',   'hearts',),
    ('king',    'king\'s',    'kings',),
    ('law',     'law\'s',     'law',),
    ('mage',    'mage\'s',    'the mage',),
    ('mist',    'mist\'s',    'the mists',),
    ('night',   'night\'s',   'the night',),
    ('ogre',    'ogre\'s',    'the ogres',),
    ('orc',     'orc\'s',     'the orcs',),
    ('serpent', 'serpent\'s', 'the serpent',),
    ('soul',    'soul\'s',    'souls',),
    ('spirit',  'spirit\'s',  'spirits',),
    ('storm',   'storm\'s',   'the storm',),
    ('sun',     'sun\'s',     'the sun',),
    ('truth',   'truth\'s',   'truth',),
    ('thunder', 'thunder\'s', 'thunder',),
    ('world',   'world\'s',   'the world',),
    
)

titles = (
    ('{0} breaker',     {'b', 'm'}),
    ('{0} crusher',     {'b'}),
    ('{0} cutter',      {'s'}),
    ('{0} eater',       {'b', 'p', 'm', 's'}),
    ('{0} edge',        {'s'}),
    ('{0} killer',      {'b', 'p', 'm', 's'}),
    ('{0} knife',       {'p', 's'}),
    ('{0} piercer',     {'p'}),
    ('{0} poker',       {'p'}),
    ('{0} reaper',      {'b', 'p', 'm', 's'}),
    ('{0} slayer',      {'b', 'p', 'm', 's'}),
    ('{0} smasher',     {'b', 'm'}),
    ('{0} splitter',    {'s', 'm'}),
    ('{0} stabber',     {'p'}),
    ('{1} bane',        {'b', 'p', 'm', 's'}),
    ('{1} blade',       {'s', 'p'}),
    ('{1} end',         {'b', 'p', 'm', 's'}),
    ('{1} glory',       {'b', 'p', 'm', 's'}),
    ('{1} heart',       {'b', 'p', 'm', 's'}),
    ('{1} knife',       {'p', 's'}),
    ('{1} might',       {'b', 'p', 'm', 's'}),
    ('bane of {2}',     {'b', 'p', 'm', 's'}),
    ('blade of {2}',    {'p', 's'}),
    ('breath of {2}',   {'b', 'p', 'm', 's'}),
    ('defender of {2}', {'b', 'p', 'm', 's'}),
    ('glory of {2}',    {'b', 'p', 'm', 's'}),
    ('hammer of {2}',   {'b'}),
    ('knife of {2}',    {'p', 's'}),
    ('might of {2}',    {'b', 'p', 'm', 's'}),
    ('spirit of {2}',   {'b', 'p', 'm', 's'}),
    ('soul of {2}',     {'b', 'p', 'm', 's'}),
    ('tear of {2}',     {'b', 'p', 'm', 's'}),
    ('wind of {2}',     {'b', 'p', 'm', 's'}),
)

def titlecase(title):
    words = title.split()
    ignore = ('a', 'an', 'the', 'and', 'but', 'for', 'nor', 'or', 'so', 'yet',
              'in', 'to', 'for', 'on', 'at', 'as', 'from', 'by', 'of')
    words = [word if word in ignore else word[0].upper()+word[1:] for word in words]
    return ' '.join(words)
    
def name():
    langfiles = os.listdir('name_files')
    (hash, start) = lc(os.path.join('name_files',random.choice(langfiles)))
    name1 = new_word(hash, start, 3, 5)
    name2 = new_word(hash, start, 6, 10)
    return titlecase(' '.join((name1, name2)))

def generate_title(damtypes='pbsm'):
    damset = set(damtypes)
    options = [title[0] for title in titles if 
                    len(title[1].intersection(damset)) > 0 ]
    
    return random.choice(options).format(*random.choice(targets))

def named_title():
    return titlecase(' '.join((name(), 'the', generate_title())))
    
def title_gen(damtypes='pbsm'):
    while (1):
        yield titlecase(' '.join((name(), 'the', generate_title(damtypes))))
        
if __name__ == '__main__':
    title = title_gen(damtypes='b')
    for x in range(10):
        print(next(title))
