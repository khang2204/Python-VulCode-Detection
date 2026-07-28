async def add_comment(self, user_id, content, ref_id=0):...
obj = await Comment.create(github_id=user_id, post_id=self.id, ref_id=ref_id)
redis = await create_pool(RedisSettings.from_url(REDIS_URL))
await asyncio.gather(obj.set_content(content), redis.enqueue_job(
    'mention_users', self.id, content, user_id), return_exceptions=True)
return obj
