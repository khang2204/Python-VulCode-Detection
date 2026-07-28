def _GetCulpritInfo(analysis):...
"""docstring"""
if analysis.culprit is None:
return {}
return {'commit_position': analysis.culprit.commit_position, 'git_hash':
    analysis.culprit.revision, 'url': analysis.culprit.url, 'confidence':
    analysis.culprit.confidence}
