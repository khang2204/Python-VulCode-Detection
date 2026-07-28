import asyncio
import mistune
from tortoise import fields
from tortoise.query_utils import Q
from arq import create_pool
from config import REDIS_URL
from .base import BaseModel
from .mc import cache, clear_mc
from .user import GithubUser
from .consts import K_COMMENT, ONE_HOUR
from .react import ReactMixin, ReactItem
from .signals import comment_reacted
from .utils import RedisSettings
markdown = mistune.Markdown()
MC_KEY_COMMENT_LIST = 'comment:%s:comment_list'
MC_KEY_N_COMMENTS = 'comment:%s:n_comments'
MC_KEY_COMMNET_IDS_LIKED_BY_USER = 'react:comment_ids_liked_by:%s:%s'
github_id = fields.IntField()
post_id = fields.IntField()
ref_id = fields.IntField(default=0)
kind = K_COMMENT
table = 'comments'
async def set_content(self, content):...
return await self.set_props_by_key('content', content)
