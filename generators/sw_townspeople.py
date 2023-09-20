import random
import textwrap

tool = (
    'axe',
    'flail',
    'pitchfork',
    'rake',
    'scythe',
    'shears',
    'sickle',
    'pick',
    'spade',
    'chisel',
    'hammer',
    'auger',
    'saw',
    'knife'
)

appearance = (
    'aquiline',
    'athletic',
    'barrel-chested',
    'boney',
    'brawny',
    'brutish',
    'chiseled',
    'coltish',
    'craggy',
    'delicate',
    'furrowed',
    'gaunt',
    'gorgeous',
    'grizzled',
    'haggard',
    'handsome',
    'hideous',
    'lanky',
    'pudgy',
    'scrawny',
    'slender',
    'solid',
    'square-jawed',
    'statuesque',
    'towering',
    'trim',
    'weathered',
    'willowy',
    'wiry',
    'wrinkled',
)

detail =  (
    'a birthmark',
    'braided hair',
    'a broken nose',
    'bronze skin',
    'bushy eyebrows',
    'curly hair',
    'dark skin',
    'a deep voice',
    'dreadlocks',
    'an exotic accent',
    'freckles',
    'a gravelly voice',
    'a gold tooth',
    'a hoarse voice',
    'a huge beard',
    'light skin',
    'long hair',
    'matted hair',
    'missing teeth',
    'a mustache',
    'mutton chops',
    'nine fingers',
    'oiled hair',
    'one eye',
    'pale skin',
    'piercings',
    'sallow skin',
    'scars',
    'a shaved head',
    'a sunburn',
    'tangled hair',
    'tattoos',
    'a topknot',
)

clothing = (
    'antique',
    'bedraggled',
    'ceremonial',
    'dated',
    'decaying',
    'eccentric',
    'elegant',
    'exotic',
    'fashionable',
    'flamboyant',
    'food-stained',
    'formal',
    'frayed',
    'frumpy',
    'grimy',
    'lacey',
    'muddy',
    'oversized',
    'patched',
    'patterened',
    'perfumed',
    'practical',
    'rumpled',
    'singed',
    'tasteless',
    'torn',
    'undersized',
    'wine-stained',
    'worn out',
)

personality = (
    'bitter',
    'brave',
    'cautious',
    'chipper',
    'contrary',
    'cowardly',
    'cunning',
    'driven',
    'entitled',
    'gregarious',
    'grumpy',
    'hotheaded',
    'inquisitive',
    'jolly',
    'lazy',
    'loyal',
    'menacing',
    'mopey',
    'nervous',
    'protective',
    'righteous',
    'rude',
    'sarcastic',
    'savage',
    'scheming',
    'serene',
    'spacey',
    'stoic',
    'stubborn',
    'stuck-up',
    'suspicious',
    'wisecracking'
)

stuff = (
    'A folded piece of leather containing several pieces of blank parchment',
    'A diary/journal',
    'A bag of various pretty stones and small coins',
    'A key',
    'A half eaten piece of cheese',
    'A silver ring',
    'A fishing hook',
    'A love poem',
    'A brass signet ring',
    'A sea shell',
    'A small piece of parchment',
    'A small bone knife carved with runes',
    'A palm-sized brass coin from a distant Fire Giant city',
    'A paper napkin with a few stanzas of poetry',
    'A paper napkin with a diagram of a machine scrawled on it',
    'A piece of chalk',
    'A small crystal',
    'A deck of cards',
    'A leather bag full of seeds',
    'A roughly scribbled map on a piece of parchment folded up three times',
    'A feather',
    'An old love letter neatly but repeated folded and worn from age',
    'A simple pen knife',
    'A poorly made rope doll with button eyes and frayed yellow cloth for hair',
    'A tiny nugget of fool\'s gold',
    'A tinder box',
    'A handkerchief',
    'A bottle cork with a small blue star inked on the bottom',
    'A wrapped sandwich',
    'A lovenote',
    'A half eaten ham sandwich',
    'The perfect skipping stone',
    'A small pouch of nuts and dried meats',
    'A charm of antlers',
    'A small wooden figurine carved into the shape of an owlbear',
    'A small brass bell',
    'A brooch',
    'A game piece',
    'A nice shell comb',
    'An oil lamp',
    'A sewing needle and thread',
    'A tobacco pipe',
    'A wooden flute',
    'A small steel mirror',
    'A pouch of marbles',
    'A tin of sulfur',
    'A tuning fork',
    'A small first aid kit',
    'A ball of twine',
    'A small metal flask',
    'Flint and Steel',
    'A copper ring etched with runes',
    'A quartz crystal'    
)

