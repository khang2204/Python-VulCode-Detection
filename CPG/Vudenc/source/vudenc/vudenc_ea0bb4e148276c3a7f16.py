def test_long_qa_notes(self):...
self.objects.extext.qa_edited = True
note = QANotes.objects.create(extracted_text=self.objects.extext)
self.assertEqual(note.qa_notes, None)
note.qa_notes = 'A short QA note'
note.clean()
template = """An exception of type {0} occurred. Arguments:
{1!r}"""
long_note = 'A long QA note' * 200
message = template.format(type(ex).__name__, ex.args)
note.qa_notes = long_note
note.clean()
template = """An exception of type {0} occurred. Arguments:
{1!r}"""
message = template.format(type(ex).__name__, ex.args)
