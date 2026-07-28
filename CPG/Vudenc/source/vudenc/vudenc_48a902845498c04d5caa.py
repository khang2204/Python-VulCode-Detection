@memoized_method...
buildroot = get_buildroot()
return scheduler.capture_snapshots((PathGlobsAndRoot(PathGlobs(tuple(
    fast_relpath(a, buildroot) for a in (self.zinc, self.compiler_bridge,
    self.compiler_interface))), buildroot),))[0]
