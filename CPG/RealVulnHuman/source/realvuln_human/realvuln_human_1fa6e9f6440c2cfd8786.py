raise werkzeug.exceptions.SecurityError('Introspection is Disabled')

    return next(root, info, **kwargs)

class IGQLProtectionMiddleware(object):
  @run_only_once
  def resolve(self, next, root, info, **kwargs):
    if helpers.is_level_hard():
      raise werkzeug.exceptions.SecurityError('GraphiQL is disabled')

    cookie = request.cookies.get('env')
    if cookie and cookie == 'graphiql:enable':
      return next(root, info, **kwargs)

    raise werkzeug.exceptions.SecurityError('GraphiQL Access Rejected')
