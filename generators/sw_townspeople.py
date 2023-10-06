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
    'attractive',
    'barrel-chested',
    'boney',
    'brawny',
    'brutish',
    'burly',
    'chiseled',
    'coltish',
    'craggy',
    'delicate',
    'furrowed',
    'gangly',
    'gaunt',
    'gorgeous',
    'grizzled',
    'haggard',
    'handsome',
    'lanky',
    'middle-aged',
    'old',
    'petite',
    'plain',
    'pudgy',
    'scrawny',
    'short',
    'slender',
    'slim',
    'solid',
    'square-jawed',
    'statuesque',
    'stout',
    'tall',
    'towering',
    'trim',
    'weathered',
    'willowy',
    'wiry',
    'wrinkled',
    'young',
)

details =  (
    {'default': 'a birthmark',},
    {'default': 'a neat appearance', 'fur': 'braided hair', 'scales': 'lined scales', 'feathers': 'lined feathers',},
    {'default': 'a broken nose', 'feathers':'a crooked beak'},
    {'default': 'a bronze complexion', 'fur': 'bronze skin', 'scales': 'bronze scales', 'feathers': 'golden feathers', 'skin': 'bronze skin', 'mechanical': 'bronze plating'},
    {'default': 'a prominent brow', 'fur': 'bushy eyebrows',},
    {'default': 'a dark complexion', 'fur': 'curly hair', 'scales': 'patterned scales', 'feathers': 'striped wings', 'skin': 'tattooed arms'},
    {'default': 'dark skin', 'scales': 'dark scales', 'feathers': 'dark feathers', 'mechanical': 'dark plating'},
    {'default': 'a deep voice',},
    {'default': 'a high-pitched voice',},
    {'default': 'a rough complexion', 'fur': 'dreadlocks', 'scales': 'ridged scales', 'feathers': 'sleek feathers', 'skin': 'smooth skin'},
    {'default': 'an exotic accent',},
    {'default': 'freckles', 'scales': 'mottled scales', 'feathers': 'speckled plumage'},
    {'default': 'a gravelly voice',},
    {'default': 'a melodious voice',},
    {'default': 'a gold tooth', 'feathers': 'a chipped beak'},
    {'default': 'a hoarse voice',},
    {'default': 'a pronounced chin', 'fur': 'a huge beard', 'feathers': 'a large beak'},
    {'default': 'light skin', 'scales': 'pale shiny scales', 'feathers': 'faded plumage'},
    {'default': 'a long face', 'fur': 'long hair', 'scales': 'bright scales', 'feathers': 'graceful plumage', 'skin': 'leathery skin'},
    {'default': 'a dirty countenance', 'fur': 'matted hair', 'scales': 'dull scales', 'feathers': 'dusty feathers', 'skin': 'dry skin'},
    {'default': 'missing teeth', 'feathers': 'a chipped beak', 'mechanical': 'a damaged faceplate'},
    {'default': 'old eyes', 'fur': 'mutton chops'},
    {'default': 'nine fingers',},
    {'default': 'oily skin', 'fur': 'oiled hair', 'scales': 'oily scales', 'feathers': 'greasy feathers', 'skin': 'greasy skin'},
    {'default': 'one eye',},
    {'default': 'shifty eyes',},
    {'default': 'piercing eyes',},
    {'default': 'dark eyes',},
    {'default': 'a pale complexion', 'fur': 'pale skin', 'scales': 'pale scales', 'feathers': 'pale feathers', 'skin': 'pale skin'},
    {'default': 'piercings',},
    {'default': 'a pale complexion', 'fur': 'sallow skin', 'scales': 'blotchy scales', 'feathers': 'patchy feathers', 'skin': 'sallow skin'},
    {'default': 'scars',},
    {'default': 'an oddly shaped head', 'fur': 'a shaved head', 'scales': 'a ridge of scales on their head', 'feathers': 'a molting head', 'skin': 'a shiny bald head'},
    {'default': 'a sunburn', 'mechanical': 'soot stains', 'feathers': 'sun-bleached feathers'},
    {'default': 'a messy demeanor',  'fur': 'tangled hair', 'scales': 'missing scales', 'feathers': 'molting wings', 'skin': 'a blotchy complexion'},
    {'default': 'tattoos', 'mechanical': 'fine linework on their chassis'},
    {'default': 'an interesting hat', 'fur': 'a topknot', 'feathers': 'an impressive feather crest'},
    {'default': 'a long nose', 'feathers': 'a long beak'},
    {'default': 'a well-muscled build',},
    {'default': 'long fingers',},
)

