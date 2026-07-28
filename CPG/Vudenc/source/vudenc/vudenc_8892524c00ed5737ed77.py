from re import compile, UNICODE
from Acquisition import aq_base
from unidecode import unidecode
from collective.solr.interfaces import ISolrSchema
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
import six
from six.moves import range
if hasattr(str, 'maketrans'):
maketrans = str.maketrans
from string import maketrans
def getConfig():...
registry = getUtility(IRegistry)
return registry.forInterface(ISolrSchema, prefix='collective.solr')
