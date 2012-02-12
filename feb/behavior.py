"""A Behavior responds to stimulus with it's ``execute`` method. Beaviors are
collected by Entities.

"""

import abc

class Behavior(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """Behaviors are required to implemnt the execute method. In this method the behavior performs its duty."""
        pass
