def add_parlai_args(self, args=None):...
default_downloads_path = os.path.join(self.parlai_home, 'downloads')
parlai = self.add_argument_group('Main ParlAI Arguments')
parlai.add_argument('-t', '--task', help=
    'ParlAI task(s), e.g. "babi:Task1" or "babi,cbt"')
parlai.add_argument('--download-path', default=default_downloads_path, help
    =
    'path for non-data dependencies to store any needed files.defaults to {parlai_dir}/downloads'
    )
parlai.add_argument('-dt', '--datatype', default='train', choices=['train',
    'train:stream', 'train:ordered', 'train:ordered:stream',
    'train:stream:ordered', 'valid', 'valid:stream', 'test', 'test:stream'],
    help=
    'choose from: train, train:ordered, valid, test. to stream data add ":stream" to any option (e.g., train:stream). by default: train is random with replacement, valid is ordered, test is ordered.'
    )
parlai.add_argument('-im', '--image-mode', default='raw', type=str, help=
    'image preprocessor to use. default is "raw". set to "none" to skip image loading.'
    )
parlai.add_argument('-nt', '--numthreads', default=1, type=int, help=
    'number of threads. If batchsize set to 1, used for hogwild; otherwise, used for number of threads in threadpool loading, e.g. in vqa'
    )
parlai.add_argument('--hide-labels', default=False, type='bool', help=
    'default (False) moves labels in valid and test sets to the eval_labels field. If True, they are hidden completely.'
    )
batch = self.add_argument_group('Batching Arguments')
batch.add_argument('-bs', '--batchsize', default=1, type=int, help=
    'batch size for minibatch training schemes')
batch.add_argument('-bsrt', '--batch-sort', default=True, type='bool', help
    =
    'If enabled (default True), create batches by flattening all episodes to have exactly one utterance exchange and then sorting all the examples according to their length. This dramatically reduces the amount of padding present after examples have been parsed, speeding up training.'
    )
batch.add_argument('-clen', '--context-length', default=-1, type=int, help=
    'Number of past utterances to remember when building flattened batches of data in multi-example episodes.'
    )
batch.add_argument('-incl', '--include-labels', default=True, type='bool',
    help=
    'Specifies whether or not to include labels as past utterances when building flattened batches of data in multi-example episodes.'
    )
self.add_parlai_data_path(parlai)
