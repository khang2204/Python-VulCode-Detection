"""
HubbleStack Custom Grains and Pillar

Allows for fetching custom grain and pillar data from a local salt-minion via
salt-call

:maintainer: HubbleStack
:platform: All
:requires: SaltStack
"""
import re
import salt.modules.cmdmod
import logging
log = logging.getLogger(__name__)
__salt__ = {'cmd.run': salt.modules.cmdmod._run_quiet, 'config.get': salt.
    modules.config.get}
def populate_custom_grains_and_pillar():...
"""docstring"""
log.debug('Fetching custom grains and pillar details')
grains = {}
salt.modules.config.__opts__ = __opts__
custom_grains = __salt__['config.get']('custom_grains_pillar:grains', [])
for grain in custom_grains:
for key in grain:
custom_pillar = __salt__['config.get']('custom_grains_pillar:pillar', [])
if _valid_command(grain[key]):
for pillar in custom_pillar:
value = __salt__['cmd.run']('salt-call grains.get {0}'.format(grain[key])
    ).split('\n')[1].strip()
for key in pillar:
log.debug('Done with fetching custom grains and pillar details')
grains[key] = value
if _valid_command(pillar[key]):
return grains
value = __salt__['cmd.run']('salt-call pillar.get {0}'.format(pillar[key])
    ).split('\n')[1].strip()
grains[key] = value
