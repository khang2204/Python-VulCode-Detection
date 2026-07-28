@property...
if hasattr(self, 'curated_chemical') and self.curated_chemical is not None:
return self.curated_chemical.sid
return None
