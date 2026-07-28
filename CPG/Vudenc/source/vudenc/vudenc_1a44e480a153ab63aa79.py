from cachetools import TTLCache, cached
from sqlalchemy import func, text
from server import db
from server.models.dtos.stats_dto import ProjectContributionsDTO, UserContribution, Pagination, TaskHistoryDTO, ProjectActivityDTO, HomePageStatsDTO, OrganizationStatsDTO, CampaignStatsDTO
from server.models.postgis.project import Project
from server.models.postgis.statuses import TaskStatus
from server.models.postgis.task import TaskHistory, User, Task
from server.models.postgis.utils import timestamp, NotFound
from server.services.project_service import ProjectService
from server.services.users.user_service import UserService
homepage_stats_cache = TTLCache(maxsize=4, ttl=30)
@staticmethod...
"""docstring"""
if new_state in [TaskStatus.READY, TaskStatus.LOCKED_FOR_VALIDATION,
return
project = ProjectService.get_project_by_id(project_id)
user = UserService.get_user_by_id(user_id)
StatsService._update_tasks_stats(project, user, last_state, new_state, action)
UserService.upsert_mapped_projects(user_id, project_id)
project.last_updated = timestamp()
return project, user
