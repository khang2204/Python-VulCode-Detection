"""Subscriptions"""
  gql_query = info
  ast = parse(gql_query)

  try:
    gql_operation = ast.definitions[0].name.value
  except:
    gql_operation = 'No Operation'

  obj = cls(**{"gqloperation":gql_operation, "gqlquery":gql_query})
  db.session.add(obj)
else:
  """Queries and Mutations"""
  try:
    gql_operation = info.operation.name.value
  except:
    gql_operation = "No Operation"

  if isinstance(info, ResolveInfo):
    if isinstance(info.context.json, list):
      """Array-based Batch"""
      for i in info.context.json:
        gql_query = i.get("query")
        gql_query = clean_query(gql_query)
        obj = cls(**{"gqloperation":gql_operation, "gqlquery":gql_query})
        db.session.add(obj)
    else:
      if info.context.json:
        gql_query = info.context.json.get("query")
        gql_query = clean_query(gql_query)
        obj = cls(**{"gqloperation":gql_operation, "gqlquery":gql_query})
        db.session.add(obj)
