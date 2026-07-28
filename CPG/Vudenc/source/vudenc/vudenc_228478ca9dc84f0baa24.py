from lxml import html
from django.test import Client
from django.urls import reverse
from django.test import TestCase, override_settings
from django.core.exceptions import ObjectDoesNotExist
from dashboard.forms import *
from factotum.settings import EXTRA
from dashboard.tests.loader import *
fixtures = fixtures_standard
def setUp(self):...
self.client.login(username='Karyn', password='specialP@55word')
def test_absent_extracted_text(self):...
for dd in DataDocument.objects.all():
ddid = dd.id
def test_script_links(self):...
resp = self.client.get('/datadocument/%s/' % ddid)
doc = DataDocument.objects.first()
self.assertEqual(resp.status_code, 200,
    'The page must return a 200 status code')
response = self.client.get(f'/datadocument/179486/')
extracted_text = ExtractedText.objects.get(data_document=dd)
self.assertContains(resp, 'No Extracted Text exists for this Data Document')
self.assertContains(resp, '<h4>Extracted Text')
self.assertIn('Download Script', response.content.decode('utf-8'))
self.assertIn('Extraction Script', response.content.decode('utf-8'))
def test_product_card_location(self):...
response = self.client.get('/datadocument/179486/')
html = response.content.decode('utf-8')
e_idx = html.index('<h4>Extracted Text')
p_idx = html.index('<h4 class="d-inline">Products')
self.assertTrue(p_idx > e_idx,
    'Product card should come after Extracted Text card')
def test_product_create_link(self):...
response = self.client.get('/datadocument/167497/')
self.assertContains(response, '/link_product_form/167497/')
data = {'title': ['New Product'], 'upc': ['stub_1860'], 'document_type': [1
    ], 'return_url': ['/datadocument/167497/']}
response = self.client.post('/link_product_form/167497/', data=data)
self.assertRedirects(response, '/datadocument/167497/')
response = self.client.get(response.url)
self.assertContains(response, 'New Product')
def test_product_title_duplication(self):...
response = self.client.get('/datadocument/245401/')
self.assertContains(response, '/link_product_form/245401/')
data = {'title': ['Product Title'], 'upc': ['stub_9100'], 'document_type':
    [1], 'return_url': ['/datadocument/245401/']}
response = self.client.post('/link_product_form/245401/', data=data)
self.assertRedirects(response, '/datadocument/245401/')
response = self.client.get(response.url)
new_product = Product.objects.get(upc='stub_9100')
self.assertContains(response, f'product/%s' % new_product.id)
data = {'title': ['Product Title'], 'upc': ['stub_9101'], 'document_type':
    [1], 'return_url': ['/datadocument/245401/']}
response = self.client.post('/link_product_form/245401/', data=data)
self.assertRedirects(response, '/datadocument/245401/')
response = self.client.get(response.url)
new_product = Product.objects.get(upc='stub_9101')
self.assertContains(response, f'product/%s' % new_product.id)
def test_add_extracted(self):...
"""docstring"""
doc = DataDocument.objects.get(pk=354784)
self.assertFalse(doc.extracted, 'This document is matched but not extracted')
data = {'hhe_report_number': ['47']}
response = self.client.post('/extractedtext/edit/354784/', data=data,
    follow=True)
doc = DataDocument.objects.get(pk=354784)
self.assertTrue(doc.extracted, 'This document is not extracted ')
page = html.fromstring(response.content)
hhe_no = page.xpath('//dd[contains(@class, "hh-report-no")]')[0].text
self.assertIn('47', hhe_no)
fixtures = fixtures_standard
def setUp(self):...
self.client.login(username='Karyn', password='specialP@55word')
def test_fetch_extracted_records(self):...
"""docstring"""
for et in ExtractedText.objects.all():
for ex_child in et.fetch_extracted_records():
def test_extractedsubclasses(self):...
child_model = ex_child.__class__
"""docstring"""
self.assertEqual(et.pk, child_model.objects.get(pk=ex_child.pk).
    extracted_text.pk,
    'The ExtractedChemical object with the returned child pk should have the correct extracted_text parent'
    )
for doc in DataDocument.objects.all():
def test_every_extractedtext(self):...
extsub = ExtractedText.objects.get_subclass(data_document=doc)
"""docstring"""
if doc.data_group.group_type.code == 'CP':
for et in ExtractedText.objects.all():
self.assertEqual(type(extsub), ExtractedCPCat)
if doc.data_group.group_type.code == 'HH':
dd = et.data_document
def test_curated_chemical(self):...
self.assertEqual(type(extsub), ExtractedHHDoc)
self.assertEqual(type(extsub), ExtractedText)
ParentForm, ChildForm = create_detail_formset(dd, EXTRA)
"""docstring"""
extracted_text_form = ParentForm(instance=et)
for et in ExtractedText.objects.all():
child_formset = ChildForm(instance=et)
dd = et.data_document
def test_num_forms(self):...
dd_child_model = get_extracted_models(dd.data_group.group_type.code)[1]
ParentForm, ChildForm = create_detail_formset(dd)
"""docstring"""
childform_model = child_formset.__dict__.get('queryset').__dict__.get('model')
child_formset = ChildForm(instance=et)
group_models = {'CO': ExtractedChemical, 'FU': ExtractedFunctionalUse, 'HP':
    ExtractedHabitsAndPractices, 'CP': ExtractedListPresence, 'HH':
    ExtractedHHRec}
self.assertEqual(dd_child_model, childform_model)
for form in child_formset.forms:
for code, model in group_models.items():
if dd.data_group.type in ['CO', 'UN']:
if DataDocument.objects.filter(document_type__group_type__code=code,
ec = form.instance
self.assertFalse('true_cas' in form.fields)
doc = DataDocument.objects.filter(document_type__group_type__code=code,
    extractedtext__isnull=False).first()
if ec.dsstox is not None:
response = self.client.get(reverse('data_document', kwargs={'pk': doc.pk}))
self.assertTrue('true_cas' in form.fields)
self.assertFalse('true_cas' in form.fields)
num_forms = response.context['detail_formset'].total_form_count()
self.assertTrue('SID' in form.fields)
self.assertFalse('SID' in form.fields)
children = model.objects.filter(extracted_text=doc.extractedtext).count()
if doc.detail_page_editable:
error = f'{model.__module__} should have one more forms than instances'
error = f'{model.__module__} should have the same number of forms as instances'
self.assertEqual(num_forms, children + 1, error)
self.assertEqual(num_forms, children, error)
