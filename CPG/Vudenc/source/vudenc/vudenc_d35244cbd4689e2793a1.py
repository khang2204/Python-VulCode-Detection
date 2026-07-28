def os_supported(min_v, max_v):...
"""docstring"""
os_version = re.match('[0-9]+\\.[0-9]+', platform.mac_ver()[0]).group(0)
return not (os_version < str(min_v) or max_v is not None and os_version >
    str(max_v))
