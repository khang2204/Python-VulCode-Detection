@receiver(models.signals.post_delete, sender=DataGroup)...
"""docstring"""
dg_folder = instance.get_dg_folder()
if os.path.isdir(dg_folder):
shutil.rmtree(dg_folder)
