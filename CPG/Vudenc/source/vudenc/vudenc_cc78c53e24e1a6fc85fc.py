def list_available_images(self):...
"""docstring"""
logger = logging.getLogger(__name__)
gcloud_agent = self.gce_observer
service_account = self.bindings.get('GCE_SERVICE_ACCOUNT', None)
extra_args = ['--account', service_account] if service_account else []
logger.debug('Looking up available images.')
cli_result = gcloud_agent.list_resources('images', extra_args=extra_args)
if not cli_result.ok():
json_doc = json_module.JSONDecoder().decode(cli_result.output)
spinnaker_account = self.agent.deployed_config.get(
    'providers.google.primaryCredentials.name')
logger.debug('Configured with Spinnaker account "%s"', spinnaker_account)
expect_images = [{'account': spinnaker_account, 'imageName': image['name']} for
    image in json_doc]
expect_images = sorted(expect_images, key=lambda k: k['imageName'])
builder = HttpContractBuilder(self.agent)
builder.new_clause_builder('Has Expected Images').get_url_path(
    '/gce/images/find').add_constraint(jc.EQUIVALENT(expect_images))
return st.OperationContract(NoOpOperation('List Available Images'),
    contract=builder.build())
