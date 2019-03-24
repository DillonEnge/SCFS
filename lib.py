# lib.py: Lib file responsible for the heavy lifting of stat generation and json manipulation.

import json, random
from scipy.stats import truncnorm

# Writes the initial default trait_tree object to a json file
def generate_initial_json():
    with open('trait_tree.json', 'w') as outfile:
        json.dump(
            {
                'value': 0,
                'traits':
                    {
                        'agreeableness': {
                            'value': 0,
                            'subtraits': {
                                'trust': 0,
                                'morality': 0,
                                'altruism': 0,
                                'cooperation': 0,
                                'modesty': 0,
                                'sympathy': 0
                            }
                        },
                        'conscientiousness': {
                            'value': 0,
                            'subtraits': {
                                'self-efficacy': 0,
                                'orderliness': 0,
                                'dutifulness': 0,
                                'achievement-striving': 0,
                                'self-discipline': 0,
                                'cautiousness': 0
                            }
                        },
                        'extraversion': {
                            'value': 0,
                            'subtraits': {
                                'friendliness': 0,
                                'gregariousness': 0,
                                'assertiveness': 0,
                                'activity level': 0,
                                'excitement-seeking': 0,
                                'cheerfulness': 0
                            }
                        },
                        'neuroticism': {
                            'value': 0,
                            'subtraits': {
                                'Anxiety': 0,
                                'Anger': 0,
                                'Depression': 0,
                                'Self-consciousness': 0,
                                'Immoderation': 0,
                                'Vulnerability': 0
                            }
                        },
                        'openness': {
                            'value': 0,
                            'subtraits': {
                                'imagination': 0,
                                'artistic interests': 0,
                                'emotionality': 0,
                                'adventurousness': 0,
                                'intellect': 0,
                                'liberalism': 0
                            }
                        }
                }
            }, outfile, indent=4)

# Gets the trait_tree object from a json file and returns it
def get_trait_tree():
    trait_tree = {}
    with open('trait_tree.json') as trait_tree_file:
        trait_tree = json.load(trait_tree_file)

    return trait_tree

# Writes the trait_tree object it receives to a json file
def write_trait_tree(trait_tree):
    with open('trait_tree.json', 'w') as outfile:
        json.dump(trait_tree, outfile, indent=4)

# Will eventually take 'age' as a param to signify max percentage remaining
def fill_random_sub_values():
    trait_tree = get_trait_tree()
    traits = get_and_shuffle_trait_tree(trait_tree['traits'])

    iterate_value_generation(trait_tree, traits)

# Will eventually be used in the context of physical/mental attribute generation that can be estimated using a normally distributed model
# Example usage:
#   bwg = get_truncated_normal(mean=3.25, sd=1, low=2.5, upp=4)
#   weight = bwg.rvs()
def get_truncated_normal(mean=3.25, sd=1, low=2.5, upp=4):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

# Takes in a trait tree level (ie. trait_tree['traits']), randomly shuffles the internal keys, then returns the shuffled array
def get_and_shuffle_trait_tree(trait_tree_level):
    traits = []

    for key in trait_tree_level:
        traits.append(key)

    random.shuffle(traits)

    return traits

# Recursively iterates through multiple levels of the received trait_tree object, firstly generating initial 'traits' level -->
# values randomly using a rudimentary conditional check to add up to the default percentage remaining, after each trait's value is -->
# generated the function calls itself to iterate this time through all of that traits subtraits, generating a random value for -->
# the subtrait using the same random method as before. All of this ends up intuitively summing up from the lowest level upwards in chunks -->
# resulting in a balanced trait presence percentage being reflected for every trait available.
def iterate_value_generation(trait_tree, traits, subtraits = [], iteration = -1):
    percentage_remaining = None
    selected_traits = None

    if len(subtraits) == 0:
        selected_traits = traits
        percentage_remaining = 100
    else:
        selected_traits = subtraits
        percentage_remaining = int(trait_tree['traits'][traits[iteration]]['value'] * 100)

    for i in range(len(selected_traits)):
        random_percentage = 0

        if i == len(selected_traits) - 1:
            random_percentage = percentage_remaining
        elif i == 0:
            if int(percentage_remaining/4) != 0 or int(percentage_remaining/2) != 0:
                random_percentage = random.randrange(int(percentage_remaining/4), int(percentage_remaining/2))
        elif i == 1:
            if int(percentage_remaining/2) != 0:
                random_percentage = random.randrange(int(percentage_remaining/2), percentage_remaining)
        else:
            if percentage_remaining != 0:
                random_percentage = random.randrange(0, percentage_remaining)

        if len(subtraits) == 0:
            trait_tree['traits'][traits[i]]['value'] = float(random_percentage)/100
            iterate_value_generation(trait_tree, traits, get_and_shuffle_trait_tree(trait_tree['traits'][traits[i]]['subtraits']), i)
        else:
            trait_tree['traits'][traits[iteration]]['subtraits'][subtraits[i]] = float(random_percentage)/100

        percentage_remaining = percentage_remaining - random_percentage

    write_trait_tree(trait_tree)
