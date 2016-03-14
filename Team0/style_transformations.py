to_asian = {
    'noodles': {
        'cup': [1, 'cup', 'rice'],
        'other': 'rice noodles'
    },
    'salt': {
        'teaspoon': [2, 'tablespoon', 'soy sauce'],
        'tablespoon': [4, 'tablespoon', 'soy sauce']
    },
    'mozerella cheese': {
        'cup': [1, '', 'poached or soft-boiled egg']
    },
    'cheddar cheese': {
        'cup': [1, '', 'poached or soft-boiled egg']
    },
    'parmesan cheese': {
        'cup': [1, '', 'poached or soft-boiled egg']
    },
    'cheese': {
        'cup': [1, '', 'poached or soft-boiled egg']
    },
    'sugar': {
        'tablespoon': [1, 'tablespoon', 'teriyaki sauce'],
        'teaspoon': [1, 'teaspoon', 'teriyaki sauce'],
        'cup': [2, 'tablespoon', 'hoisin sauce']
    },

    'worcestershire sauce': ['hoisin sauce', True],
    'sauce': ['hoisin sauce', False],

    'cilantro': ['basil', True],
    'parsley': ['basil', True],
    'milk': ['coconut milk', False],

    'olive oil': ['sesame oil', False],
    'vegetable oil': ['sesame oil', False],
    'oil': ['sesame oil', False],

    'brussels sprouts': ['bok choy', True],
    'potatoes': ['drained 5 oz. can of water chestnuts', False],
    'potato': ['drained 5 oz. can water chestnuts', False],
    'artichokes': ['drained 5 oz. can of bamboo shoots', True],
    'artichoke hearts': ['bamboo shoots', True],
    'artichoke': ['drained 5 oz. can bamboo shoots', False],

    'cumin': ['ground ginger', True],
    'paprika': {
        'teaspoon': [1, 'tablespoon', 'garlic chili sauce'],
    },

    'oregano': {
        'teaspoon': [.5, 'teaspoon', 'ground ginger'],
        'tablespoon': [1, 'teaspoon', 'ground ginger'],
        'pinch': [1, 'pinch', 'ground ginger']
    },
    'horseradish': ['minced ginger', False],
    'pickles': ['pickled ginger', False],
    'rosemary': ['basil', True],
    'sour cream': ['coconut milk', False],
    'cream': ['coconut milk', False],
}

to_mex = {
    'parsley': ['cilantro', True],
    'basil': ['cilantro', True],
    'flour tortillas': ['corn tortillas', True],
    'bread': {
        'slice': [1, '', 'corn tortilla'],
        'slices': [1, '', 'corn tortilla'],
        'other': 'corn tortillas'
    },
    'mushrooms': ['green peppers', False],
    'parmesan cheese': ['queso fresco', True],
    'lemon': ['lime', True],
    'lemon juice': ['lice juice', True],
    'coriander': ['paprika', True],
    'turmeric': ['paprika', True],
    'teriyaki sauce': ['black mole sauce', True],
    'ginger': ['habanero', True],
    'ginger root': ['habanero', True],
    'noodles': {
        'cup': [1, 'cup', 'rice'],
        'other': 'rice noodles'
    },
    'soy sauce': {
        'tablespoon': [.25, 'teaspoon', 'salt'],
        'teaspoon': [.5, 'teaspoon', 'salt']
    },
    'olives': ['jalapenos', False],
    'worcestor sauce': ['cholula sauce', False],
    'sauce': ['salsa', False],
    # corn, beans red peppers
}

to_veggie = {
    'pork': ['red peppers', True],
    'chops': ['red bell peppers', False],
    'loin': ['portabello mushroom', False],
    'ribs': ['portabello mushroom', False],

    'beef': ['black beans', True],
    'ground beef': ['black beans', True],
    'meat': ['mushrooms', False],

    'chicken': ['tofu', True],
    'breasts': ['tofu', False],
    'chicken breasts': ['tofu', False],
    'wings': ['tofu', False],
    'thighs': ['tofu', False],

    'tripe': ['tofu strips', False],
    'sausage': ['tofu', True],
    'dog': ['tofu', True],
    'hot dog': ['tofu', True],
    'bratwurst': ['tofu', True],
    'bacon': ['mushrooms', False],
}

to_vegan = {
    'milk': ['coconut milk', False],
    'cheese': ['applesauce', False],
    'yogurt': ['almond milk', True],
    'sour cream': ['almond milk', True],
    'cream': ['almond milk', True],
    'egg': {
        '': [.5, '', 'mashed up bananas'],
        'other': '1 mashed up banana'
    },
    'eggs': {
        '': [.5, '', 'mashed up bananas'],
        'other': '1 mashed up banana'
    },
    'bread': ['vegan bread', True],
    'buns': ['vegan buns', True],
    'bun': ['vegan bun', True]
}
