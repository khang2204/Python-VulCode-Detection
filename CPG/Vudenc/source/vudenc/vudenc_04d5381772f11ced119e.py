""" Main module for the benchmark. It reads the command line arguments, reads the benchmark configuration, 
determines the runtime mode (dynamic vs. static); if dynamic, gets the benchmark data from the server,
runs the benchmarks, and records the timer results. """
import argparse
import time
import csv
import logging
import sys
import shutil
from benchmark import config, data_service
def get_cli_arguments():...
"""docstring"""
logging.debug('Getting cli arguments')
parser = argparse.ArgumentParser(description=
    'A benchmark for genomics routines in Python.')
subparser = parser.add_subparsers(title='commands', dest='command')
subparser.required = True
config_parser = subparser.add_parser('config', help=
    'Setting up the default configuration of the benchmark. It creates the default configuration file.'
    )
config_parser.add_argument('--output_config', type=str, required=True, help
    ='Specify the output path to a configuration file.', metavar='FILEPATH')
config_parser.add_argument('-f', action='store_true', help=
    'Overwrite the destination file if it already exists.')
data_setup_parser = subparser.add_parser('setup', help=
    'Preparation and setting up of the data for the benchmark. It requires a configuration file.'
    )
data_setup_parser.add_argument('--config_file', required=True, help=
    'Location of the configuration file', metavar='FILEPATH')
benchmark_exec_parser = subparser.add_parser('exec', help=
    'Execution of the benchmark modes. It requires a configuration file.')
benchmark_exec_parser.add_argument('--label', type=str, default='run',
    metavar='RUN_LABEL', help='Label for the benchmark run.')
benchmark_exec_parser.add_argument('--config_file', type=str, required=True,
    help='Specify the path to a configuration file.', metavar='FILEPATH')
runtime_configuration = vars(parser.parse_args())
return runtime_configuration
