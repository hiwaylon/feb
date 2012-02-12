"""Test the entity factory."""

import unittest

import feb
from feb import entity_factory
from feb.testing.helpers import StubBehavior


class StubConfigurationSource(feb.ConfigurationSource):
    def fetch(self, tag):
        return {
            "behaviors": [{
                "tag": "stub"
            }]
        }


class TestEntityFactory(unittest.TestCase):
    def setUp(self):
        super(TestEntityFactory, self).setUp()
        self._capture = {}
        self._original_register_behaviors = \
            entity_factory._register_behavior_factories

        def stub_behavior_registrar(factory_manager):
            factory_manager.register("stub", self._make_stub_behavior)
            return StubBehavior
        
        entity_factory._register_behavior_factories = stub_behavior_registrar

    def tearDown(self):
        super(TestEntityFactory, self).tearDown()
        entity_factory._register_behavior_factories = \
            self._original_register_behaviors

    def test_entity_construction(self):
        """It should create an entity from the given tag.""" 
        configuration_source = StubConfigurationSource()
        factory = feb.EntityFactory(configuration_source=configuration_source)
        entity = factory.create("stub_entity")
        self.assertIsNotNone(entity)

    def test_created_entity_response_to_event(self):
        """The new entity should respond to the given event."""
        factory = feb.EntityFactory(
            configuration_source=StubConfigurationSource())
        entity = factory.create("stub_entity")
        entity.stub()
        self.assertTrue(self._capture["called"])

    def _make_stub_behavior(self):
        stub_behavior = StubBehavior(self._capture)
        return stub_behavior
