import random
from .base_event import BaseEvent
from lib import get_and_shuffle_trait_tree

class RandomEvent(BaseEvent):
    @staticmethod
    def step(state):
        for person in state:
            trait_tree = person.get_trait_tree()
            traits = get_and_shuffle_trait_tree(trait_tree['traits'])
            new_vals = RandomEvent._randomize_values(trait_tree, traits)
            person.write_trait_tree(new_vals)

    @staticmethod
    def _randomize_values(trait_tree, traits, subtraits = [], iteration = -1):
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
                RandomEvent._randomize_values(trait_tree, traits, subtraits=get_and_shuffle_trait_tree(trait_tree['traits'][traits[i]]['subtraits']), iteration=i)
            else:
                trait_tree['traits'][traits[iteration]]['subtraits'][subtraits[i]] = float(random_percentage)/100

            percentage_remaining = percentage_remaining - random_percentage

        return trait_tree