clothing = (
    'antique',
    'bedraggled',
    'casual',
    'ceremonial',
    'classic',
    'colorful',
    'comfortable',
    'dated',
    'designer',
    'drab',
    'durable',
    'dusty',
    'eccentric',
    'elegant',
    'embroidered',
    'exotic',
    'expensive',
    'faded',
    'fancy',
    'fashionable',
    'flamboyant',
    'flattering',
    'formal',
    'frayed',
    'frumpy',
    'gaudy',
    'gothic',
    'grimy',
    'hand-sewn',
    'homespun',
    'humble',
    'ill-fitting',
    'imported',
    'lacey',
    'lavish',
    'layered',
    'lightweight',
    'loose-fitting',
    'mismatched',
    'modern',
    'motley',
    'muddy',
    'neat',
    'noble',
    'non-descript',
    'old-fashioned',
    'oversized',
    'paisley',
    'padded',
    'patched',
    'patterened',
    'perfumed',
    'practical',
    'refined',
    'reliable',
    'rumpled',
    'simple',
    'singed',
    'stained',
    'tailored',
    'tasteful',
    'tasteless',
    'tight',
    'torn',
    'traditional',
    'unique',
    'well-fitted',
    'woolen',
    'worn out',
)

personality = (
    'absent-minded',
    'adventurous',
    'ambitious',
    'angry',
    'awkward',
    'bitter',
    'bland',
    'blunt',
    'bold',
    'brave',
    'bureaucratic',
    'calm',
    'cautious',
    'charming',
    'cheerful',
    'chipper',
    'cold',
    'conceited',
    'confident',
    'contrary',
    'courteous',
    'cowardly',
    'creative',
    'cunning',
    'curious',
    'dependable',
    'determined',
    'diplomatic',
    'disciplined',
    'driven',
    'dull',
    'eager',
    'earnest',
    'easygoing',
    'educated',
    'eloquent',
    'energetic',
    'enigmatic',
    'enthusiastic',
    'entitled',
    'excited',
    'fearful',
    'flamboyant',
    'focused',
    'foolish',
    'friendly',
    'frugal',
    'funny',
    'generous',
    'greedy',
    'gregarious',
    'gruff',
    'grumpy',
    'happy',
    'honest',
    'honorable',
    'hotheaded',
    'humble',
    'independant',
    'inquisitive',
    'intimidating',
    'inventive',
    'irresponsible',
    'jolly',
    'keen',
    'kind',
    'knavish',
    'knowledgeable',
    'lazy',
    'loud',
    'loyal',
    'menacing',
    'merciful',
    'miserly',
    'mopey',
    'narcissistic',
    'nervous',
    'observant',
    'officious',
    'optimistic',
    'organized',
    'overconfident',
    'paranoid',
    'passionate',
    'patient',
    'perceptive',
    'perky',
    'persuasive',
    'petulant',
    'pretentious',
    'protective',
    'quaint',
    'quick-witted',
    'quiet',
    'quirky',
    'rational',
    'reckless',
    'resourceful',
    'respectable',
    'righteous',
    'rude',
    'rugged',
    'sarcastic',
    'savage',
    'selfish',
    'scheming',
    'serene',
    'sleepy',
    'slick',
    'smug',
    'sober',
    'sophisticated'
    'spacey',
    'stoic',
    'stubborn',
    'stuck-up',
    'surly',
    'suspicious',
    'taciturn',
    'talkitive',
    'uncouth',
    'unkempt',
    'vacuous',
    'violent',
    'wary',
    'weird',
    'wise',
    'wisecracking',
    'witty',
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
    'blade ward',
    'fire bolt',
    'guidance',
    'light',
    'magic stone',
    'produce flame',
    'ray of frost',
    'shocking grasp',
    'true strike',
)

