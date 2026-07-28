def test_autocommit(self):...
self.assertEqual(self.cnxn.autocommit, False)
othercnxn = pyodbc.connect(self.connection_string, autocommit=True)
self.assertEqual(othercnxn.autocommit, True)
othercnxn.autocommit = False
self.assertEqual(othercnxn.autocommit, False)
