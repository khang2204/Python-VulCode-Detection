def main():...
import time
import os
data = CloudConnection()
data.__dict__ = {'type': 's3', 'region': os.environ['MOTUZ_REGION'],
    'access_key_id': os.environ['MOTUZ_ACCESS_KEY_ID'], 'secret_access_key':
    os.environ['MOTUZ_SECRET_ACCESS_KEY']}
connection = RcloneConnection()
job_id = 123
import random
connection.copy(src_data=None, src_path='/tmp/motuz/mb_blob.bin', dst_data=
    data, dst_path='/fh-ctr-mofuz-test/hello/world/{}'.format(random.
    randint(10, 10000)), job_id=job_id)
while not connection.copy_finished(job_id):
print(connection.copy_percent(job_id))
time.sleep(0.1)
