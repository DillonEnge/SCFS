from .base_event import BaseEvent

class IncrementEvent(BaseEvent):
    def step(instance, state):
        print("Taking increment step")