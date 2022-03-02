import random

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
    'A paper napkin with a few stanzas of poetry or a partial diagram of a machine scrawled on it',
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
    'a bushel of carrots',
    'a bushel of corn',
    'a bushel of parsnips',
    'a bushel of potatoes',
    'a bushel of radishes',
    'a bushel of rice',
    'a bushel of rutabagas'
    'a bushel of turnips',
    'a bushel of wheat',
)

animal = (
    'a chicken',
    'a cow',
    'a dog',
    'a duck',
    'a goat',
    'a goose',
    'a mule',
    'an ox',
    'a pony',
    'a pig',
    'a sheep',
)

jobs = [
    ('Alchemist',           'Staff', 'Oil - 1 flask', 'Arcana'),
    ('Animal trainer',      tool, animal, 'Animal Handling'),
    ('Apprentice',          tool, stuff, 'Athletics'),
    ('Armorer',             'Hammer', 'Iron helmet', 'Athletics'),
    ('Artisan',             'Staff', 'Clay', 'Perception'),
    ('Astrologer',          'Dagger', 'Spyglass', 'Nature'),
    ('Barber',              'Straight razor', 'Bandages', 'Medicine'),
    ('Barkeep',             tool, 'bottle of spirits', 'Insight'),
    ('Blacksmith',          'Hammer', 'Steel tongs', 'Athletics'),
    ('Bowyer',              'Longbow', '20 arrows', 'Perception'),
    ('Caravan guard',       'Short sword', 'Padded armor', 'Survival'), 
    ('Carpenter',           'Hammer', 'Nails', 'Perception'),
    ('Cobbler',             'Awl', 'Shoehorn', 'Perception'),
    ('Confidence artist',   'Dagger', 'Quality cloak', 'Deception'),
    ('Cook',                'Meat Cleaver', 'Fresh meat', 'Survival'),
    ('Cooper',              'Crowbar', 'Barrel', 'Perception'),
    ('Cutpurse',            'Dagger', stuff, 'Sleight of Hand'),
    ('Ditch digger',        'Shovel', stuff, 'Athletics'),
    ('Drifter',             'Sling', stuff, 'Investigation'),
    ('Farmer',              tool,  animal, 'Animal Handling'),
    ('Farrier',             'Hammer', 'pliers', 'Animal Handling'),
    ('Forester',            'Staff', 'Herbs', 'Nature'),
    ('Fortune-teller',      'Dagger', 'Tarot deck', 'Performance'),
    ('Gambler',             'Sap', 'Dice', 'Sleight of Hand'),
    ('Gongfarmer',          tool, 'Sack of night soil', 'Athletics'),
    ('Grave digger',        'Shovel', stuff, 'Athletics'),
    ('Groom',               'Whip', 'saddle horse', 'Animal Handling'),
    ('Guard',               'Spear', 'Shield', 'Intimidation'),
    ('Guild beggar',        'Sling', 'Crutches', 'Deception'),
    ('Healer',              'Club', 'Vial of Holy water', 'Medicine'),
    ('Hedge Witch',         'Knife', 'healing herbs', 'Nature'),
    ('Herbalist',           tool, 'Herbs', 'Nature'),
    ('Herder',              'Staff', 'Herding dog', 'Animal Handling'),
    ('Hunter',              'Shortbow', 'Deer pelt', 'Stealth'),
    ('Indentured servant',  'Staff', stuff, 'Athletics'),
    ('Innkeeper',           'Club', stuff, 'Insight'),
    ('Jester',              'Darts', 'Silk clothes', 'Performance'),
    ('Jeweler',             'Fine Dagger', 'Gem worth 20 gp', 'Perception'),
    ('Locksmith',           'Dagger', 'Fine tools', 'Perception'),
    ('Mason',               tool, stuff, 'Athletics'),
    ('Mayor',               'Mace', stuff, 'Persuasion'),
    ('Mercenary',           'Longsword', 'Hide armor', 'Survival'),
    ('Merchant',            'Dagger', stuff, 'Persuasion'),
    ('Miller/baker',        'Rolling pin', 'Flour - 1 lb', 'Athletics'),
    ('Miner',               'Pick', 'Lantern', 'Athletics'),
    ('Minstrel',            'Dagger', 'Lyre', 'Performance'),
    ('Noble',               'Longsword', 'Gold signet ring', 'History'),
    ('Orphan',              'Club', 'Rag doll', 'Stealth'),
    ('Outlaw',              'Short sword', 'Leather tunic', 'Deception'),
    ('Rat Catcher',         'Club', 'Small dog', 'Animal Handling'),
    ('Sage',                'Dagger', 'Notebook and pencils', 'History'),
    ('Scribe',              'Darts', 'Parchment, quill pen and ink', 'Investigation'),
    ('Shaman',              tool, 'Herbs', 'Religion'),
    ('Smuggler',            'Sling', 'Waterproof sack', 'Stealth'),
    ('Squire',              'Longsword', 'Iron helmet', 'Athletics'),
    ('Tanner',              'Knife', 'waterproof bag', 'Athletics'),
    ('Trader',              'Short sword', '20 sp', 'Persuasion'),
    ('Trapper',             'Sling', 'Badger pelt', 'Survival'),
    ('Urchin',              'Stick', 'Begging bowl', 'Stealth'),
    ('Vagrant',             'Club', 'Begging bowl', 'Deception'),
    ('Wainwright',          tool, 'Pushcart', 'Athletics'),
    ('Weaver',              'Dagger', 'Fine suit of clothes', 'Perception'),
    ('Wizard’s apprentice', 'Dagger', 'spellbook', 'Arcana'),
    ('Woodcutter',          'Axe', 'Bundle of wood', 'Athletics')
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
    'Axe'         : {'damage': '1d6 s', 'weight': '4lb', 'properties': 'versatile (1d8)'},
    'Club'        : {'damage': '1d4 b', 'weight': '2lb', 'properties': 'light'},
    'Dagger'      : {'damage': '1d4 p', 'weight': '1lb', 'properties': 'finesse, light, thrown(20/60)'},
    'Darts'       : {'damage': '1d4 p', 'weight': '1/4lb', 'properties': 'finesse, thrown(20/60)'},
    'Flail'       : {'damage': '1d6 b', 'weight': '2lb', 'properties': ''},
    'Hammer'      : {'damage': '1d4 b', 'weight': '2lb', 'properties': 'light, thrown(20/60)'},
    'Knife'       : {'damage': '1d4 s', 'weight': '1lb', 'properties': 'finesse, light, thrown(10/60)'},
    'Longbow'     : {'damage': '1d8 p', 'weight': '2lb', 'properties': 'range(150/600), heavy, two-handed'},
    'Longsword'   : {'damage': '1d8 s', 'weight': '3lb', 'properties': 'versatile (1d10)'},
    'Mace'        : {'damage': '1d6 b', 'weight': '4lb', 'properties': ''},
    'Scythe'      : {'damage': '1d6 s', 'weight': '3lb', 'properties': 'two-handed'},
    'Short sword' : {'damage': '1d6 p', 'weight': '2lb', 'properties': 'finesse, light'},
    'Sickle'      : {'damage': '1d4 s', 'weight': '2lb', 'properties': 'light'},
    'Sling'       : {'damage': '1d4 b', 'weight': '-', 'properties': 'range(30/120)'},
    'Spear'       : {'damage': '1d6 p', 'weight': '3lb', 'properties': 'thrown(20/60), versatile(1d8)'},
    'Staff'       : {'damage': '1d6 b', 'weight': '4lb', 'properties': 'versatile (1d8)'},
    'Whip'        : {'damage': '1d4 s', 'weight': '3lb', 'properties': 'finesse, reach'},
}


