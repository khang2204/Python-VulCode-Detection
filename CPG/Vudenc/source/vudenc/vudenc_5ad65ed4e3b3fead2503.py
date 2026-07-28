import os
import re
import shutil
from subprocess import check_call, CalledProcessError, DEVNULL
import tempfile
from coalib.bears.Bear import Bear
from coalib.misc.Decorators import enforce_signature
from coalib.misc.Shell import escape_path_argument, run_shell_command
from coalib.results.Diff import Diff
from coalib.results.Result import Result
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY
"""
    Deals with the creation of linting bears.

    For the tutorial see:
    http://coala.readthedocs.org/en/latest/Users/Tutorials/Linter_Bears.html

    :param executable:                  The executable to run the linter.
    :param prerequisite_command:        The command to run as a prerequisite
                                        and is of type ``list``.
    :param prerequisites_fail_msg:      The message to be displayed if the
                                        prerequisite fails.
    :param arguments:                   The arguments to supply to the linter,
                                        such that the file name to be analyzed
                                        can be appended to the end. Note that
                                        we use ``.format()`` on the arguments -
                                        so, ``{abc}`` needs to be given as
                                        ``{{abc}}``. Currently, the following
                                        will be replaced:

                                         - ``{filename}`` - The filename passed
                                           to ``lint()``
                                         - ``{config_file}`` - The config file
                                           created using ``config_file()``

    :param output_regex:    The regex which will match the output of the linter
                            to get results. This is not used if
                            ``gives_corrected`` is set. This regex should give
                            out the following variables:

                             - line - The line where the issue starts.
                             - column - The column where the issue starts.
                             - end_line - The line where the issue ends.
                             - end_column - The column where the issue ends.
                             - severity - The severity of the issue.
                             - message - The message of the result.
                             - origin - The origin of the issue.

    :param diff_severity:   The severity to use for all results if
                            ``gives_corrected`` is set.
    :param diff_message:    The message to use for all results if
                            ``gives_corrected`` is set.
    :param use_stderr:      Uses stderr as the output stream is it's True.
    :param use_stdin:       Sends file as stdin instead of giving the file name.
    :param gives_corrected: True if the executable gives the corrected file
                            or just the issues.
    :param severity_map:    A dict where the keys are the possible severity
                            values the Linter gives out and the values are the
                            severity of the coala Result to set it to. If it is
                            not a dict, it is ignored.
    """
executable = None
prerequisite_command = None
prerequisite_fail_msg = 'Unknown failure.'
arguments = ''
output_regex = re.compile(
    '(?P<line>\\d+)\\.(?P<column>\\d+)\\|(?P<severity>\\d+): (?P<message>.*)')
diff_message = 'No result message was set'
diff_severity = RESULT_SEVERITY.NORMAL
use_stderr = False
use_stdin = False
gives_corrected = False
severity_map = None
def lint(self, filename=None, file=None):...
"""docstring"""
assert self.use_stdin and file is not None or not self.use_stdin and filename is not None
config_file = self.generate_config_file()
self.command = self._create_command(filename=filename, config_file=config_file)
stdin_input = ''.join(file) if self.use_stdin else None
stdout_output, stderr_output = run_shell_command(self.command, stdin=
    stdin_input)
self.stdout_output = tuple(stdout_output.splitlines(keepends=True))
self.stderr_output = tuple(stderr_output.splitlines(keepends=True))
results_output = self.stderr_output if self.use_stderr else self.stdout_output
results = self.process_output(results_output, filename, file)
if not self.use_stderr:
self._print_errors(self.stderr_output)
if config_file:
os.remove(config_file)
return results
