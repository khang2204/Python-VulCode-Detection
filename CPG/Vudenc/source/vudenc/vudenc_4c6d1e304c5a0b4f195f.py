def _secure_save_data(self):...
"""docstring"""
smb_conn = self._get_smb_connection()
if smb_conn and smb_conn.connect(SmbConfig.smb_ip, SmbConfig.smb_port):
config_obj = self.env['ir.config_parameter']
share_nas = config_obj.get_param('partner_compassion.share_on_nas')
store_path = config_obj.get_param('partner_compassion.store_path')
src_zip_file = tempfile.NamedTemporaryFile()
attrs = smb_conn.retrieveFile(share_nas, store_path, src_zip_file)
file_size = attrs[1]
if file_size:
src_zip_file.flush()
zip_dir = tempfile.mkdtemp()
pyminizip.uncompress(src_zip_file.name, SmbConfig.file_pw, zip_dir, 0)
csv_path = zip_dir + '/partner_data.csv'
csv_writer = csv.writer(csv_file)
csv_writer.writerow([str(self.id), self.ref, self.contact_address, fields.
    Date.today()])
dst_zip_file = tempfile.NamedTemporaryFile()
pyminizip.compress(csv_path, '', dst_zip_file.name, SmbConfig.file_pw, 5)
smb_conn.storeFile(share_nas, store_path, dst_zip_file)
logger.error(
    "Couldn't store secure partner data on NAS. Please do it manually by replicating the following file: "
     + dst_zip_file.name)
