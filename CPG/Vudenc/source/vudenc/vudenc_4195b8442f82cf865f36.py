def get_data_document(self):...
"""docstring"""
id = self.id
return apps.get_model('dashboard.ExtractedChemical').objects.get(rawchem_ptr=id
    ).data_document
return apps.get_model('dashboard.ExtractedFunctionalUse').objects.get(
    rawchem_ptr=id).data_document
return apps.get_model('dashboard.ExtractedListPresence').objects.get(
    rawchem_ptr=id).data_document
return False
