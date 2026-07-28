def test_extracted_text_qa_notes(self):...
self.objects.extext.qa_edited = True
note = QANotes.objects.create(extracted_text=self.objects.extext)
self.assertEqual(note.qa_notes, None)
self.assertRaises(ValidationError, note.clean)
