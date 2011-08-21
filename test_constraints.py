#!/usr/bin/env python

import yaml
import unittest2

from constraints import Constraints

directory = {}
groups = {}

directory_file=open('tests/directory.yaml')
directory=yaml.load(directory_file)
groups_file=open('tests/groups.yaml')
groups=yaml.load(groups_file)

def generate_group_membership_checker(criteria, expected_members):
    def check_group_membership(self):
        generated_members = self.constrainer.get_members(criteria=criteria,
                directory=self.directory)
        self.assertItemsEqual(expected_members, generated_members)
    return check_group_membership

class TestConstraints(unittest2.TestCase):

    def setUp(self):
        self.constrainer = Constraints()
        self.groups = groups
        self.directory = directory

    def test_members_for_attr(self):
        attr = 'location'
        values = ['Free Cities', 'Kings Landing']
        expected_members = ['robert', 'cersei', 'tyrion', 'viserys', 'daenrys']
        generated_members = self.constrainer._get_members_for_attr(
                attr, values, self.directory)
        self.assertItemsEqual(expected_members, generated_members)

    def test_members_for_criterion(self):
        criterion = { 'location': ['Winterfell'], 'department': ['Tully'] }
        expected_members = ['catelyn']
        generated_members = self.constrainer._get_members_for_criterion(
                criterion, self.directory)
        self.assertItemsEqual(expected_members, generated_members)

for test_name, test_data in groups.items():
    test = generate_group_membership_checker(test_data['criteria'],
            test_data['members'])
    setattr(TestConstraints, test_name, test)

test_cases = [TestConstraints]

def load_tests(loader, tests, pattern):
    suite = unittest2.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


if __name__=='__main__':
    unittest2.main()
