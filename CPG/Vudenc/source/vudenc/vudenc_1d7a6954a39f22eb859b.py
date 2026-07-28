def add_parlai_data_path(self, argument_group=None):...
if argument_group is None:
argument_group = self
default_data_path = os.path.join(self.parlai_home, 'data')
argument_group.add_argument('-dp', '--datapath', default=default_data_path,
    help='path to datasets, defaults to {parlai_dir}/data')
