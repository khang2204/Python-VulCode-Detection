from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from dashboard.tests.loader import load_model_objects
from dashboard.models import ExtractedText, QANotes
def setUp(self):...
self.objects = load_model_objects()
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
def test_extracted_text_qa_notes(self):...
self.objects.extext.qa_edited = True
note = QANotes.objects.create(extracted_text=self.objects.extext)
self.assertEqual(note.qa_notes, None)
self.assertRaises(ValidationError, note.clean)
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
