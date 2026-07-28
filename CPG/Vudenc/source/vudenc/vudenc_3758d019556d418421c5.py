def _mock_add_rules_in_section(*args):...
rules = args[0]
return {'rules': [{'display_name': rule['display_name'], 'id': uuidutils.
    generate_uuid()} for rule in rules]}
