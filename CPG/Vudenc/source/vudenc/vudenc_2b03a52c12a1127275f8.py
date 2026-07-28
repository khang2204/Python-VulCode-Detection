def get_keywords_from_text(text_lines, taxonomy_name, output_mode='text',...
"""docstring"""
cache = reader.get_cache(taxonomy_name)
if not cache:
reader.set_cache(taxonomy_name, reader.get_regular_expressions(
    taxonomy_name, rebuild=rebuild_cache, no_cache=no_cache))
_skw = cache[0]
cache = reader.get_cache(taxonomy_name)
_ckw = cache[1]
text_lines = normalizer.cut_references(text_lines)
fulltext = normalizer.normalize_fulltext('\n'.join(text_lines))
if match_mode == 'partial':
fulltext = _get_partial_text(fulltext)
author_keywords = None
if with_author_keywords:
author_keywords = extract_author_keywords(_skw, _ckw, fulltext)
acronyms = {}
if extract_acronyms:
acronyms = extract_abbreviations(fulltext)
single_keywords = extract_single_keywords(_skw, fulltext)
composite_keywords = extract_composite_keywords(_ckw, fulltext, single_keywords
    )
if only_core_tags:
single_keywords = clean_before_output(_filter_core_keywors(single_keywords))
single_keywords = clean_before_output(single_keywords)
composite_keywords = _filter_core_keywors(composite_keywords)
return get_keywords_output(single_keywords, composite_keywords,
    taxonomy_name, author_keywords, acronyms, output_mode, output_limit,
    spires, only_core_tags)
