from twisted.internet.defer import inlineCallbacks, returnValue
from base import Database
JOIN = 'JOIN'
LEFT_JOIN = 'LEFT JOIN'
TYPES = {'BOOL': 'bool', 'CHAR': 'varchar', 'FLOAT': 'float', 'INT': 'int',
    'JSON': 'jsonb', 'DATE': 'timestamp'}
def connectionError(self, f):...
print('ERROR: connecting failed with {0}'.format(f.value))
@inlineCallbacks...
from txpostgres import txpostgres, reconnection
from txpostgres.reconnection import DeadConnectionDetector
def startReconnecting(self, f):...
print('ERROR: database connection is down (error: {0})'.format(f.value))
return DeadConnectionDetector.startReconnecting(self, f)
