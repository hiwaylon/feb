"""A Entity is an object which contains a collection of Behaviors. Behaviors
respond to events, i.e. method calls on the Entity.

"""

import logging

from feb import behavior


class Entity(object):
    def __init__(self, behaviors):
        logging.debug("Initializing Entity with behaviors (%s).", behaviors)
        self._behaviors = behaviors

    def __getattr__(self, name):
        """Try to use a ``Behavior`` before allowing normal attribute access."""
        logging.debug("Searching for (%s) in Behaviors (%s).", name, self._behaviors)
        behavior = self._behaviors.get(name)
        if behavior:
            logging.debug("Found Behavior (%s).", behavior.__class__)
            # TODO: args and kwargs into execute?
            return behavior.execute
        raise AttributeError("(%s) was not found as a normal attribute, method or behavior." % (name))
