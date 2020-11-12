class Event:
    def __init__(self):
        self.events = {}

    def on(self, name, callback):
        self.events[name] = callback

    def clear_events(self):
        self.events = {}
