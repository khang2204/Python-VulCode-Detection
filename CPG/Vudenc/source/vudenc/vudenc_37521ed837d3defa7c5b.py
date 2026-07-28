"""This module is to handle manual triage of a suspected CL.

This handler will flag the suspected cl as correct or incorrect.
"""
from google.appengine.api import users
from google.appengine.ext import ndb
from gae_libs.handlers.base_handler import BaseHandler
from gae_libs.handlers.base_handler import Permission
from libs import time_util
from model import result_status
from model import suspected_cl_status
from model.wf_analysis import WfAnalysis
from model.wf_suspected_cl import WfSuspectedCL
from waterfall import build_util
from waterfall import buildbot
from waterfall.suspected_cl_util import GetCLInfo
@ndb.transactional...
suspected_cl = WfSuspectedCL.Get(repo_name, revision)
if not suspected_cl or not suspected_cl.builds:
return False
if not suspected_cl.builds.get(build_key):
return True
suspected_cl.builds[build_key]['status'] = cl_status
cl_correct = True
cl_incorrect = True
partial_triaged = False
for build in suspected_cl.builds.values():
if build['status'] is None:
if partial_triaged:
partial_triaged = True
if build['status'] == suspected_cl_status.CORRECT:
suspected_cl.status = suspected_cl_status.PARTIALLY_TRIAGED
if cl_correct:
cl_incorrect = False
cl_correct = False
suspected_cl.updated_time = updated_time or time_util.GetUTCNow()
suspected_cl.status = suspected_cl_status.CORRECT
if cl_incorrect:
suspected_cl.put()
suspected_cl.status = suspected_cl_status.INCORRECT
suspected_cl.status = suspected_cl_status.PARTIALLY_CORRECT
return True
