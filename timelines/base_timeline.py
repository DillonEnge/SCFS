class BaseTimeline:
    def __init__(self):
        self.events = []
        self.instance = 0
        print("Initalizing BaseTimeline")

    def register_event(self, event):
        print(f'Registering event : {type(event).__name__}')
        self.events.append(event)
 
    def step(self, state):
        for event in self.events:
            event.step(state)
        self.instance += 1