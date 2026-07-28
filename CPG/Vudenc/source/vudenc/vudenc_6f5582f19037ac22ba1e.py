async def del_comment(self, user_id, comment_id):...
c = await Comment.get(id=comment_id)
if c and c.github_id == user_id and c.post_id == self.id:
await c.delete()
return False
return True
