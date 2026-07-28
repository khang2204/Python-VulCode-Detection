def test_baseline_filter(self):...
issue_text = (
    'A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.'
    )
json = (
    """{
          "results": [
            {
              "code": "...",
              "filename": "%s/examples/flask_debug.py",
              "issue_confidence": "MEDIUM",
              "issue_severity": "HIGH",
              "issue_text": "%s",
              "line_number": 10,
              "line_range": [
                10
              ],
              "test_name": "flask_debug_true",
              "test_id": "B201"
            }
          ]
        }
        """
     % (os.getcwd(), issue_text))
self.b_mgr.populate_baseline(json)
self.run_example('flask_debug.py')
self.assertEqual(1, len(self.b_mgr.baseline))
self.assertEqual({}, self.b_mgr.get_issue_list())
