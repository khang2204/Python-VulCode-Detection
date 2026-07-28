import logging
from google.appengine.api import users
from google.appengine.ext import ndb
from gae_libs.handlers.base_handler import BaseHandler
from gae_libs.handlers.base_handler import Permission
from gae_libs.http import auth_util
from libs import analysis_status
from libs import time_util
from model import triage_status
from model.flake.flake_analysis_request import FlakeAnalysisRequest
from model.flake.flake_try_job import FlakeTryJob
from model.flake.flake_try_job_data import FlakeTryJobData
from model.flake.master_flake_analysis import MasterFlakeAnalysis
from waterfall import buildbot
from waterfall.flake import flake_analysis_service
from waterfall.flake import triggering_sources
from waterfall.trigger_base_swarming_task_pipeline import NO_TASK
from waterfall.trigger_base_swarming_task_pipeline import NO_TASK_EXCEPTION
def _GetSuspectedFlakeInfo(analysis):...
"""docstring"""
if analysis.suspected_flake_build_number is None:
return {}
data_point = analysis.GetDataPointOfSuspectedBuild()
assert data_point
return {'confidence': analysis.confidence_in_suspected_build,
    'build_number': analysis.suspected_flake_build_number,
    'commit_position': data_point.commit_position, 'git_hash': data_point.
    git_hash, 'lower_bound_commit_position': data_point.
    previous_build_commit_position, 'lower_bound_git_hash': data_point.
    previous_build_git_hash, 'triage_result': analysis.triage_history[-1].
    triage_result if analysis.triage_history else triage_status.UNTRIAGED}
