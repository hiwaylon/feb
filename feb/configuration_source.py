"""Defines the interface for configuration sources.

Configuration sources fetch configuration dictionaries from sources such as
YAML files or a database.

"""

import abc


class ConfigurationSource(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def fetch(self, tag):
        """A ConfigurationSource implement this method to return the
        configuration identified by ``tag``.

        """
        pass
