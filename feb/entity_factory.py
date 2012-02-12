"""The EntityFactory is responsible for creating Entites from configurations.

"""

import logging

from entity import Entity
from factory_manager import FactoryManager


class EntityFactory(object):
    def __init__(self, configuration_source):
        self._configuration_source = configuration_source

    def create(self, entity_tag):
        
        entity_configuration = self._configuration_source.fetch(entity_tag)
        
        behavior_configurations = entity_configuration.get("behaviors")
        if not behavior_configurations:
            _configuration_error(
                "Entity configuration (%s) requires behaviors attribute." % (
                entity_tag))

        behaviors = {}
        for configuration in behavior_configurations:
            behavior_tag = configuration.get("tag")
            if not behavior_tag:
                _configuration_error(
                    "Behavior configuration (%s) requires a tag attribute." %
                    (configuration))
            
            # TODO: FM registerations stuff can probably be moved to module 
            # scope level when EntityFactory is broken out.
            factory_manager = FactoryManager()
            _register_behavior_factories(factory_manager)
            behavior = factory_manager.create(behavior_tag)
            behaviors[behavior_tag] = behavior

        return Entity(behaviors=behaviors)


def _register_behavior_factories(factory_manager):
    print "nosh"
    # TODO: REgister some factories.
    return factory_manager

# TODO: make ConfigurationError a re-usable utility in library
class ConfigurationError(Exception):
    pass


def _configuration_error(message):
    logging.warning(message)
    raise ConfigurationError(message)
