def test_timer(self):...
t = Timer()
time.sleep(0.001)
t.mark('thing1')
time.sleep(0.001)
t.mark('thing2')
snapshot = t.finish()
time.sleep(0.001)
t.mark('thing1')
time.sleep(0.001)
t.mark('thing2')
snapshot_2 = t.finish()
assert snapshot['marks_ms'].keys() == snapshot_2['marks_ms'].keys()
assert snapshot['marks_ms']['thing1'] < snapshot_2['marks_ms']['thing1']
assert snapshot['marks_ms']['thing2'] < snapshot_2['marks_ms']['thing2']