produce = (
    'A bushel of carrots',
    'A bushel of corn',
    'A bushel of parsnips',
    'A bushel of potatoes',
    'A bushel of radishes',
    'A bushel of rice',
    'A bushel of rutabagas'
    'A bushel of turnips',
    'A bushel of wheat',
)

animal = (
    'A chicken',
    'A cow',
    'A dog',
    'A duck',
    'A goat',
    'A goose',
    'A mule',
    'An ox',
    'A pony',
    'A pig',
    'A sheep',
)

cantrip = (
    'acid splash',
    'fire bolt',
    'ray of frost',
)

jobs = [
    ('alchemist',           'staff', 'Oil - 1 flask', 'Arcana'),
    ('animal trainer',      tool, animal, 'Animal Handling'),
    ('apprentice',          tool, stuff, 'Athletics'),
    ('armorer',             'hammer', 'Iron helmet', 'Athletics'),
    ('artisan',             'staff', 'Clay', 'Perception'),
    ('astrologer',          'dagger', 'A spyglass', 'Nature'),
    ('barber',              'straight razor', 'Bandages', 'Medicine'),
    ('barkeep',             tool, 'A bottle of spirits', 'Insight'),
    ('blacksmith',          'hammer', 'Steel tongs', 'Athletics'),
    ('bowyer',              'longbow', '20 arrows', 'Perception'),
    ('caravan guard',       'short sword', 'Padded armor', 'Survival'),
    ('carpenter',           'hammer', 'Nails', 'Perception'),
    ('cobbler',             'awl', 'Shoehorn', 'Perception'),
    ('confidence artist',   'dagger', 'Quality cloak', 'Deception'),
    ('cook',                'meat cleaver', 'Fresh meat', 'Survival'),
    ('cooper',              'crowbar', 'Barrel', 'Perception'),
    ('cutpurse',            'dagger', stuff, 'Sleight of Hand'),
    ('ditch digger',        'shovel', stuff, 'Athletics'),
    ('drifter',             'sling', stuff, 'Investigation'),
    ('farmer',              tool,  animal, 'Animal Handling'),
    ('farrier',             'hammer', 'Pliers', 'Animal Handling'),
    ('forester',            'shortbow', 'Herbs', 'Nature'),
    ('fortune-teller',      'dagger', 'Tarot deck', 'Performance'),
    ('gambler',             'sap', 'Dice', 'Sleight of Hand'),
    ('gongfarmer',          tool, 'Sack of night soil', 'Athletics'),
    ('grave digger',        'shovel', stuff, 'Athletics'),
    ('groom',               'whip', 'saddle horse', 'Animal Handling'),
    ('guard',               'spear', 'shield', 'Intimidation'),
    ('guild beggar',        'sling', 'Crutches', 'Deception'),
    ('healer',              'club', 'Vial of holy water', 'Medicine'),
    ('hedge witch',         'knife', 'Healing herbs', 'Nature'),
    ('herbalist',           tool, 'Herbs', 'Nature'),
    ('herder',              'staff', 'Herding dog', 'Animal Handling'),
    ('hunter',              'shortbow', 'Deer pelt', 'Stealth'),
    ('indentured servant',  'staff', stuff, 'Athletics'),
    ('innkeeper',           'club', stuff, 'Insight'),
    ('jester',              'darts', 'Silk clothes', 'Performance'),
    ('jeweler',             'fine dagger', 'Gem worth 20 gp', 'Perception'),
    ('locksmith',           'dagger', 'Fine tools', 'Perception'),
    ('mason',               tool, stuff, 'Athletics'),
    ('mayor',               'mace', stuff, 'Persuasion'),
    ('mercenary',           'longsword', 'Hide armor', 'Survival'),
    ('merchant',            'dagger', stuff, 'Persuasion'),
    ('miller/baker',        'rolling pin', 'Flour - 1 lb', 'Athletics'),
    ('miner',               'pick', 'Lantern', 'Athletics'),
    ('minstrel',            'dagger', 'Lyre', 'Performance'),
    ('noble',               'longsword', 'Gold signet ring', 'History'),
    ('orphan',              'club', 'Rag doll', 'Stealth'),
    ('outlaw',              'short sword', 'Leather tunic', 'Deception'),
    ('rat catcher',         'club', 'Small dog', 'Animal Handling'),
    ('sage',                'dagger', 'Notebook and pencils', 'History'),
    ('scribe',              'darts', 'Parchment, Quill pen and ink', 'Investigation'),
    ('shaman',              tool, 'Herbs', 'Religion'),
    ('smuggler',            'sling', 'Waterproof sack', 'Stealth'),
    ('squire',              'short sword', 'Iron helmet', 'Athletics'),
    ('tanner',              'knife', 'Waterproof bag', 'Athletics'),
    ('trader',              'short sword', '20 sp', 'Persuasion'),
    ('trapper',             'sling', 'Badger pelt', 'Survival'),
    ('urchin',              'stick', 'Begging bowl', 'Stealth'),
    ('vagrant',             'club', 'Begging bowl', 'Deception'),
    ('wainwright',          tool, 'Pushcart', 'Athletics'),
    ('weaver',              'dagger', 'Fine suit of clothes', 'Perception'),
    ('wizard\'s apprentice', cantrip, 'Spellbook', 'Arcana'),
    ('woodcutter',          'axe', 'Bundle of wood', 'Athletics')
]

