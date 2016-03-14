from nltk import pos_tag, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import copy

def extract_cooking_methods(input_steps, title):
    steps = copy.deepcopy(input_steps)
    steps.append(title)
    tk_steps = [pos_tag(word_tokenize(w.lower())) for w in steps]

    methods = []
    for step in tk_steps:
        # methods += [wordnet_lemmatizer.lemmatize(w, pos='v').encode('ascii', 'ignore') for (w, pos) in step if 'VB' in pos]
        methods += [w.encode('ascii', 'ignore') for (w, pos) in step if 'VB' in pos]

    for step in steps:
        if 'preheat' in step:
            methods += ['preheat', 'preheating']
        if 'microwav' in step:
            methods += ['microwave', 'microwaving']
        if 'place' in step:
            methods.append('place')
        if 'form' in step:
            methods.append('form')
        if 'sprinkle' in step:
            methods.append('sprinkle')

    wordnet_lemmatizer = WordNetLemmatizer()
    discard = ['be', 'use', 'need', 'should', 'allow', 'pink', 'turn', 'reserve']
    methods =  [m for m in methods if wordnet_lemmatizer.lemmatize(m, pos='v') not in discard and len(m) > 2]
    stems = [wordnet_lemmatizer.lemmatize(w, pos='v') for w in methods]
    gerunds = [w[:-1] + 'ing' for w in stems if w[-1] == 'e']
    gerunds +=  [w + 'ing' for w in stems if w[-1] != 'e']
    methods = list(set(methods + stems + gerunds))
    return methods


# print extract_cooking_methods(['Season lamb shoulder chops with salt and black pepper.',
# 'Heat oil in a large heavy skillet over high heat. Working in batches, cook lamb shoulder chops until browned on both sides, 3 to 5 minutes per side. Transfer chops to a stock pot.',
# 'Cook and stir onion with a pinch of salt in the same skillet over medium heat until slightly softened and edges are browning, about 5 minutes. Stir butter into onion until melted; add flour and stir until onions are coated, about 1 minute.',
# 'Pour stock into onion mixture; bring to a boil, add rosemary, and stir until mixture thickens, 5 to 10 minutes.',
# 'Stir carrots and celery into pot with lamb shoulder chops and pour chicken stock mixture over the top. Add water as needed to cover meat completely. Bring mixture to a simmer, reduce heat to low, cover the pot with a lid, and cook until meat is almost falling off the bone, about 1 1/2 hours.',
# 'Transfer meat to a plate. Stir potatoes into stew and return meat to stew, placing on top of vegetables. Simmer, covered, until potatoes are tender and meat is falling off the bone, about 30 minutes.',
# 'Transfer meat to a plate using a slotted spoon. Bring stew to a boil and cook, skimming off fat, until stew is reduced and thick, 10 to 12 minutes.',
# 'Remove meat from bones; discard bones and any pieces of fat. Stir meat back into stew. Stir green onions into stew and season with salt and pepper to taste.'], "Chef John's Irish Stew")
