from __future__ import absolute_import
import os
from pony.orm import db_session
from six.moves import xrange
from twisted.internet.defer import inlineCallbacks
from Tribler.Core.Modules.MetadataStore.OrmBindings.channel_node import NEW
from Tribler.Core.Modules.MetadataStore.store import MetadataStore
from Tribler.Core.Utilities.random_utils import random_infohash
from Tribler.community.gigachannel.community import GigaChannelCommunity
from Tribler.pyipv8.ipv8.keyvault.crypto import default_eccrypto
from Tribler.pyipv8.ipv8.peer import Peer
from Tribler.pyipv8.ipv8.test.base import TestBase
"""
    Unit tests for the GigaChannel community which do not need a real Session.
    """
def setUp(self):...
super(TestGigaChannelUnits, self).setUp()
self.count = 0
self.initialize(GigaChannelCommunity, 2)
def create_node(self, *args, **kwargs):...
metadata_store = MetadataStore(os.path.join(self.temporary_directory(), 
    '%d.db' % self.count), self.temporary_directory(), default_eccrypto.
    generate_key(u'curve25519'))
kwargs['metadata_store'] = metadata_store
node = super(TestGigaChannelUnits, self).create_node(*args, **kwargs)
self.count += 1
return node
