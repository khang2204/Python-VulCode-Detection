return self.username.capitalize()
    return self.username

  @staticmethod
  def resolve_password(self, info, **kwargs):
    if info.context.json.get('identity') == 'admin':
      return self.password
    else:
      return '******'

class PasteObject(SQLAlchemyObjectType):
  class Meta:
    model = Paste

  def resolve_ip_addr(self, info):
    for field_ast in info.field_asts:
      for i in field_ast.directives:
        if i.name.value == 'show_network':
          if i.arguments[0].name.value == 'style':
            return security.get_network(self.ip_addr, style=i.arguments[0].value.value)
    return self.ip_addr

class OwnerObject(SQLAlchemyObjectType):
  class Meta:
    model = Owner

class AuditObject(SQLAlchemyObjectType):
  class Meta:
    model = Audit

class UserInput(graphene.InputObjectType):
  username = graphene.String(required=True)
  email = graphene.String(required=True)
  password = graphene.String(required=True)
