from grokcore.component import baseclass, context
from zope.component import provideSubscriptionAdapter
import argparse
from opennode.oms.endpoint.ssh import cmd
from opennode.oms.endpoint.ssh.completion import Completer
from opennode.oms.endpoint.ssh.cmdline import GroupDictAction
from opennode.oms.model.model.base import IContainer
from opennode.oms.model.model import creatable_models
from opennode.oms.zodb import db
"""Completes a command."""
context(cmd.NoCommand)
def complete(self, token, parsed, parser):...
return [name for name in cmd.commands().keys() if name.startswith(token)]
