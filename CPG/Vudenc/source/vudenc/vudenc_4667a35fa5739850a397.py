def xray_driver_removed_handler(self, unused_channel, data):...
"""docstring"""
gcs_entries = ray.gcs_utils.GcsTableEntry.GetRootAsGcsTableEntry(data, 0)
driver_data = gcs_entries.Entries(0)
message = ray.gcs_utils.DriverTableData.GetRootAsDriverTableData(driver_data, 0
    )
driver_id = message.DriverId()
logger.info('Monitor: XRay Driver {} has been removed.'.format(
    binary_to_hex(driver_id)))
self._xray_clean_up_entries_for_driver(driver_id)
