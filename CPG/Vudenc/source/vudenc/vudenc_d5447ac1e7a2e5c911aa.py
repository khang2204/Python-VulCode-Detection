def test_extracted_doc_date_validation(self):...
text = ExtractedText(doc_date='Wednesday, January 21, 2014', data_document=
    self.objects.doc, extraction_script=self.objects.script)
self.assertRaises(ValidationError, text.clean())
text = ExtractedText(doc_date='January 1984', data_document=self.objects.
    doc, extraction_script=self.objects.script)
text.clean()
self.fail('clean() raised ExceptionType unexpectedly!')
text = ExtractedText(data_document=self.objects.doc, extraction_script=self
    .objects.script)
text.clean()
self.fail('clean() raised ExceptionType unexpectedly!')
