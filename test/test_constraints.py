#!/usr/bin/env python

import yaml
import unittest

from testscenarios import TestWithScenarios

from constraints.constraints import Constraints

directory = {}
groups = {}

directory_file=open('test/directory.yaml')
directory=yaml.load(directory_file)
groups_file=open('test/groups.yaml')
groups=yaml.load(groups_file)

scenarios = []

for test_name, test_data in groups.items():
    if 'exceptions' not in test_data:
        test_data['exceptions'] = None
    scenarios.append((test_name, test_data))

class TestConstraintsWithSampleDirectory(TestWithScenarios):

    scenarios = scenarios

    def setUp(self):
        self.groups = groups
        self.directory = directory
        self.constrainer = Constraints(self.directory)

    def test_group(self):
        generated_members = self.constrainer.get_members(self.criteria,
                self.exceptions)
        self.assertItemsEqual(self.members, generated_members)


class TestConstraints(unittest.TestCase):

    def setUp(self):
        self.groups = groups
        self.directory = directory
        self.constrainer = Constraints(self.directory)
