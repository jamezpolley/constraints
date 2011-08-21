#!/usrbin/env python

class Constraints:

    def _get_members_for_attr(self, attr, values, directory):
        attr_members = []
        for member_name, member in directory.items():
            if (attr in member and member[attr] in values):
                attr_members.append(member_name)
        return attr_members

    def _get_members_for_criterion(self, criterion, directory):
        criterion_members = set(directory)
        attr_members = []
        for attr, values in criterion.items():
            attr_members.append(self._get_members_for_attr(
                attr, values, directory))
        for member_list in attr_members:
            criterion_members = criterion_members.intersection(
                    member_list)
        return criterion_members



    def get_members(self, criteria, directory=None):
        directory = directory or self._directory
        members = set()
        for criterion in criteria:
            members = members.union(
                    self._get_members_for_criterion(criterion, directory))

        return members




