result = graphene.String()

class Arguments:
  host = graphene.String(required=True)
  port = graphene.Int(required=False)
  path = graphene.String(required=True)
  scheme = graphene.String(required=True)

def mutate(self, info, host='pastebin.com', port=443, path='/', scheme="http"):
  url = security.strip_dangerous_characters(f"{scheme}://{host}:{port}{path}")
  cmd = helpers.run_cmd(f'curl --insecure {url}')

  owner = Owner.query.filter_by(name='DVGAUser').first()
  Paste.create_paste(
      title='Imported Paste from URL - {}'.format(helpers.generate_uuid()),
      content=cmd, public=False, burn=False,
      owner_id=owner.id, owner=owner, ip_addr=request.remote_addr,
      user_agent=request.headers.get('User-Agent', '')
  )

  Audit.create_audit_entry(info)
