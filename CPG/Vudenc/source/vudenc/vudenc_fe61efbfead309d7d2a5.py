def create_qa_group(self, force_doc_id=None):...
"""docstring"""
from .qa_group import QAGroup
from .extracted_text import ExtractedText
es = self
if QAGroup.objects.filter(extraction_script=es).count() == 1:
return QAGroup.objects.get(extraction_script=es)
if QAGroup.objects.filter(extraction_script=es).count() > 1:
return QAGroup.objects.filter(extraction_script=es).first()
qa_group = QAGroup.objects.create(extraction_script=es)
doc_text_ids = list(ExtractedText.objects.filter(extraction_script=es,
    qa_checked=False).values_list('pk', flat=True))
if len(doc_text_ids) < 100 and len(doc_text_ids) > 0:
texts = ExtractedText.objects.filter(pk__in=doc_text_ids)
if len(doc_text_ids) >= 100:
if texts is not None:
random_20 = math.ceil(len(doc_text_ids) / 5)
texts = None
for text in texts:
if force_doc_id is not None and ExtractedText.objects.filter(pk=force_doc_id
shuffle(doc_text_ids)
text.qa_group = qa_group
text = ExtractedText.objects.get(pk=force_doc_id)
return qa_group
texts = ExtractedText.objects.filter(pk__in=doc_text_ids[:random_20])
text.save()
text.qa_group = qa_group
text.save()
