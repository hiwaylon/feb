"""Helper module for testing FEB objects."""

from feb import behavior


class StubBehavior(behavior.Behavior):
    def __init__(self, capture=dict()):
        self.capture = capture

    def execute(self):
        self.capture["called"] = True
