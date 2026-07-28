def add_messenger_args(self):...
messenger = self.add_argument_group('Facebook Messenger')
messenger.add_argument('--debug', dest='is_debug', action='store_true',
    help='print and log all server interactions and messages')
messenger.add_argument('--verbose', dest='verbose', action='store_true',
    help='print all messages sent to and from Turkers')
messenger.add_argument('--log-level', dest='log_level', type=int, default=
    20, help=
    'importance level for what to put into the logs. the lower the level the more that gets logged. values are 0-50'
    )
messenger.add_argument('--force-page-token', dest='force_page_token',
    action='store_true', help=
    'override the page token stored in the cache for a new one')
messenger.add_argument('--password', dest='password', type=str, default=
    None, help='Require a password for entry to the bot')
messenger.add_argument('--local', dest='local', action='store_true',
    default=False, help=
    'Run the server locally on this server rather than setting up a heroku server.'
    )
messenger.set_defaults(is_debug=False)
messenger.set_defaults(verbose=False)