armor_values = {
    'Iron helmet'   : 11,
    'Padded armor'  : 11,
    'Shield'        : 12,
    'Hide armor'    : 12,
    'Leather tunic' : 11,
}

default_weapon = {'damage': '1d4', 'weight': '1lb', 'properties': 'improvised, thrown(20/60)'}
weapon_stats = {
    'axe'         : {'damage': '1d6 s', 'weight': '4', 'properties': 'versatile (1d8)'},
    'club'        : {'damage': '1d4 b', 'weight': '2', 'properties': 'light'},
    'dagger'      : {'damage': '1d4 p', 'weight': '1', 'properties': 'finesse, light, thrown(20/60)'},
    'darts'       : {'damage': '1d4 p', 'weight': '1/4', 'properties': 'finesse, thrown(20/60)'},
    'flail'       : {'damage': '1d6 b', 'weight': '2', 'properties': ''},
    'hammer'      : {'damage': '1d4 b', 'weight': '2', 'properties': 'light, thrown(20/60)'},
    'knife'       : {'damage': '1d4 s', 'weight': '1', 'properties': 'finesse, light, thrown(10/60)'},
    'longbow'     : {'damage': '1d8 p', 'weight': '2', 'properties': 'range(150/600), heavy, two-handed'},
    'longsword'   : {'damage': '1d8 s', 'weight': '3', 'properties': 'versatile (1d10)'},
    'mace'        : {'damage': '1d6 b', 'weight': '4', 'properties': ''},
    'scythe'      : {'damage': '1d6 s', 'weight': '3', 'properties': 'two-handed'},
    'shortbow'    : {'damage': '1d6 p', 'weight': '2', 'properties': 'range(80/320), two-handed'},
    'short sword' : {'damage': '1d6 p', 'weight': '2', 'properties': 'finesse, light'},
    'sickle'      : {'damage': '1d4 s', 'weight': '2', 'properties': 'light'},
    'sling'       : {'damage': '1d4 b', 'weight': '-', 'properties': 'range(30/120)'},
    'spear'       : {'damage': '1d6 p', 'weight': '3', 'properties': 'thrown(20/60), versatile(1d8)'},
    'staff'       : {'damage': '1d6 b', 'weight': '4', 'properties': 'versatile (1d8)'},
    'whip'        : {'damage': '1d4 s', 'weight': '3', 'properties': 'finesse, reach'},
    'acid splash' : {'damage': '1d6',   'weight': '-', 'properties': 'range: 60, 1-2 creatures within 5 feet, Dex save'},
    'fire bolt'   : {'damage': '1d10',  'weight': '-', 'properties': 'range 120, Attack roll'},
    'ray of frost': {'damage': '1d8',   'weight': '-', 'properties': 'range: 60, Attack roll, -10 feet movement on hit'},
}

