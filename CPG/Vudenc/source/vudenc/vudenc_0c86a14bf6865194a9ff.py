@comment_reacted.connect...
comment = await Comment.cache(comment_id)
if comment:
asyncio.gather(clear_mc(MC_KEY_COMMENT_LIST % comment.post_id), clear_mc(
    MC_KEY_COMMNET_IDS_LIKED_BY_USER % (user_id, comment.post_id)),
    return_exceptions=True)
