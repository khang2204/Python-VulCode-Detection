def _generate_data(self, user, data=None):...
profile = user.userprofile if user and user.is_authenticated() else None
return {'courses': self._generate_courses(profile), 'groups': self.
    _generate_groups(profile)}
