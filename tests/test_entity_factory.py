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

        # Register stub behaviors with factory to be passed to EntityFactory.
        self._behavior_factory = feb.FactoryManager()
        self._behavior_factory.register("stub", self._make_stub_behavior)

    def tearDown(self):
        super(TestEntityFactory, self).tearDown()

    def test_entity_construction(self):
        """It should create an entity from the given tag.""" 
        configuration_source = StubConfigurationSource()
        factory = feb.EntityFactory(
            configuration_source=configuration_source,
            behavior_factory=self._behavior_factory)
        entity = factory.create("stub_entity")
        self.assertIsNotNone(entity)

    def test_created_entity_response_to_event(self):
        """The new entity should respond to the given event."""
        factory = feb.EntityFactory(
            configuration_source=StubConfigurationSource(),
            behavior_factory=self._behavior_factory)
        entity = factory.create("stub_entity")
        entity.stub()
        self.assertTrue(self._capture["called"])

    def _make_stub_behavior(self):
        stub_behavior = StubBehavior(self._capture)
        return stub_behavior
