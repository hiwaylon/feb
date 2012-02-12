"""The factory manager holds factory objects. Factory objects are any object
that responds to a `create()` method that accepts a configuration dictionary. 
Factories are added to the FactoryManager via `register_factory()` and
retrieved with `get_factory()`. As a convience, `create()` can be called with 
a type name and configuration and the factory manager will look up the
appropriate factory, call `create()` on it and return the product. 

Example usage::

    # define a method to register factories in the factory manager
    def register_factories(factory_manager):
        factory_manager.register_factory("wibble", WibbleFactory())

    # create the factory manager and register factories
    factory_manager = FactoryMananger()
    register_factories(factory_manager)

    # create stuff
    configuration = {
        "size": "small"}
    small_wibbles = factory_manager.create("wibble", configuration)

    # or get the factory for later
    wibble_factory = factory_manager.get_factory("wibble")

"""

import logging


class FactoryManager(object):
    """The factory manager is responsible for collecting binding tags and creating
    objects with the bound factories.

    """
    def __init__(self):
        self._factories = {}

    def register(self, tag, factory):
        """Associate a tag with a factory or type so it can be created later.

        """
        binding = self._factories.get(tag)
        if binding:
            _report_error(
                "Tag (%s) already bound to type (%s)." % (tag,
                binding.__class__))
                
        logging.debug("Binding tag (%s) to type (%s).", tag,
            factory.__name__)
        self._factories[tag] = factory

    def create(self, tag, *args, **kwargs):
        """Create a type identified by tag."""
        factory = self._factories.get(tag)
        if not factory:
            _report_error("No binding exists for tag (%s)" % (tag))
        
        logging.debug(
            "Creating (%s) from factory (%s).", tag, factory.__name__)
        if hasattr(factory, "create"):
            return factory.create(*args, **kwargs)
        return factory(*args, **kwargs)

# TODO: Make this cool and re-usable utility - _report("blah", NameError)
def _report_error(message):
    logging.warning(message)
    raise NameError(message)
