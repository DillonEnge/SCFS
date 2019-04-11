from .base_event import BaseEvent

class AgeEvent(BaseEvent):
    @staticmethod
    def step(state):
        for person in state:
            trait_tree = person.get_trait_tree()
            trait_tree['age'] += 1
            person.write_trait_tree(trait_tree)