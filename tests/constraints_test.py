#!/usr/bin/env python

import yaml
import unittest2

from constraints import Constraints



class TestPrivateFunctions(unittest.TestCase):

    @classmethod
    def generate_group_membership_checker(self, criteria, expected_members):
        def check_group_membership(self):
            generated_members = self.constrainer.get_members(criteria=criteria,
                    directory=self.directory)
            self.assertItemsEqual(expected_members, generated_members)
        return check_group_membership


    @classmethod
    def setUpClass(cls):
        directory_file=open('tests/directory.yaml')
        cls.directory=yaml.load(directory_file)
        groups_file=open('tests/groups.yaml')
        cls.groups=yaml.load(groups_file)

        for test_name, test_data in cls.groups.items():
            test = cls.generate_group_membership_checker(test_data['criteria'],
                    test_data['members'])
            setattr(self, test_name, test)

    def setUp(self):
        self.constrainer = Constraints()

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

if __name__=='__main__':
    unittest2.main()






