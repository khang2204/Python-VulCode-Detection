def add_model_args(self):...
"""docstring"""
model_args = self.add_argument_group('ParlAI Model Arguments')
model_args.add_argument('-m', '--model', default=None, help=
    'the model class name. can match parlai/agents/<model> for agents in that directory, or can provide a fully specified module for `from X import Y` via `-m X:Y` (e.g. `-m parlai.agents.seq2seq.seq2seq:Seq2SeqAgent`)'
    )
model_args.add_argument('-mf', '--model-file', default=None, help=
    'model file name for loading and saving models')
model_args.add_argument('--dict-class', help=
    'the class of the dictionary agent uses')
