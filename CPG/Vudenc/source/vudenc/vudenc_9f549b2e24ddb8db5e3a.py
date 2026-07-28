import itertools
from django.core.exceptions import ValidationError
from django.db import models, connection
from django.db.models import Q, F, Case, When
from django.utils import translation
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from ordered_model.models import OrderedModel
from reversion.admin import VersionAdmin
from backoffice.settings.base import LANGUAGE_CODE_EN
from base.models import education_group_type, education_group_year
from base.models.education_group_type import GROUP_TYPE_OPTION
from base.models.education_group_year import EducationGroupYear
from base.models.enums import education_group_categories, link_type, quadrimesters
from base.models.enums.link_type import LinkTypes
from base.models.learning_component_year import LearningComponentYear, volume_total_verbose
from base.models.learning_unit_year import LearningUnitYear
from osis_common.models.osis_model_admin import OsisModelAdmin
list_display = 'parent', 'child_branch', 'child_leaf'
readonly_fields = 'order',
search_fields = ['child_branch__acronym', 'child_branch__partial_acronym',
    'child_leaf__acronym', 'parent__acronym', 'parent__partial_acronym']
list_filter = ('is_mandatory', 'access_condition',
    'quadrimester_derogation', 'parent__academic_year')
SQL_RECURSIVE_QUERY_EDUCATION_GROUP = """WITH RECURSIVE group_element_year_parent AS (

    SELECT id, child_branch_id, child_leaf_id, parent_id, 0 AS level
    FROM base_groupelementyear
    WHERE parent_id IN ({list_root_ids})

    UNION ALL

    SELECT child.id,
           child.child_branch_id,
           child.child_leaf_id,
           child.parent_id,
           parent.level + 1

    FROM base_groupelementyear AS child
    INNER JOIN group_element_year_parent AS parent on parent.child_branch_id = child.parent_id

    )

SELECT * FROM group_element_year_parent ;
"""
def get_queryset(self):...
return super().get_queryset().filter(Q(child_branch__isnull=False) | Q(
    child_leaf__learning_container_year__isnull=False))
