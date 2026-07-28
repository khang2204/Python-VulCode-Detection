@cache(MC_KEY_COMMNET_IDS_LIKED_BY_USER % ('{user_id}', '{self.id}'), ONE_HOUR)...
cids = [c.id for c in await self.comments]
if not cids:
return []
queryset = await ReactItem.filter(Q(user_id=user_id), Q(target_id__in=cids),
    Q(target_kind=K_COMMENT))
return [item.target_id for item in queryset]
