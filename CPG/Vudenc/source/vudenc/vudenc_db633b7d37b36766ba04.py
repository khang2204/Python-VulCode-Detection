def __init__(self, campaign={}, create_result=False, database_file=...
if not exists(database_file):
self.campaign = campaign
self.result = {}
self.file = database_file
self.lock = Lock()
if create_result:
db.__create_result()
