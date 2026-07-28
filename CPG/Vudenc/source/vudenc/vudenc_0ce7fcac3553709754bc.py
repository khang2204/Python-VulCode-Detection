@defer.inlineCallbacks...
"""docstring"""
partial, rest, completions = yield completion.complete(self, self.
    lineBuffer, self.lineBufferIndex)
if len(completions) == 1:
space = '' if rest else ' '
if len(completions) > 1:
if self.lineBuffer[self.lineBufferIndex - len(partial) - 1] == '"':
common_prefix = os.path.commonprefix(completions)
space = '" '
if completions[0].endswith('='):
patch = common_prefix[len(partial):]
space = ''
patch = completions[0][len(partial):] + space
self.insert_text(patch)
self.insert_text(patch)
if not patch:
self.terminal.nextLine()
self.terminal.write(columnize(completions))
self.drawInputLine()
if len(rest):
self.terminal.cursorBackward(len(rest))
