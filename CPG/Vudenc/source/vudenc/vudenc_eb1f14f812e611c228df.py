def __init__(self, *args, **kwargs):...
super(ExtractedChemicalForm, self).__init__(*args, **kwargs)
if hasattr(self.instance, 'dsstox') and self.instance.dsstox is not None:
self.fields['true_cas'] = forms.CharField(max_length=200)
self.fields['true_cas'].initial = self.instance.dsstox.true_cas
self.fields['true_cas'].disabled = True
self.fields['true_chemname'] = forms.CharField(max_length=400)
self.fields['true_chemname'].initial = self.instance.dsstox.true_chemname
self.fields['true_chemname'].disabled = True
self.fields['SID'] = forms.CharField(max_length=50)
self.fields['SID'].initial = self.instance.dsstox.sid
self.fields['SID'].disabled = True
