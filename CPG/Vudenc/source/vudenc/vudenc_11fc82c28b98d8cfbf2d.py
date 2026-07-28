def extract_author_keywords(skw_db, ckw_db, fulltext):...
"""docstring"""
akw = {}
K = reader.KeywordToken
for k, v in keyworder.get_author_keywords(skw_db, ckw_db, fulltext).items():
akw[K(k, type='author-kw')] = v
return akw
