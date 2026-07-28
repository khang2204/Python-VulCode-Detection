from __future__ import unicode_literals
from six.moves import urllib_parse as urlparse
import os
import collections
import requests
import six
import json
import yaml
from flex.context_managers import ErrorDict
from flex.exceptions import ValidationError
from flex.loading.definitions import definitions_validator
from flex.loading.schema import swagger_schema_validator
from flex.loading.schema.paths.path_item.operation.responses.single.schema import schema_validator
from flex.http import normalize_request, normalize_response
from flex.validation.common import validate_object
from flex.validation.request import validate_request
from flex.validation.response import validate_response
def load_source(source):...
"""docstring"""
if isinstance(source, collections.Mapping):
return source
if hasattr(source, 'read') and callable(source.read):
raw_source = source.read()
if os.path.exists(os.path.expanduser(str(source))):
def parse(raw_schema):...
return json.loads(raw_source)
return yaml.load(raw_source)
raw_source = source_file.read()
if isinstance(source, six.string_types):
context = {'deferred_references': set()}
parts = urlparse.urlparse(source)
swagger_definitions = definitions_validator(raw_schema, context=context)
if parts.scheme and parts.netloc:
swagger_schema = swagger_schema_validator(raw_schema, context=
    swagger_definitions)
response = requests.get(source)
raw_source = source
return swagger_schema
if isinstance(response.content, six.binary_type):
raw_source = six.text_type(response.content, encoding='utf-8')
raw_source = response.content
