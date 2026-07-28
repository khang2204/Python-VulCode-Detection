def __init__(self, key_transform, *args, **kwargs):...
assert isinstance(key_transform, JsonKeyTransform)
key_text_transform = JsonKeyTextTransform(key_transform.key_name, *
    key_transform.source_expressions, **key_transform.extra)
super(JsonKeyTransformTextLookupMixin, self).__init__(key_text_transform, *
    args, **kwargs)
