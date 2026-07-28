def include(self, *names, contexts=None):...
contexts = list(contexts) if contexts is not None else []
contexts.extend(self._get_context(name) for name in names)
return ContextView(self, contexts)
