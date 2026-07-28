def check_source_management(self):...
print_header('SOURCES MANAGEMENT')
DIR = os.path.join(self.path, 'sources')
if os.path.exists(os.path.join(self.path, 'sources')) and len([name for
print_warning(
    """[YEP-3.3] Upstream app sources shouldn't be stored in this 'sources' folder of this git repository as a copy/paste
During installation, the package should download sources from upstream via 'ynh_setup_source'.
See the helper documentation. Original discussion happened here : https://github.com/YunoHost/issues/issues/201#issuecomment-391549262"""
    )