skills = (
    'Athletics',
    'Acrobatics',
    'Sleight of Hand',
    'Stealth',
    'Arcana',
    'History',
    'Investigation',
    'Nature',
    'Religion',
    'Animal Handling',
    'Insight',
    'Medicine',
    'Perception',
    'Survival',
    'Deception',
    'Intimidation',
    'Performance',
    'Persuasion'
)

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
    vals = [round(random.gammavariate(9, .3))+6 for x in range(6)]
    return dict(zip(labels, vals))

proficiency_bonus = 1
score_mod = lambda x: x//2 - 5
# don't forget '{0:+}'.format(value) to get leading +

def character():
    char = {}
    stats = statblock()
    char['abilities'] = stats 
    dex_mod = score_mod(stats['dex'])
    char['ability_mods'] = {k:f'{score_mod(v):+}' for (k,v) in stats.items()}
    (job, weapon, gear, prof) = random.choice(jobs)

    if isinstance(weapon, tuple):
        weapon = random.choice(weapon)
    
    if isinstance(gear, tuple):
        gear = random.choice(gear)

    race = random.choice(available_races)
    char['race'] = race
    char['size'] = race_traits[race]['size']
    char['speed'] = race_traits[race]['speed']
    char['description'] = f'a {random.choice(personality)}, {random.choice(appearance)} '\
                          f'{race} with {random.choice(detail)} wearing '\
                          f'{random.choice(clothing)} clothes.'
    char['job'] = job
    char['weapon'] = weapon
    char['weapon_stats'] = weapon_stats.get(weapon, default_weapon)
    char['gear'] = [gear, random.choice(stuff)]
    char['ac'] = armor_values.get(gear, 10) + dex_mod
    char['initiative'] = dex_mod
    char['hit_points'] = 6 + score_mod(stats['con'])
    char['hit_dice'] = '1d6'
    
    char['skills'] = {}
    char['proficiency_bonus'] = proficiency_bonus
    char['proficiencies'] = {}
    for skill in skill_ability.keys():
        val = score_mod(char['abilities'][skill_ability[skill]])
        if skill == prof:
            val += proficiency_bonus
        char['skills'][skill] = f'{val:+}'
        char['proficiencies'][skill] = True if skill == prof else False

    return char


if __name__ == '__main__':
    print(character())
