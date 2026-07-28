def get_pct_checked_numeric(self):...
count = self.get_datadocument_count()
pct = 0 if count == 0 else self.get_qa_complete_extractedtext_count(
    ) / count * 100
return pct
