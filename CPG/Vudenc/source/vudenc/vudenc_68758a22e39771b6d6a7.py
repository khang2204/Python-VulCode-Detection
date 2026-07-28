def decode_factory(text):...
"""docstring"""
if isinstance(text, str):
return unicoder(text)
if isinstance(text, list):
new_text = []
if isinstance(text, dict):
for t in text:
new_text = {}
return text
new_text.append(decode_factory(t))
return new_text
for key in text:
new_text[key] = decode_factory(text[key])
return new_text
