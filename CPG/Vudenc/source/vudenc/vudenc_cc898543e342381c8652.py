def test_filters(self):...
app = TestApp(main({}))
self.assertTrue('filtered response' in app.get('/filtered').body)
self.assertTrue('unfiltered' in app.post('/filtered').body)
