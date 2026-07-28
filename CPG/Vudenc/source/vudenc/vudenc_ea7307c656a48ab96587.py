"""Set of functions for tasks to freeze the data within a GSoCProgram.
"""
__authors__ = ['"Daniel Hans" <daniel.m.hans@gmail.com>',
    '"Lennard de Rijk" <ljvderijk@gmail.com>']
import pickle
from google.appengine.ext import db
from soc.tasks import responses
from soc.tasks.helper import error_handler
from soc.modules.gsoc.logic.models.mentor import logic as mentor_logic
from soc.modules.gsoc.logic.models.org_admin import logic as org_admin_logic
from soc.modules.gsoc.logic.models.organization import logic as org_logic
from soc.modules.gsoc.logic.models.program import logic as program_logic
from soc.modules.gsoc.logic.models.student import logic as student_logic
ROLE_PER_SCOPE_MODELS_URL_PATTERNS = [(
    '^tasks/gsoc/freezer/manage_students_status$',
    'soc.modules.gsoc.tasks.program_freezer.manageStudentsStatus')]
ROLE_PER_PROGRAM_MODELS_URL_PATTERNS = [(
    '^tasks/gsoc/freezer/manage_mentors_status$',
    'soc.modules.gsoc.tasks.program_freezer.manageMentorsStatus'), (
    '^tasks/gsoc/freezer/manage_org_admins_status$',
    'soc.modules.gsoc.tasks.program_freezer.manageOrgAdminsStatus')]
ORG_MODEL_URL_PATTERNS = [('^tasks/gsoc/freezer/manage_orgs_status$',
    'soc.modules.gsoc.tasks.program_freezer.manageOrgsStatus')]
ROLE_MODELS_URL_PATTERNS = (ROLE_PER_SCOPE_MODELS_URL_PATTERNS +
    ROLE_PER_PROGRAM_MODELS_URL_PATTERNS + ORG_MODEL_URL_PATTERNS)
BATCH_SIZE = 50
def getDjangoURLPatterns():...
"""docstring"""
return ROLE_MODELS_URL_PATTERNS
