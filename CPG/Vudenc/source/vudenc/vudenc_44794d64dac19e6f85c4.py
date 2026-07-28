def update_local_scheduler_map(self):...
local_schedulers = self.state.client_table()
self.local_scheduler_id_to_ip_map = {}
for local_scheduler_info in local_schedulers:
client_id = local_scheduler_info.get('DBClientID') or local_scheduler_info[
    'ClientID']
ip_address = (local_scheduler_info.get('AuxAddress') or
    local_scheduler_info['NodeManagerAddress']).split(':')[0]
self.local_scheduler_id_to_ip_map[client_id] = ip_address
