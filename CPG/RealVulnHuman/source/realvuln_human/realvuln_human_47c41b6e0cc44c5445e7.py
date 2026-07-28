return CreatePaste(paste=paste_obj)

class EditPaste(graphene.Mutation):
    paste = graphene.Field(lambda:PasteObject)

    class Arguments:
      id = graphene.Int()
      title = graphene.String(required=False)
      content = graphene.String(required=False)

    def mutate(self, info, id, title=None, content=None):
      paste_obj = Paste.query.filter_by(id=id).first()

      if title == None:
        title = paste_obj.title
      if content == None:
        content = paste_obj.content

      Paste.query.filter_by(id=id).update(dict(title=title, content=content))
      paste_obj = Paste.query.filter_by(id=id).first()

      db.session.commit()

      Audit.create_audit_entry(info)

      return EditPaste(paste=paste_obj)

class DeletePaste(graphene.Mutation):
  result = graphene.Boolean()
