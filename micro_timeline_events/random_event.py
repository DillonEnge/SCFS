from .base_event import BaseEvent
from lib import write_trait_tree

class RandomEvent(BaseEvent):
    def step(instance, state):
        print("Taking random step")