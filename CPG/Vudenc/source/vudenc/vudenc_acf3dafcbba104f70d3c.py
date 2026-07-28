def extract_abbreviations(fulltext):...
"""docstring"""
acronyms = {}
K = reader.KeywordToken
for k, v in acronymer.get_acronyms(fulltext).items():
acronyms[K(k, type='acronym')] = v
return acronyms