ranged = [
    'longbow',
    'shortbow',
    'sling',
]

skill_ability = {
    'Athletics': 'str',
    'Acrobatics': 'dex',
    'Sleight of Hand': 'dex',
    'Stealth': 'dex',
    'Arcana' : 'int',
    'History' : 'int',
    'Investigation' : 'int',
    'Nature' : 'int',
    'Religion' : 'int',
    'Animal Handling' : 'wis',
    'Insight' : 'wis',
    'Medicine' : 'wis',
    'Perception' : 'wis',
    'Survival' : 'wis',
    'Deception' : 'cha',
    'Intimidation' : 'cha',
    'Performance' : 'cha',
    'Persuasion' : 'cha',
}

available_races = (
    'Dragonborn',
    'Dwarf',
    'Elf',
    'Gnome',
    'Half-Elf',
    'Half-Orc',
    'Halfling',
    'Human',
    'Tiefling',
)

race_traits = {
    'Aarakocra'    : {'languages': 'Common, Aarakocra, Auran',  'size': 'Medium', 'speed':25},
    'Aasimar'      : {'languages': 'Common, Celestial',         'size': 'Medium', 'speed':30},
    'Bugbear'      : {'languages': 'Common, Goblin',            'size': 'Medium', 'speed':30},
    'Centaur'      : {'languages': 'Common, Sylvan',            'size': 'Medium', 'speed':40},
    'Changeling'   : {'languages': 'Common, 2',                 'size': 'Medium', 'speed':30},
    'Dragonborn'   : {'languages': 'Common, Draconic',          'size': 'Medium', 'speed':30},
    'Dwarf'        : {'languages': 'Common, Dwarf',             'size': 'Medium', 'speed':25},
    'Elf'          : {'languages': 'Common, Elvish',            'size': 'Medium', 'speed':30},
    'Firbolg'      : {'languages': 'Common, Elvish, Giant',     'size': 'Medium', 'speed':30},
    'Genasi'       : {'languages': 'Common, Primordial',        'size': 'Medium', 'speed':30},
    'Gith'         : {'languages': 'Common, Gith',              'size': 'Medium', 'speed':30},
    'Gnome'        : {'languages': 'Common, Gnomish',           'size': 'Small' , 'speed':25},
    'Goblin'       : {'languages': 'Common, Goblin',            'size': 'Small' , 'speed':30},
    'Goliath'      : {'languages': 'Common, Giant',             'size': 'Medium', 'speed':30},
    'Halfling'     : {'languages': 'Common, Halfling',          'size': 'Small' , 'speed':25},
    'Half-Elf'     : {'languages': 'Common, Elvish',            'size': 'Medium', 'speed':30},
    'Half-Orc'     : {'languages': 'Common, Orc',               'size': 'Medium', 'speed':30},
    'Hobgoblin'    : {'languages': 'Common, Goblin',            'size': 'Medium', 'speed':30},
    'Human'        : {'languages': 'Common, 1',                 'size': 'Medium', 'speed':30},
    'Kalashtar'    : {'languages': 'Common, Quori, 1',          'size': 'Medium', 'speed':30},
    'Kenku'        : {'languages': 'Common, Auran ',            'size': 'Medium', 'speed':30},
    'Kobold'       : {'languages': 'Common, Draconic',          'size': 'Small' , 'speed':30},
    'Lizardfolk'   : {'languages': 'Common, Draconic',          'size': 'Medium', 'speed':30},
    'Loxodon'      : {'languages': 'Common, Loxodon',           'size': 'Medium', 'speed':30},
    'Minotaur'     : {'languages': 'Common, Minotaur',          'size': 'Medium', 'speed':30},
    'Orc'          : {'languages': 'Common, Orc',               'size': 'Medium', 'speed':30},
    'Shifter'      : {'languages': 'Common',                    'size': 'Medium', 'speed':30},
    'Simic Hybrid' : {'languages': 'Common, Elvish/Vedalken',   'size': 'Medium', 'speed':30},
    'Tabaxi'       : {'languages': 'Common, 1',                 'size': 'Medium', 'speed':30},
    'Tiefling'     : {'languages': 'Common, Infernal',          'size': 'Medium', 'speed':30},
    'Tortle'       : {'languages': 'Common, Aquan',             'size': 'Medium', 'speed':30},
    'Triton'       : {'languages': 'Common, Aquan',             'size': 'Medium', 'speed':30},
    'Vedalken'     : {'languages': 'Common, Vedalken, 1',       'size': 'Medium', 'speed':30},
    'Warforged'    : {'languages': 'Common',                    'size': 'Medium', 'speed':30},
    'Yuan-Ti'      : {'languages': 'Common, Abyssal, Draconic', 'size': 'Medium', 'speed':30},
}

    
def statblock():
    labels = ('str', 'dex', 'con', 'int', 'wis', 'cha')
    vals = [{'val':round(random.gammavariate(10, .4))+6} for x in range(6)]
    return dict(zip(labels, vals))

