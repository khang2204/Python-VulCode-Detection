def __init__(self):...
super(OmsSshProtocol, self).__init__()
self.path = ['']
@defer.inlineCallbacks...
self.obj_path = yield db.transact(lambda : [db.ref(db.get_root()['oms_root'])]
    )()
_get_obj_path()
self.tokenizer = CommandLineTokenizer()
