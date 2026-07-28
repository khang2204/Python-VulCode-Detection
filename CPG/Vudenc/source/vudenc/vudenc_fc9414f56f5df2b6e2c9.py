@staticmethod...
"""docstring"""
dto = HomePageStatsDTO()
dto.total_projects = Project.query.count()
dto.mappers_online = Task.query.filter(Task.locked_by is not None).distinct(
    Task.locked_by).count()
dto.total_mappers = User.query.count()
dto.total_validators = Task.query.filter(Task.task_status == TaskStatus.
    VALIDATED.value).distinct(Task.validated_by).count()
dto.tasks_mapped = Task.query.filter(Task.task_status.in_((TaskStatus.
    MAPPED.value, TaskStatus.VALIDATED.value))).count()
dto.tasks_validated = Task.query.filter(Task.task_status == TaskStatus.
    VALIDATED.value).count()
org_proj_count = db.session.query(Project.organisation_tag, func.count(
    Project.organisation_tag)).group_by(Project.organisation_tag).all()
untagged_count = 0
tasks_mapped_sql = (
    'select coalesce(sum(ST_Area(geometry)), 0) as sum from public.tasks where task_status = :task_status'
    )
tasks_mapped_result = db.engine.execute(text(tasks_mapped_sql), task_status
    =TaskStatus.MAPPED.value)
dto.total_mapped_area = tasks_mapped_result.fetchone()['sum']
tasks_validated_sql = (
    'select coalesce(sum(ST_Area(geometry)), 0) as sum from public.tasks where task_status = :task_status'
    )
tasks_validated_result = db.engine.execute(text(tasks_validated_sql),
    task_status=TaskStatus.VALIDATED.value)
dto.total_validated_area = tasks_validated_result.fetchone()['sum']
campaign_count = db.session.query(Project.campaign_tag, func.count(Project.
    campaign_tag)).group_by(Project.campaign_tag).all()
no_campaign_count = 0
unique_campaigns = 0
for tup in campaign_count:
campaign_stats = CampaignStatsDTO(tup)
if no_campaign_count:
if campaign_stats.tag:
no_campaign_proj = CampaignStatsDTO(('Untagged', no_campaign_count))
dto.total_campaigns = unique_campaigns
dto.campaigns.append(campaign_stats)
no_campaign_count += campaign_stats.projects_created
dto.campaigns.append(no_campaign_proj)
org_proj_count = db.session.query(Project.organisation_tag, func.count(
    Project.organisation_tag)).group_by(Project.organisation_tag).all()
unique_campaigns += 1
no_org_count = 0
unique_orgs = 0
for tup in org_proj_count:
org_stats = OrganizationStatsDTO(tup)
if no_org_count:
if org_stats.tag:
no_org_proj = OrganizationStatsDTO(('Untagged', no_org_count))
dto.total_organizations = unique_orgs
dto.organizations.append(org_stats)
no_org_count += org_stats.projects_created
dto.organizations.append(no_org_proj)
return dto
unique_orgs += 1
