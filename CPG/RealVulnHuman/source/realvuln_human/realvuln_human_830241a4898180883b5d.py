return EditPaste(paste=paste_obj)

class DeletePaste(graphene.Mutation):
  result = graphene.Boolean()

  class Arguments:
    id = graphene.Int()


  def mutate(self, info, id):
    result = False

    if Paste.query.filter_by(id=id).delete():
      result = True
      db.session.commit()

    Audit.create_audit_entry(info)

    return DeletePaste(result=result)

class UploadPaste(graphene.Mutation):
  content = graphene.String()
  filename = graphene.String()

  class Arguments:
