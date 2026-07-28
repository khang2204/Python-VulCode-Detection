import asyncio
import click
import collections
import hashlib
import os
import sys
import threading
import traceback
import urllib.parse
from concurrent import futures
from pathlib import Path
from markupsafe import Markup
from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PrefixLoader
from sanic import Sanic, response
from sanic.exceptions import InvalidUsage, NotFound
from .views.base import DatasetteError, ureg
from .views.database import DatabaseDownload, DatabaseView
from .views.index import IndexView
from .views.special import JsonDataView
from .views.table import RowView, TableView
from .utils import InterruptedError, Results, escape_css_string, escape_sqlite, get_plugins, module_from_path, sqlite3, sqlite_timelimit, to_css_class
from .inspect import inspect_hash, inspect_views, inspect_tables
from .plugins import pm, DEFAULT_PLUGINS
from .version import __version__
app_root = Path(__file__).parent.parent
connections = threading.local()
MEMORY = object()
ConfigOption = collections.namedtuple('ConfigOption', ('name', 'default',
    'help'))
CONFIG_OPTIONS = ConfigOption('default_page_size', 100,
    """
        Default page size for the table view
    """.strip()
    ), ConfigOption('max_returned_rows', 1000,
    """
        Maximum rows that can be returned from a table or custom query
    """
    .strip()), ConfigOption('num_sql_threads', 3,
    """
        Number of threads in the thread pool for executing SQLite queries
    """
    .strip()), ConfigOption('sql_time_limit_ms', 1000,
    """
        Time limit for a SQL query in milliseconds
    """.strip()
    ), ConfigOption('default_facet_size', 30,
    """
        Number of values to return for requested facets
    """.strip()
    ), ConfigOption('facet_time_limit_ms', 200,
    """
        Time limit for calculating a requested facet
    """.strip()
    ), ConfigOption('facet_suggest_time_limit_ms', 50,
    """
        Time limit for calculating a suggested facet
    """.strip()
    ), ConfigOption('allow_facet', True,
    """
        Allow users to specify columns to facet using ?_facet= parameter
    """
    .strip()), ConfigOption('allow_download', True,
    """
        Allow users to download the original SQLite database files
    """
    .strip()), ConfigOption('suggest_facets', True,
    """
        Calculate and display suggested facets
    """.strip()
    ), ConfigOption('allow_sql', True,
    """
        Allow arbitrary SQL queries via ?sql= parameter
    """.strip()
    ), ConfigOption('default_cache_ttl', 365 * 24 * 60 * 60,
    """
        Default HTTP cache TTL (used in Cache-Control: max-age= header)
    """
    .strip()), ConfigOption('cache_size_kb', 0,
    """
        SQLite cache size in KB (0 == use SQLite default)
    """.
    strip()), ConfigOption('allow_csv_stream', True,
    """
        Allow .csv?_stream=1 to download all rows (ignoring max_returned_rows)
    """
    .strip()), ConfigOption('max_csv_mb', 100,
    """
        Maximum size allowed for CSV export in MB - set 0 to disable this limit
    """
    .strip()), ConfigOption('truncate_cells_html', 2048,
    """
        Truncate cells longer than this in HTML table view - set 0 to disable
    """
    .strip()), ConfigOption('force_https_urls', False,
    """
        Force URLs in API output to always use https:// protocol
    """
    .strip())
DEFAULT_CONFIG = {option.name: option.default for option in CONFIG_OPTIONS}
async def favicon(request):...
return response.text('')
