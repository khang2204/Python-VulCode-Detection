formatted = Analytics.format_raw_sql(cmd, raw, col)
    return formatted

# defined in railsgoat but not used, expects valid column name
@classmethod
def count_by_col(cls, col):
    return cls.objects.values(col).count()

# expects field type to be string
@staticmethod
def parse_field(field):
    valid_fields = ["ip_address", "referrer", "user_agent"]
    if field in valid_fields:
        return field
    else:
        return '1'
