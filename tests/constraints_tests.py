#!/usr/bin/env python

import nose
import yaml

from constraints import Constraints

class TestConstraints(object):

    @classmethod
    def setup_class(cls):
        directory_file=open('tests/directory.yaml')
        cls.directory=yaml.load(directory_file)
        groups_file=open('tests/groups.yaml')
        cls.groups=yaml.load(groups_file)

        cls.constrainer = Constraints()

    def test_members_for_attr(self):
        attr = 'location'
        values = ['Winterfell', 'Kings Landing']
        expected_members = ['eddard', 'robert', 'catelyn', 'cersei', 'tyrion']
        generated_members = self.constrainer._get_members_for_attr(
                attr, values, self.directory)
        assert len(generated_members) == len(expected_members)
        for expected_member in expected_members:
            assert expected_member in generated_members

    def check_group_membership(self, criteria, expected_members):
        generated_members = self.constrainer.get_members(criteria=criteria,
                directory=self.directory)
        assert len(generated_members) == len(expected_members)
        for expected_member in expected_members:
            assert expected_member in generated_members


    def test_group_memberships(self):
        for test_name, test_data in self.groups.items():
            yield (self.check_group_membership, test_data['criteria'],
                test_data['members'])





