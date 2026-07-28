def get_all_meta(self):...
"""docstring"""
return {key: self.get_safe_value(self.meta, key) for key in self.meta.iptc_keys
    }
