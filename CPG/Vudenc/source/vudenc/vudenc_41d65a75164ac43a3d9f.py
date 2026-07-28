def indexing(self):...
obj = ExtractedChemicalIndex(meta={'id': self.id}, chem_name=self.
    raw_chem_name, raw_cas=self.raw_cas, raw_chem_name=self.raw_chem_name,
    facet_model_name='Extracted Chemical')
obj.save()
return obj.to_dict(include_meta=True)
