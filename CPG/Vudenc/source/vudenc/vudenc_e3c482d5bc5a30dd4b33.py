def get_matching_Member(self, username, discriminator):...
all_members = self.get_all_members()
matching_member = [x for x in all_members if x.name == username and x.
    discriminator == discriminator][0]
return matching_member
