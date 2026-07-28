@staticmethod...
instance = kwargs.get('instance')
previous_raw_cas = instance.tracker.previous('raw_cas')
previous_raw_chem_name = instance.tracker.previous('raw_chem_name')
if instance.tracker.has_changed('raw_cas') or instance.tracker.has_changed(
instance.dsstox = None
