def parse(raw_schema):...
context = {'deferred_references': set()}
swagger_definitions = definitions_validator(raw_schema, context=context)
swagger_schema = swagger_schema_validator(raw_schema, context=
    swagger_definitions)
return swagger_schema
