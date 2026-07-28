def test_maybe_profiled(self):...
profile_path = os.path.join(td, 'profile.prof')
for _ in range(5):
print('test')
self.assertTrue(os.path.exists(profile_path))
pstats.Stats(profile_path).print_stats()
