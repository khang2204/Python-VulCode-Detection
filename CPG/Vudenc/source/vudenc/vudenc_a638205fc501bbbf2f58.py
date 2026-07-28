def add_mturk_args(self):...
mturk = self.add_argument_group('Mechanical Turk')
default_log_path = os.path.join(self.parlai_home, 'logs', 'mturk')
mturk.add_argument('--mturk-log-path', default=default_log_path, help=
    'path to MTurk logs, defaults to {parlai_dir}/logs/mturk')
mturk.add_argument('-t', '--task', help=
    'MTurk task, e.g. "qa_data_collection" or "model_evaluator"')
mturk.add_argument('-nc', '--num-conversations', default=1, type=int, help=
    'number of conversations you want to create for this task')
mturk.add_argument('--unique', dest='unique_worker', default=False, action=
    'store_true', help='enforce that no worker can work on your task twice')
mturk.add_argument('--unique-qual-name', dest='unique_qual_name', default=
    None, type=str, help=
    'qualification name to use for uniqueness between HITs')
mturk.add_argument('-r', '--reward', default=0.05, type=float, help=
    'reward for each worker for finishing the conversation, in US dollars')
mturk.add_argument('--sandbox', dest='is_sandbox', action='store_true',
    help='submit the HITs to MTurk sandbox site')
mturk.add_argument('--live', dest='is_sandbox', action='store_false', help=
    'submit the HITs to MTurk live site')
mturk.add_argument('--debug', dest='is_debug', action='store_true', help=
    'print and log all server interactions and messages')
mturk.add_argument('--verbose', dest='verbose', action='store_true', help=
    'print all messages sent to and from Turkers')
mturk.add_argument('--hard-block', dest='hard_block', action='store_true',
    default=False, help=
    'Hard block disconnecting Turkers from all of your HITs')
mturk.add_argument('--log-level', dest='log_level', type=int, default=20,
    help=
    'importance level for what to put into the logs. the lower the level the more that gets logged. values are 0-50'
    )
mturk.add_argument('--block-qualification', dest='block_qualification',
    default='', help=
    'Qualification to use for soft blocking users. By default turkers are never blocked, though setting this will allow you to filter out turkers that have disconnected too many times on previous HITs where this qualification was set.'
    )
mturk.add_argument('--count-complete', dest='count_complete', default=False,
    action='store_true', help=
    'continue until the requested number of conversations are completed rather than attempted'
    )
mturk.add_argument('--allowed-conversations', dest='allowed_conversations',
    default=0, type=int, help=
    'number of concurrent conversations that one mturk worker is able to be involved in, 0 is unlimited'
    )
mturk.add_argument('--max-connections', dest='max_connections', default=30,
    type=int, help=
    'number of HITs that can be launched at the same time, 0 is unlimited.')
mturk.add_argument('--min-messages', dest='min_messages', default=0, type=
    int, help=
    'number of messages required to be sent by MTurk agent when considering whether to approve a HIT in the event of a partner disconnect. I.e. if the number of messages exceeds this number, the turker can submit the HIT.'
    )
mturk.add_argument('--local', dest='local', default=False, action=
    'store_true', help=
    'Run the server locally on this server rather than setting up a heroku server.'
    )
mturk.set_defaults(is_sandbox=True)
mturk.set_defaults(is_debug=False)
mturk.set_defaults(verbose=False)