proficiency_bonus = 1
score_mod = lambda x: x//2 - 5
# don't forget '{0:+}'.format(value) to get leading +

def character():
    char = {}
    stats = statblock()
    for ability in stats.keys():
        mod = score_mod(stats[ability]['val'])
        stats[ability]['mod'] = mod
        stats[ability]['modstr'] = f'{mod:+}'
        
    char['abilities'] = stats 
    (job, weapon, gear, prof) = random.choice(jobs)

    if isinstance(weapon, tuple):
        weapon = random.choice(weapon)
    
    if isinstance(gear, tuple):
        gear = random.choice(gear)

    race = random.choice(available_races)
    char['race'] = race
    char['size'] = race_traits[race]['size']
    char['speed'] = race_traits[race]['speed']
    pers = random.choice(personality)
    article = 'an' if pers[0] in 'aeiou' else 'a'
    char['description'] = f'{article} {pers}, {random.choice(appearance)} '\
                          f'{race} with {random.choice(detail)} and is wearing '\
                          f'{random.choice(clothing)} clothes.'
    char['job'] = job
    char['weapon'] = weapon
    wstats = dict(weapon_stats.get(weapon, default_weapon))

    weapon_ability = 'str'
    if weapon in cantrip:
        weapon_ability = 'int'
    elif weapon in ranged:
        weapon_ability = 'dex'

    if 'finesse' in wstats['properties']:
        atk_bonus = max(stats['str']['mod'], stats['dex']['mod']) + proficiency_bonus
    else:
        atk_bonus = stats[weapon_ability]['mod'] + proficiency_bonus

    wstats['atk_bonus'] = f'{atk_bonus:+}'
    wstats['name'] = weapon
    attacks = [wstats]
    
    if 'thrown' in wstats['properties']:
        wstats2 = dict(weapon_stats.get(weapon, default_weapon))
        wstats2['name'] = f'{weapon} (thrown)'
        wstats2['atk_bonus'] = f'{(stats["dex"]["mod"] + proficiency_bonus):+}'
        attacks.append(wstats2)
        
    char['attacks'] = attacks

        
    gear2 = random.choice(stuff)
    while gear == gear2:
        gear2 = random.choice(stuff)

    if len(gear2) > 40:
        gearlist = textwrap.wrap(gear2, width=40, subsequent_indent='  ')
    else:
        gearlist = [gear2]
    
    char['money'] = {
        'pp': 0,
        'gp': 0,
        'ep': 0,
        'sp': 0,
        'cp': random.randrange(10,20)
    }
    
    #TODO: make this more generic
    if gear.endswith('sp'):
        char['money']['sp'] += int(gear.split()[0])
        char['gear'] = gearlist
    else:
        gearlist.insert(0, gear)
        char['gear'] = gearlist
        
        
    char['ac'] = armor_values.get(gear, 10) + stats['dex']['mod']
    char['initiative'] = stats['dex']['mod']
    char['hit_points'] = 6 + stats['con']['mod']
    char['hit_dice'] = '1d6'
    
    char['skills'] = {}
    char['proficiency_bonus'] = {'val': proficiency_bonus, 'valstr': f'{proficiency_bonus:+}'}
    for skill in skill_ability.keys():
        ability = skill_ability[skill]
        skillblock = {'ability': ability}
        val = stats[ability]['mod']
        if skill == prof:
            val += proficiency_bonus
        skillblock['val'] = val
        skillblock['valstr'] = f'{val:+}'
        skillblock['prof'] = (skill == prof)
        char['skills'][skill] = skillblock


    return char


if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(character())
