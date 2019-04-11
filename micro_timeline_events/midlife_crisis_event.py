from .base_event import BaseEvent

class MidlifeCrisisEvent(BaseEvent):
    @staticmethod
    def step(state):
        for person in state:
            traits = person.get_trait_tree()
            if traits["age"] == 45:
                traits["traits"]["neuroticism"]["subtraits"]["Self-consciousness"] = 50
                traits["traits"]["neuroticism"]["subtraits"]["adventurousness"] = 50
                traits["traits"]["conscientiousness"]["subtraits"]["cautiousness"] = 0
                person.write_trait_tree(traits)