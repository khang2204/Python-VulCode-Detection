def handle_query(tokens, id, query):...
commands = {'help': customer_commands.process_help, 'id': customer_commands
    .process_id, 'purchase': customer_commands.process_purchase, 'brand':
    customer_commands.process_brand, 'itemtype': customer_commands.
    process_type, 'userinfo': customer_commands.process_userinfo, 'lookup':
    customer_commands.process_lookup}
command = commands.get(tokens[0], 'invalid')
if command == 'invalid':
print('\tinvalid command "' + tokens[0] + '"')
command(id, tokens[1:], query)
