def CreateCompletionRequest(self, force_semantic=False):...
if not self.NativeFiletypeCompletionAvailable(
self._latest_completion_request = OmniCompletionRequest(self._omnicomp)
extra_data = {}
return self._latest_completion_request
self._AddExtraConfDataIfNeeded(extra_data)
if force_semantic:
extra_data['force_semantic'] = True
self._latest_completion_request = CompletionRequest(extra_data
    ) if self._IsServerAlive() else None
