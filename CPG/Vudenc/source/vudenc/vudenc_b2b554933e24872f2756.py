def configfile(self, jsonpath):...
"""docstring"""
c = snakemake.io.load_configfile(jsonpath)
update_config(config, c)
update_config(config, self.overwrite_config)
