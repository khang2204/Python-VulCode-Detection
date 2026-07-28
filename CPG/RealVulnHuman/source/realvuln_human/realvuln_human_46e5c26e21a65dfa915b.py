username = graphene.String(capitalize=graphene.Boolean())

  @staticmethod
  def resolve_username(self, info, **kwargs):
    if kwargs.get('capitalize'):
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
