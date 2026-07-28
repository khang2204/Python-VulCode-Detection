def next_extracted_text_in_qa_group(self):...
nextid = 0
extextnext = get_next_or_prev(ExtractedText.objects.filter(qa_group=self.
    qa_group, qa_checked=False), self, 'next')
if extextnext:
nextid = extextnext.pk
if extextnext == self:
nextid = 0
return nextid
