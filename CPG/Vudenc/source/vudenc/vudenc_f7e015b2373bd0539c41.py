def test_qa_script_without_ext_text(self):...
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"/qa/extractionscript/15/'> Begin QA".encode(), response.content
    )
pk = 9
response = self.client.get(f'/qa/extractionscript/{pk}/', follow=True)
self.assertEqual(response.status_code, 200)
