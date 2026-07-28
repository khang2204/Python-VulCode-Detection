@classmethod...
super(TestGetObjectInfo, cls).setUpTestData()
cls.get_info_url = reverse('ajax-info')
cls.group_nitrate = EnvGroupFactory(name='nitrate')
cls.group_new = EnvGroupFactory(name='NewGroup')
cls.property_os = EnvPropertyFactory(name='os')
cls.property_python = EnvPropertyFactory(name='python')
cls.property_django = EnvPropertyFactory(name='django')
EnvGroupPropertyMapFactory(group=cls.group_nitrate, property=cls.property_os)
EnvGroupPropertyMapFactory(group=cls.group_nitrate, property=cls.
    property_python)
EnvGroupPropertyMapFactory(group=cls.group_new, property=cls.property_django)
