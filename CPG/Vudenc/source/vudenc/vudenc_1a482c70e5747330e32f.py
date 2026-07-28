ANSIBLE_METADATA = {'status': ['stableinterface'], 'supported_by':
    'community', 'version': '1.0'}
DOCUMENTATION = """
---
module: postgresql_setting
short_description: manage config settings for PostgreSQL instance.
description:
  - Change server configuration parameters across the entire database cluster
  - New values will be effective after the next server configuration reload,
    or after the next server restart in the case of parameters that can only
    be changed at server start
  - Only superusers can change configuration settings
author: "Kostiantyn Nemchenko (@kostiantyn-nemchenko)"
version_added: "2.3"
requirements:
  - psycopg2
options:
  login_user:
    description:
      - The username used to authenticate with
    required: false
    default: null
  login_password:
    description:
      - The password used to authenticate with
    required: false
    default: null
  login_host:
    description:
      - Host running the database
    required: false
    default: localhost
  login_unix_socket:
    description:
      - Path to a Unix domain socket for local connections
    required: false
    default: null
  port:
    description:
      - Database port to connect to.
    required: false
    default: 5432
  option:
    description:
      - The parameter from PostgreSQL configuration file
    required: true
    default: null
  value:
    description:
      - The value of the parameter to change
    required: false
    default: null
  state:
    description:
      - The parameter state
    required: false
    default: present
    choices: [ "present", "absent" ]
"""
EXAMPLES = """
# Set work_mem parameter to 8MB
- postgresql_setting:
    option: work_mem
    value: 8MB
    state: present

# Allow only local TCP/IP "loopback" connections to be made
- postgresql_setting:
    option: listen_addresses
    state: absent

# Enable autovacuum
- postgresql_setting:
    option: autovacuum
    value: on
"""
import psycopg2
postgresqldb_found = False
postgresqldb_found = True
import psycopg2.extras
from ansible.module_utils.six import iteritems
def option_ispreset(cursor, option):...
"""docstring"""
query = """
    SELECT EXISTS
        (SELECT 1
         FROM pg_settings
         WHERE context = 'internal'
           AND name = '%s')
    """
cursor.execute(query % option)
return cursor.fetchone()[0]
