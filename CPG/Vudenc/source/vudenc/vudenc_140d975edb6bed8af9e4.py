def __init__(self, bindings, agent=None):...
super(GoogleServerGroupTestScenario, self).__init__(bindings, agent)
self.TEST_APP = bindings['TEST_APP']
self.__path = 'applications/%s/tasks' % self.TEST_APP
self.TEST_STACK = bindings['TEST_STACK']
self.TEST_REGION = bindings['TEST_GCE_REGION']
self.TEST_ZONE = bindings['TEST_GCE_ZONE']
self.__cluster_name = '%s-%s' % (self.TEST_APP, self.TEST_STACK)
self.__server_group_name = '%s-v000' % self.__cluster_name
self.__cloned_server_group_name = '%s-v001' % self.__cluster_name
self.__lb_name = '%s-%s-fe' % (self.TEST_APP, self.TEST_STACK)