jobs = {
    'alchemist':           ('staff', 'Oil - 1 flask', 'Arcana', 'int'),
    'animal trainer':      (tool, animal, 'Animal Handling', 'wis'),
    'apothecary':          (cantrip, 'vial of acid', 'Nature', 'int'),
    'apprentice':          (tool, stuff, 'Athletics', 'str'),
    'armorer':             ('hammer', 'Iron helmet', 'Athletics', 'str'),
    'artisan':             ('staff', 'Clay', 'Perception', 'dex'),
    'astrologer':          (cantrip, 'A spyglass', 'History', 'int'),
    'baker':               ('rolling pin', 'Loaf of fresh bread', 'Perception', None),
    'barber':              ('straight razor', 'Bandages', 'Medicine', 'dex'),
    'barkeep':             (tool, 'A bottle of spirits', 'Insight', 'cha'),
    'blacksmith':          ('hammer', 'Steel tongs', 'Athletics', 'str'),
    'bowyer':              ('longbow', '20 arrows', 'Perception', 'dex'),
    'butler':              ('dagger', 'a bottle of fine brandy', 'Insight', 'wis'),
    'caravan guard':       ('short sword', 'Padded armor', 'Survival', 'con'),
    'carpenter':           ('hammer', 'Nails', 'Perception', 'dex'),
    'cobbler':             ('awl', 'Shoehorn', 'Perception', 'dex'),
    'confidence artist':   ('dagger', 'Quality cloak', 'Deception', 'cha'),
    'cook':                ('meat cleaver', 'Fresh meat', 'Survival', None),
    'cooper':              ('crowbar', 'Barrel', 'Perception', 'dex'),
    'cutpurse':            ('dagger', stuff, 'Sleight of Hand', 'dex'),
    'ditch digger':        ('shovel', stuff, 'Athletics', 'str'),
    'drifter':             ('sling', stuff, 'Investigation', None),
    'farmer':              (tool,  animal, 'Animal Handling', None),
    'farrier':             ('hammer', 'Pliers', 'Animal Handling', 'str'),
    'forester':            ('shortbow', 'Herbs', 'Nature', 'wis'),
    'fortune-teller':      (('guidance', 'true strike'), 'Tarot deck', 'Performance', 'cha'),
    'gambler':             ('sap', 'Dice', 'Sleight of Hand', 'int'),
    'gongfarmer':          (tool, 'Sack of night soil', 'Athletics', None),
    'grave digger':        ('shovel', stuff, 'Athletics', 'str'),
    'groom':               ('whip', 'saddle horse', 'Animal Handling', 'wis'),
    'guard':               ('spear', 'shield', 'Intimidation', 'con'),
    'guild beggar':        ('sling', 'Crutches', 'Deception', 'cha'),
    'healer':              ('club', 'Vial of holy water', 'Medicine', 'wis'),
    'hedge witch':         ('magic stone', 'Healing herbs', 'Nature', 'wis'),
    'herbalist':           (tool, 'Herbs', 'Nature', 'int'),
    'herder':              ('staff', 'Herding dog', 'Animal Handling', None),
    'hunter':              ('shortbow', 'Deer pelt', 'Stealth', 'dex'),
    'indentured servant':  ('staff', stuff, 'Athletics', None),
    'innkeeper':           ('club', stuff, 'Insight', 'cha'),
    'jester':              ('prestidigitation', 'Silk clothes', 'Performance', 'cha'),
    'jeweler':             ('fine dagger', 'Gem worth 20 gp', 'Perception', 'dex'),
    'locksmith':           ('dagger', 'Fine tools', 'Sleight of Hand', 'dex'),
    'mason':               (tool, stuff, 'Athletics', 'str'),
    'mayor':               ('mace', stuff, 'Persuasion', 'wis'),
    'mercenary':           ('longsword', 'Hide armor', 'Survival', 'str'),
    'merchant':            ('dagger', stuff, 'Persuasion', 'cha'),
    'messenger':           ('spear', stuff, 'Survival', 'con'),
    'miller':              ('short sword', 'Flour - 1 lb', 'Athletics', 'str'),
    'miner':               ('pick', 'Lantern', 'Athletics', 'con'),
    'minstrel':            ('dagger', 'Lyre', 'Performance', 'cha'),
    'noble':               ('longsword', 'Gold signet ring', 'History', 'int'),
    'orphan':              ('club', 'Rag doll', 'Stealth', None),
    'outlaw':              ('short sword', 'Leather tunic', 'Deception', None),
    'porter':              ('club', stuff, 'Athletics', 'str'),
    'rat catcher':         ('club', 'Small dog', 'Animal Handling', 'dex'),
    'sage':                (cantrip, 'Notebook and pencils', 'History', 'int'),
    'scholar':             (cantrip, stuff, 'Arcana', 'int'),
    'scribe':              ('darts', 'Parchment, Quill pen and ink', 'Investigation', 'int'),
    'shaman':              (cantrip, 'Herbs', 'Religion', 'wis'),
    'smuggler':            ('sling', 'Waterproof sack', 'Stealth', 'dex'),
    'squire':              ('short sword', 'Iron helmet', 'Athletics', 'str'),
    'tanner':              ('knife', 'Waterproof bag', 'Athletics', None),
    'tavern keeper':       ('club', 'jug of ale', 'Insight', 'cha')
    'teamster':            ('whip', stuff, 'Animal Handling', 'str'),
    'trader':              ('short sword', '20 sp', 'Persuasion', 'cha'),
    'trapper':             ('sling', 'Badger pelt', 'Survival', 'wis'),
    'urchin':              ('stick', 'Begging bowl', 'Sleight of Hand', 'dex'),
    'vagrant':             ('club', 'Begging bowl', 'Deception', None),
    'wainwright':          (tool, 'Pushcart', 'Athletics', 'dex'),
    'weaver':              ('dagger', 'Fine suit of clothes', 'Perception', 'dex'),
    'wizard\'s apprentice':(cantrip, 'Spellbook', 'Arcana', 'int'),
    'woodcutter':          ('axe', 'Bundle of wood', 'Athletics', 'dex')
}

