def get_sanitized_bracket(url, symbol='{}'):...
bracket = get_bracket(url)
sanitized = sanitize_bracket(bracket, symbol) if bracket else None
return sanitized
