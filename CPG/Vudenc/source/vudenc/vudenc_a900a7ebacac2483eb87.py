from django.test import Client
from dashboard.tests.loader import *
from django.test import TestCase, override_settings, RequestFactory
from dashboard.models import DataDocument, Script, ExtractedText, ExtractedChemical, QAGroup
from django.db.models import Count
fixtures = fixtures_standard
def setUp(self):...
self.factory = RequestFactory()
self.client.login(username='Karyn', password='specialP@55word')
def test_qa_begin(self):...
"""docstring"""
self.assertFalse(Script.objects.get(pk=5).qa_begun,
    'The Script should have qa_begun of False at the beginning')
response = self.client.get('/qa/extractionscript/5/')
self.assertTrue(Script.objects.get(pk=5).qa_begun,
    'qa_begun should now be true')
def test_new_qa_group_urls(self):...
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"/qa/extractionscript/15/'> Begin QA".encode(), response.content
    )
pk = 15
response = self.client.get(f'/qa/extractionscript/{pk}/')
et = ExtractedText.objects.filter(extraction_script=pk).first()
self.assertIn(f'/qa/extractedtext/{et.pk}/'.encode(), response.content)
group_count = QAGroup.objects.filter(extraction_script_id=pk).count()
self.assertTrue(group_count == 1)
self.assertTrue(Script.objects.get(pk=15).qa_begun)
group_pk = QAGroup.objects.get(extraction_script_id=pk).pk
et = ExtractedText.objects.filter(extraction_script=pk).first()
self.assertTrue(et.qa_group_id == group_pk)
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"'/qa/extractionscript/15/'> Continue QA".encode(), response
    .content)
def test_qa_script_without_ext_text(self):...
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"/qa/extractionscript/15/'> Begin QA".encode(), response.content
    )
pk = 9
response = self.client.get(f'/qa/extractionscript/{pk}/', follow=True)
self.assertEqual(response.status_code, 200)
def test_data_document_qa(self):...
scr = Script.objects.annotate(num_ets=Count('extractedtext')).filter(
    num_ets__lt=100).filter(script_type='EX').first()
pk = ExtractedText.objects.filter(qa_group=None).filter(extraction_script=scr
    ).filter(data_document__data_group__group_type__code='CO').first().pk
response = self.client.get(f'/qa/extractedtext/{pk}/')
scr = ExtractedText.objects.get(pk=pk).extraction_script
group_count = QAGroup.objects.filter(extraction_script=scr).count()
self.assertTrue(group_count == 1)
self.assertTrue(scr.qa_begun)
new_group = QAGroup.objects.get(extraction_script=scr)
et = ExtractedText.objects.get(pk=pk)
self.assertTrue(et.qa_group == new_group)
response = self.client.get(f'/qa/extractionscript/')
self.assertIn(f"'/qa/extractionscript/{scr.pk}/'> Continue QA".encode(),
    response.content)
scr = Script.objects.annotate(num_ets=Count('extractedtext')).filter(
    num_ets__gt=100).first()
pk = ExtractedText.objects.filter(extraction_script=scr).first().pk
response = self.client.get(f'/qa/extractedtext/{pk}/')
scr = ExtractedText.objects.get(pk=pk).extraction_script
new_group = QAGroup.objects.get(extraction_script=scr)
initial_qa_count = ExtractedText.objects.filter(qa_group=new_group).count()
self.assertTrue(initial_qa_count > 100)
pk = ExtractedText.objects.filter(extraction_script_id=scr.id).filter(qa_group
    =None).first().pk
response = self.client.get(f'/qa/extractedtext/{pk}/')
self.assertGreater(ExtractedText.objects.filter(qa_group=new_group).count(),
    initial_qa_count)
def test_habitsandpractices(self):...
response = self.client.get(f'/habitsandpractices/54/')
self.assertContains(response, '<b>Add New Habit and Practice</b>')
def test_dd_link(self):...
response = self.client.get('/qa/extractedtext/5', follow=True)
self.assertIn(b'/datadocument/5', response.content)
def test_approval(self):...
response = self.client.get('/qa/extractionscript/5', follow=True)
response = self.client.get('/qa/extractedtext/7', follow=True)
def test_hidden_fields(self):...
"""docstring"""
response = self.client.get('/qa/extractionscript/15/', follow=True)
response = self.client.get('/qa/extractedtext/5/', follow=True)
self.assertIn(b'<input type="text" name="rawchem-1-raw_cas"', response.content)
self.assertNotIn(b'<input type="text" name="rawchem-1-unit_type"', response
    .content)
self.assertIn(b'Functional Use Chem1', response.content)
response = self.client.get('/qa/extractionscript/5', follow=True)
response = self.client.get('/qa/extractedtext/7/', follow=True)
self.assertIn(b'rawchem-1-unit_type', response.content)
def test_cpcat_qa(self):...
response = self.client.get(f'/qa/chemicalpresence/')
self.assertIn(f"/qa/chemicalpresencegroup/49/'> View Chemical Presence Lists"
    .encode(), response.content)
response = self.client.get(f'/qa/chemicalpresencegroup/49', follow=True)
self.assertIn(f'/qa/extractedtext/254781/"> Begin QA'.encode(), response.
    content)
elps = ExtractedListPresence.objects.filter(extracted_text__data_document_id
    =254781)
self.assertEqual(elps.filter(qa_flag=True).count(), 0)
response = self.client.get(f'/qa/extractedtext/254781/', follow=True)
elps = ExtractedListPresence.objects.filter(extracted_text__data_document_id
    =254781)
self.assertEqual(elps.filter(qa_flag=True).count(), 30)
elp_flagged = elps.filter(qa_flag=True).first()
self.assertIn(elp_flagged.raw_cas.encode(), response.content)
elp_not_flagged = elps.filter(qa_flag=False).first()
self.assertNotIn(elp_not_flagged.raw_cas.encode(), response.content)
def test_every_extractedtext_qa(self):...
for et in ExtractedText.objects.all():
response = self.client.get(f'/qa/extractedtext/%s' % et.data_document_id,
    follow=True)
if response.status_code != 200:
print(et.data_document_id)
self.assertEqual(response.status_code, 200)