armor_values = {
    'Iron helmet'   : 11,
    'Padded armor'  : 11,
    'Shield'        : 12,
    'Hide armor'    : 12,
    'Leather tunic' : 11,
}

default_weapon = {'damage': '1d4', 'weight': '1lb', 'properties': 'improvised, thrown(20/60)'}
weapon_stats = {
    'axe'              : {'damage': '1d6 s', 'weight': '4', 'properties': 'versatile (1d8)'},
    'club'             : {'damage': '1d4 b', 'weight': '2', 'properties': 'light'},
    'dagger'           : {'damage': '1d4 p', 'weight': '1', 'properties': 'finesse, light, thrown(20/60)'},
    'darts'            : {'damage': '1d4 p', 'weight': '1/4', 'properties': 'finesse, thrown(20/60)'},
    'flail'            : {'damage': '1d6 b', 'weight': '2', 'properties': ''},
    'hammer'           : {'damage': '1d4 b', 'weight': '2', 'properties': 'light, thrown(20/60)'},
    'knife'            : {'damage': '1d4 s', 'weight': '1', 'properties': 'finesse, light, thrown(10/60)'},
    'longbow'          : {'damage': '1d8 p', 'weight': '2', 'properties': 'range(150/600), heavy, two-handed'},
    'longsword'        : {'damage': '1d8 s', 'weight': '3', 'properties': 'versatile (1d10)'},
    'mace'             : {'damage': '1d6 b', 'weight': '4', 'properties': ''},
    'pitchfork'        : {'damage': '1d6 p', 'weight': '5', 'properties': 'versatile (1d8), thrown(10/40)'},
    'scythe'           : {'damage': '1d6 s', 'weight': '3', 'properties': 'two-handed'},
    'shortbow'         : {'damage': '1d6 p', 'weight': '2', 'properties': 'range(80/320), two-handed'},
    'short sword'      : {'damage': '1d6 p', 'weight': '2', 'properties': 'finesse, light'},
    'sickle'           : {'damage': '1d4 s', 'weight': '2', 'properties': 'light'},
    'sling'            : {'damage': '1d4 b', 'weight': '-', 'properties': 'range(30/120)'},
    'spear'            : {'damage': '1d6 p', 'weight': '3', 'properties': 'thrown(20/60), versatile(1d8)'},
    'staff'            : {'damage': '1d6 b', 'weight': '4', 'properties': 'versatile (1d8)'},
    'whip'             : {'damage': '1d4 s', 'weight': '3', 'properties': 'finesse, reach'},
    'acid splash'      : {'damage': '1d6',   'weight': '-', 'properties': 'range: 60, 1-2 creatures within 5 feet, Dex save'},
    'blade ward'       : {'damage': '-',     'weight': '-', 'properties': 'resistance vs bludgeoning, piercing and slashing damage'},
    'fire bolt'        : {'damage': '1d10',  'weight': '-', 'properties': 'range 120, Attack roll'},
    'guidance'         : {'damage': '-',     'weight': '-', 'properties': 'Touched creature adds 1d4 to one ability check of its choice'},
    'light'            : {'damage': '-',     'weight': '-', 'properties': 'Touched object sheds light in 20\' and dim light another 20\''},
    'magic stone'      : {'damage': '1d6 b', 'weight': '-', 'properties': 'range: 60, 3 pebbles, use spellcasting mod for attack and damage'},
    'prestidigitation' : {'damage': '-',     'weight': '-', 'properties': 'Create effects, illusions and small alterations.'},
    'produce flame'    : {'damage': '1d8 f', 'weight': '-', 'properties': 'range: 30, attack roll'},
    'ray of frost'     : {'damage': '1d8 b', 'weight': '-', 'properties': 'range: 60, Attack roll, -10 feet movement on hit'},
    'shocking grasp'   : {'damage': '1d8 e', 'weight': '-', 'properties': 'touch attack (advantage if target is in metal armor)'},
    'true strike'      : {'damage': '-',     'weight': '-', 'properties': 'range: 30, advantage on next turn, first attack vs target'},

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
    'aarakocra',
    'dragonborn',
    'dwarf',
    'elf',
    'gnome',
    'half-elf',
    'half-orc',
    'halfling',
    'human',
    'kenku',
    'kobold',
    'tiefling',
)

