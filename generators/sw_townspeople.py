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

cantrip = (
    'Acid splash',
    'Fire bolt',
    'Ray of frost',
)

jobs = [
    ('Alchemist',           'Staff', 'Oil - 1 flask', 'Arcana'),
    ('Animal trainer',      tool, animal, 'Animal Handling'),
    ('Apprentice',          tool, stuff, 'Athletics'),
    ('Armorer',             'Hammer', 'Iron helmet', 'Athletics'),
    ('Artisan',             'Staff', 'Clay', 'Perception'),
    ('Astrologer',          'Dagger', 'A spyglass', 'Nature'),
    ('Barber',              'Straight razor', 'Bandages', 'Medicine'),
    ('Barkeep',             tool, 'A bottle of spirits', 'Insight'),
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
    ('Farrier',             'Hammer', 'Pliers', 'Animal Handling'),
    ('Forester',            'Shortbow', 'Herbs', 'Nature'),
    ('Fortune-teller',      'Dagger', 'Tarot deck', 'Performance'),
    ('Gambler',             'Sap', 'Dice', 'Sleight of Hand'),
    ('Gongfarmer',          tool, 'Sack of night soil', 'Athletics'),
    ('Grave digger',        'Shovel', stuff, 'Athletics'),
    ('Groom',               'Whip', 'Saddle horse', 'Animal Handling'),
    ('Guard',               'Spear', 'Shield', 'Intimidation'),
    ('Guild beggar',        'Sling', 'Crutches', 'Deception'),
    ('Healer',              'Club', 'Vial of holy water', 'Medicine'),
    ('Hedge Witch',         'Knife', 'Healing herbs', 'Nature'),
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
    ('Scribe',              'Darts', 'Parchment, Quill pen and ink', 'Investigation'),
    ('Shaman',              tool, 'Herbs', 'Religion'),
    ('Smuggler',            'Sling', 'Waterproof sack', 'Stealth'),
    ('Squire',              'Short sword', 'Iron helmet', 'Athletics'),
    ('Tanner',              'Knife', 'Waterproof bag', 'Athletics'),
    ('Trader',              'Short sword', '20 sp', 'Persuasion'),
    ('Trapper',             'Sling', 'Badger pelt', 'Survival'),
    ('Urchin',              'Stick', 'Begging bowl', 'Stealth'),
    ('Vagrant',             'Club', 'Begging bowl', 'Deception'),
    ('Wainwright',          tool, 'Pushcart', 'Athletics'),
    ('Weaver',              'Dagger', 'Fine suit of clothes', 'Perception'),
    ('Wizard\'s apprentice', cantrip, 'Spellbook', 'Arcana'),
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
    'Axe'         : {'damage': '1d6 s', 'weight': '4', 'properties': 'versatile (1d8)'},
    'Club'        : {'damage': '1d4 b', 'weight': '2', 'properties': 'light'},
    'Dagger'      : {'damage': '1d4 p', 'weight': '1', 'properties': 'finesse, light, thrown(20/60)'},
    'Darts'       : {'damage': '1d4 p', 'weight': '1/4', 'properties': 'finesse, thrown(20/60)'},
    'Flail'       : {'damage': '1d6 b', 'weight': '2', 'properties': ''},
    'Hammer'      : {'damage': '1d4 b', 'weight': '2', 'properties': 'light, thrown(20/60)'},
    'Knife'       : {'damage': '1d4 s', 'weight': '1', 'properties': 'finesse, light, thrown(10/60)'},
    'Longbow'     : {'damage': '1d8 p', 'weight': '2', 'properties': 'range(150/600), heavy, two-handed'},
    'Longsword'   : {'damage': '1d8 s', 'weight': '3', 'properties': 'versatile (1d10)'},
    'Mace'        : {'damage': '1d6 b', 'weight': '4', 'properties': ''},
    'Scythe'      : {'damage': '1d6 s', 'weight': '3', 'properties': 'two-handed'},
    'Shortbow'    : {'damage': '1d6 p', 'weight': '2', 'properties': 'range(80/320), two-handed'},
    'Short sword' : {'damage': '1d6 p', 'weight': '2', 'properties': 'finesse, light'},
    'Sickle'      : {'damage': '1d4 s', 'weight': '2', 'properties': 'light'},
    'Sling'       : {'damage': '1d4 b', 'weight': '-', 'properties': 'range(30/120)'},
    'Spear'       : {'damage': '1d6 p', 'weight': '3', 'properties': 'thrown(20/60), versatile(1d8)'},
    'Staff'       : {'damage': '1d6 b', 'weight': '4', 'properties': 'versatile (1d8)'},
    'Whip'        : {'damage': '1d4 s', 'weight': '3', 'properties': 'finesse, reach'},
    'Acid splash' : {'damage': '1d6',   'weight': '-', 'properties': 'range: 60, 1-2 creatures within 5 feet, Dex save'},
    'Fire bolt'   : {'damage': '1d10',  'weight': '-', 'properties': 'range 120, Attack roll'},
    'Ray of frost': {'damage': '1d8',   'weight': '-', 'properties': 'range: 60, Attack roll, -10 feet movement on hit'},
}

ranged = [
    'Longbow',
    'Shortbow',
    'Sling',
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
    vals = [{'val':round(random.gammavariate(9, .3))+6} for x in range(6)]
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
    char['description'] = f'a {random.choice(personality)}, {random.choice(appearance)} '\
                          f'{race} with {random.choice(detail)} wearing '\
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

    print (wstats)
    print (atk_bonus)

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
        char['gear'] = [gear2]
    else:
        char['gear'] = [gear, gear2]
        
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
