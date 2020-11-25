class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    group_size = len(group.get_groups())
    if group_size == 0:
        return False
    else:
        for g in group.get_groups():
            return is_user_in_group(user, g)

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
#Testcase 1
val = is_user_in_group(sub_child_user, parent)
print("result = {}".format(val)) # True
#Testcase 2
val = is_user_in_group("", parent)
print("result = {}".format(val)) # False
#Testcase 3
val = is_user_in_group(None, parent)
print("result = {}".format(val)) # False
