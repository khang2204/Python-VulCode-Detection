@click.command(help='Get state')...
state = newrelic.get_state(ctx.obj['ACCOUNT'])
print('# Generated on {}'.format(datetime.utcnow().isoformat()))
print(yaml.dump(state, allow_unicode=True, default_flow_style=False, Dumper
    =yamlordereddictloader.SafeDumper))
