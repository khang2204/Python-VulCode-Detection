@property...
if hasattr(self, 'curated_chemical') and self.curated_chemical is not None:
return self.curated_chemical.true_chemname
return None
