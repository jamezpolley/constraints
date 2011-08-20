#!/usrbin/env python

class Constraints:

    def get_members(self, criteria, directory=None):
        members = set()
        for criterion in criteria:
            criterion_members = set()
            for member_name, member in directory.items():
                for attr, values in criterion.items():
                    if (attr in member and member[attr] in values):
                        attr_members.add(member_name)

        return members




