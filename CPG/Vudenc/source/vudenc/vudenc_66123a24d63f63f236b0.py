def cleanup(self):...
"""docstring"""
to_remove = [f for f in self.expanded_output if f.exists]
if to_remove:
logger.info(
    """Removing output files of failed job {} since they might be corrupted:
{}"""
    .format(self, ', '.join(to_remove)))
for f in to_remove:
f.remove()
