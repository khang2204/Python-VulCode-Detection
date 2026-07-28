import datetime
import json
import logging
import re
import MySQLdb
from collections import namedtuple, defaultdict
logger = logging.getLogger(u'JSON2SQLGenerator')
"""
    To Generate SQL query from JSON data
    """
WHERE_CONDITION = 'where'
AND_CONDITION = 'and'
OR_CONDITION = 'or'
NOT_CONDITION = 'not'
EXISTS_CONDITION = 'exists'
CUSTOM_METHOD_CONDITION = 'custom_method'
INTEGER = 'integer'
STRING = 'string'
DATE = 'date'
DATE_TIME = 'datetime'
BOOLEAN = 'boolean'
NULLBOOLEAN = 'nullboolean'
CHOICE = 'choice'
MULTICHOICE = 'multichoice'
CONVERSION_REQUIRED = [STRING, DATE, DATE_TIME]
BETWEEN = 'between'
BINARY_OPERATORS = BETWEEN,
ALLOWED_AGGREGATE_FUNCTIONS = {'MIN', 'MAX'}
ALLOWED_CUSTOM_METHOD_PARAM_TYPES = {'field', 'integer', 'string'}
IS_OPERATOR_VALUE = {'NULL', 'NOT NULL', 'TRUE', 'FALSE'}
VALUE_OPERATORS = namedtuple('VALUE_OPRATORS', ['equals', 'greater_than',
    'less_than', 'greater_than_equals', 'less_than_equals', 'not_equals',
    'is_op', 'in_op', 'like', 'between', 'is_challenge_completed',
    'is_challenge_not_completed'])(equals='=', greater_than='>', less_than=
    '<', greater_than_equals='>=', less_than_equals='<=', not_equals='<>',
    is_op='IS', in_op='IN', like='LIKE', is_challenge_completed=
    'is_challenge_completed', is_challenge_not_completed=
    'is_challenge_not_completed', between=BETWEEN)
DATA_TYPES = namedtuple('DATA_TYPES', ['integer', 'string', 'date',
    'date_time', 'boolean', 'nullboolean', 'choice', 'multichoice'])(integer
    =INTEGER, string=STRING, date=DATE, date_time=DATE_TIME, boolean=
    BOOLEAN, nullboolean=NULLBOOLEAN, choice=CHOICE, multichoice=MULTICHOICE)
FIELD_NAME = 'field_name'
TABLE_NAME = 'table_name'
DATA_TYPE = 'data_type'
JOIN_TABLE = 'join_table'
JOIN_COLUMN = 'join_column'
PARENT_TABLE = 'parent_table'
PARENT_COLUMN = 'parent_column'
CHALLENGE_CHECK_QUERY = (
    'EXISTS (SELECT 1 FROM journeys_memberstagechallenge WHERE challenge_id = {value} AND completed_date IS NOT NULL AND member_id = patients_member.id) '
    )
TEMPLATE_STR_KEY = 'template_str'
TEMPLATE_PARAMS_KEY = 'parameters'
TEMPLATE_KEY_REGEX = '{(\\w+)}'
def __init__(self, field_mapping, paths, custom_methods):...
"""docstring"""
self.base_table = ''
self.field_mapping = self._parse_field_mapping(field_mapping)
self.path_mapping = self._parse_multi_path_mapping(paths)
self.custom_methods = self._parse_custom_methods(custom_methods)
self.WHERE_CONDITION_MAPPING = {self.WHERE_CONDITION:
    '_generate_where_phrase', self.AND_CONDITION: '_parse_and', self.
    OR_CONDITION: '_parse_or', self.NOT_CONDITION: '_parse_not', self.
    EXISTS_CONDITION: '_parse_exists', self.CUSTOM_METHOD_CONDITION:
    '_parse_custom_method_condition'}
def _parse_custom_methods(self, sql_templates):...
"""docstring"""
template_mapping = {}
for template_id, template_str, parameters in sql_templates:
template_id = int(template_id)
return template_mapping
parameters = json.loads(parameters)
template_str = template_str.strip()
assert len(template_str) > 0, 'Not a valid template string'
assert template_id not in template_mapping, 'Template id must be unique'
template_defined_variables = set(re.findall(self.TEMPLATE_KEY_REGEX,
    template_str, re.MULTILINE))
assert len(set(parameters.keys()) ^ template_defined_variables
    ) == 0, 'Extra variable defined'
assert len(set(map(lambda l: l['data_type'], parameters.values())) - self.
    ALLOWED_CUSTOM_METHOD_PARAM_TYPES) == 0, 'Invalid data type defined'
template_mapping[template_id] = {self.TEMPLATE_STR_KEY: template_str, self.
    TEMPLATE_PARAMS_KEY: parameters}
