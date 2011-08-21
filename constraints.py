#!/usrbin/env python

class Constraints:
    """Returns only those items of a directory which match constraints.

    A directory is a dict of members; each member is itself a dict of
    attributes. See tests/directory.yaml for a sample

    A constraint is a list of criteria. Each criterion is a dict of attributes;
    each attribute is a list of potential values for that attribute. See
    tests/groups.yaml for some sample criteria.

    How do we decide if a member of the directory matches?

    for each criterion in the list of criteria:
        for each attribute in the criterion's list of attributes:
            return all members which match any of the possible values
        return all members which appear on all lists for the criterion
    return all members which appear on any criterion's list
    """

    def __init__(self, directory):
        self.directory = directory

    def _get_members_for_attr(self, attr, values):
        attr_members = []
        for member_name, member in self.directory.items():
            if (attr in member and member[attr] in values):
                attr_members.append(member_name)
        return attr_members

    def _get_members_for_criterion(self, criterion):
        attr_member_lists = []
        attr_members = set(self.directory)
        for attr, values in criterion.items():
            attr_member_lists.append(self._get_members_for_attr(
                attr, values))
        for attr_member_list in attr_member_lists:
            attr_members = attr_members.intersection(attr_member_list)
        return attr_members

    def _get_members_for_criteria(self, criteria):
        criterion_member_lists = []
        criterion_members = set()
        for criterion in criteria:
            criterion_member_lists.append(self._get_members_for_criterion(
                criterion))
        for criterion_member_list in criterion_member_lists:
            criterion_members = criterion_members.union(criterion_member_list)
        return criterion_members

    def get_members(self, criteria):
        members = self._get_members_for_criteria(criteria)
        return members
