def __init__(self, source_proxy, target_proxy):...
self._src_prx = source_proxy
self._tgt_prx = target_proxy
self.__traversed = set()
self.__root_is_sequence = (not source_proxy is None and source_proxy.
    proxy_for == RESOURCE_KINDS.COLLECTION or not target_proxy is None and 
    target_proxy.proxy_for == RESOURCE_KINDS.COLLECTION)
if __debug__:
self.__logger = get_logger('everest')
self.__logger = None
