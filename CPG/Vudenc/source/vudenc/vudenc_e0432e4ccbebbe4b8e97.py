def add_observer(self, func, subject, changeTypes=None, id=None, cache=0):...
changeTypes = changeTypes or [NTFY_UPDATE, NTFY_INSERT, NTFY_DELETE]
"""
        Add observer function which will be called upon certain event
        Example:
        addObserver(NTFY_TORRENTS, [NTFY_INSERT,NTFY_DELETE]) -> get callbacks
                    when peers are added or deleted
        addObserver(NTFY_TORRENTS, [NTFY_SEARCH_RESULT], 'a_search_id') -> get
                    callbacks when peer-searchresults of of search
                    with id=='a_search_id' come in
        """
assert isinstance(changeTypes, list)
assert subject in self.SUBJECTS, 'Subject %s not in SUBJECTS' % subject
obs = func, subject, changeTypes, id, cache
self.observerLock.acquire()
self.observers.append(obs)
self.observerLock.release()
