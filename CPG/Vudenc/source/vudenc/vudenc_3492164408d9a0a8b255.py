def azure_rm(cred, env, private_data_dir):...
client = cred.get_input('client', default='')
tenant = cred.get_input('tenant', default='')
if len(client) and len(tenant):
env['AZURE_CLIENT_ID'] = client
env['AZURE_SUBSCRIPTION_ID'] = cred.get_input('subscription', default='')
env['AZURE_TENANT'] = tenant
env['AZURE_AD_USER'] = cred.get_input('username', default='')
env['AZURE_SECRET'] = cred.get_input('secret', default='')
env['AZURE_PASSWORD'] = cred.get_input('password', default='')
env['AZURE_SUBSCRIPTION_ID'] = cred.get_input('subscription', default='')
if cred.has_input('cloud_environment'):
env['AZURE_CLOUD_ENVIRONMENT'] = cred.get_input('cloud_environment')
