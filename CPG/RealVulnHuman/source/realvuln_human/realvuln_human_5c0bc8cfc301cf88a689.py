opname = info.operation.name.value
    except:
      opname = "No Operation"

    if opname != 'No Operation' and not security.operation_name_allowed(opname):
      raise werkzeug.exceptions.SecurityError('Operation Name "{}" is not allowed.'.format(opname))

    return next(root, info, **kwargs)


class processMiddleware(object):
  def resolve(self, next, root, info, **kwargs):
    if helpers.is_level_easy():
      return next(root, info, **kwargs)

    array_qry = []

    if info.context.json is not None:
      if isinstance(info.context.json, dict):
        array_qry.append(info.context.json)

      for q in array_qry:
        query = q.get('query', None)
        if security.on_denylist(query):
          raise werkzeug.exceptions.SecurityError('Query is on the Deny List.')

    return next(root, info, **kwargs)

class IntrospectionMiddleware(object):
  @run_only_once
  def resolve(self, next, root, info, **kwargs):
    if helpers.is_level_easy():
      return next(root, info, **kwargs)

    if info.field_name.lower() in ['__schema']:
      raise werkzeug.exceptions.SecurityError('Introspection is Disabled')
