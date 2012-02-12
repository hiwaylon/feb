"""Test the Entity class."""

import logging
import unittest

from feb import behavior
from feb import entity
from feb.testing.helpers import StubBehavior


class TestEntity(unittest.TestCase):
    def test_it_should_map_events_to_methods(self):
        stub_behavior = StubBehavior()

        # Maps "do_it" to stub_behavior, i.e. blah.do_it() -->
        # stub_behavior.execute().
        stub_behaviors = {"do_it": stub_behavior}
        stub_entity = entity.Entity(stub_behaviors)
        stub_entity.do_it()

        self.assertTrue(stub_behavior.capture["called"])
