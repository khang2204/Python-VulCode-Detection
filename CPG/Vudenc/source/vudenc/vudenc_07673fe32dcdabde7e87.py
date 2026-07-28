@classmethod...
super(TestNovaNetwork, cls).setUpClass()
if cls.manager.clients_initialized:
cls.tenant_id = cls.manager._get_identity_client(cls.config.identity.
    admin_username, cls.config.identity.admin_password, cls.config.identity
    .admin_tenant_name).tenant_id
cls.keypairs = {}
cls.security_groups = {}
cls.network = []
cls.servers = []
cls.floating_ips = []