race_traits = {
    'aarakocra'    : {'languages': 'Common, Aarakocra, Auran',  'size': 'Medium', 'speed':30, 'skin': 'feathers'  },
    'aasimar'      : {'languages': 'Common, Celestial',         'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'air Genasi'   : {'languages': 'Common, Primordial',        'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'bugbear'      : {'languages': 'Common, Goblin',            'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'centaur'      : {'languages': 'Common, Sylvan',            'size': 'Medium', 'speed':40, 'skin': 'fur'       },
    'changeling'   : {'languages': 'Common, 2',                 'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'dragonborn'   : {'languages': 'Common, Draconic',          'size': 'Medium', 'speed':30, 'skin': 'scales'    },
    'dwarf'        : {'languages': 'Common, Dwarf',             'size': 'Medium', 'speed':25, 'skin': 'fur'       },
    'earth Genasi' : {'languages': 'Common, Primordial',        'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'eladrin'      : {'languages': 'Common, Sylvan',            'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'elf'          : {'languages': 'Common, Elvish',            'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'fairy'        : {'languages': 'Common, Sylvan',            'size': 'Small' , 'speed':30, 'skin': 'fur'       },
    'firbolg'      : {'languages': 'Common, Elvish, Giant',     'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'fire genasi'  : {'languages': 'Common, Primordial',        'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'githyanki'    : {'languages': 'Common, Gith',              'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'githzerai'    : {'languages': 'Common, Gith',              'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'gnome'        : {'languages': 'Common, Gnomish',           'size': 'Small' , 'speed':25, 'skin': 'fur'       },
    'goblin'       : {'languages': 'Common, Goblin',            'size': 'Small' , 'speed':30, 'skin': 'fur'       },
    'goliath'      : {'languages': 'Common, Giant',             'size': 'Medium', 'speed':30, 'skin': 'skin'      },
    'halfling'     : {'languages': 'Common, Halfling',          'size': 'Small' , 'speed':25, 'skin': 'fur'       },
    'half-elf'     : {'languages': 'Common, Elvish',            'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'half-orc'     : {'languages': 'Common, Orc',               'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'harengon'     : {'languages': 'Common, 1'  ,               'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'hobgoblin'    : {'languages': 'Common, Goblin',            'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'human'        : {'languages': 'Common, 1',                 'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'kalashtar'    : {'languages': 'Common, Quori, 1',          'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'kenku'        : {'languages': 'Common, Auran ',            'size': 'Medium', 'speed':30, 'skin': 'feathers'  },
    'kobold'       : {'languages': 'Common, Draconic',          'size': 'Small' , 'speed':30, 'skin': 'scales'    },
    'lizardfolk'   : {'languages': 'Common, Draconic',          'size': 'Medium', 'speed':30, 'skin': 'scales'    },
    'loxodon'      : {'languages': 'Common, Loxodon',           'size': 'Medium', 'speed':30, 'skin': 'skin'      },
    'minotaur'     : {'languages': 'Common, Minotaur',          'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'orc'          : {'languages': 'Common, Orc',               'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'shifter'      : {'languages': 'Common',                    'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'simic hybrid' : {'languages': 'Common, Elvish/Vedalken',   'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'tabaxi'       : {'languages': 'Common, 1',                 'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'tiefling'     : {'languages': 'Common, Infernal',          'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'tortle'       : {'languages': 'Common, Aquan',             'size': 'Medium', 'speed':30, 'skin': 'skin'      },
    'triton'       : {'languages': 'Common, Aquan',             'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'vedalken'     : {'languages': 'Common, Vedalken, 1',       'size': 'Medium', 'speed':30, 'skin': 'mechanical'},
    'warforged'    : {'languages': 'Common',                    'size': 'Medium', 'speed':30, 'skin': 'fur'       },
    'water genasi' : {'languages': 'Common, Primordial',        'size': 'Medium', 'speed':30, 'skin': 'other'     },
    'yuan-Ti'      : {'languages': 'Common, Abyssal, Draconic', 'size': 'Medium', 'speed':30, 'skin': 'scales'    },
}

def description(race):
    pers = random.choice(personality)
    article = 'an' if pers[0] in 'aeiou' else 'a'

    detail_option = random.choice(details)
    detail = detail_option.get(race_traits[race]['skin'], detail_option['default'])

    return f'{article} {pers}, {random.choice(appearance)} '\
        f'{race} with {detail} and is wearing '\
        f'{random.choice(clothing)} clothes.'

    
def statblock(main=None):
    vals = [round(random.gammavariate(10, .4))+6 for x in range(6)]
    labels = ['str', 'dex', 'con', 'int', 'wis', 'cha']
    stats = dict(zip(labels, [{'index':i} for i in range(6)]))
    if main and main in labels:
        stats[main]['val'] = max(vals)
        vals.remove(max(vals))
        labels.remove(main)

    for label in labels:
        val = vals.pop()
        stats[label]['val'] = val
    return stats

proficiency_bonus = 1
score_mod = lambda x: x//2 - 5
# don't forget '{0:+}'.format(value) to get leading +

def character(races=None, classes=None ):
    if races is None:
        races = available_races
    if classes is None:
        classes = list(jobs.keys())
    char = {}
    job = random.choice(classes)
    (weapon, gear, prof, stat) = jobs[job]
    stats = statblock(main=stat)
    for ability in stats.keys():
        mod = score_mod(stats[ability]['val'])
        stats[ability]['mod'] = mod
        stats[ability]['modstr'] = f'{mod:+}'

    char['abilities'] = stats

    if isinstance(weapon, tuple):
        weapon = random.choice(weapon)
    
    if isinstance(gear, tuple):
        gear = random.choice(gear)

    race = random.choice(races)
    char['description'] = description(race)
    char['race'] = race
    char['size'] = race_traits[race]['size']
    char['speed'] = race_traits[race]['speed']
    char['job'] = job
    char['weapon'] = weapon
    wstats = dict(weapon_stats.get(weapon, default_weapon))

    weapon_ability = 'str'
    if weapon in cantrip:
        weapon_ability = 'int' #todo fix for caster types
    elif weapon in ranged:
        weapon_ability = 'dex'

    if 'finesse' in wstats['properties']:
        atk_bonus = max(stats['str']['mod'], stats['dex']['mod']) + proficiency_bonus
    else:
        atk_bonus = stats[weapon_ability]['mod'] + proficiency_bonus

    wstats['atk_bonus'] = f'{atk_bonus:+}'
    wstats['name'] = weapon
    attacks = [wstats]


    if wstats['damage'] == '-':
        wstats2 = dict(weapon_stats['club'])
        wstats2['name'] = 'club'
        wstats2['atk_bonus'] = f'{(stats["str"]["mod"] + proficiency_bonus):+}'
        attacks.append(wstats2)
        char['weapon'] = 'club'
    elif 'thrown' in wstats['properties']:
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
