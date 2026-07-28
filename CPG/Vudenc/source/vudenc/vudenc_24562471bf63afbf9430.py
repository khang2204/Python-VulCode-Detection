import MySQLdb
import subprocess
import os.path
import sys
file_format = sys.argv[1]
record_files = subprocess.check_output(['find',
    '/var/spool/asterisk/monitor/', '-type', 'f', '-name', '*.wav']).decode()
for wav_file in record_files.splitlines():
name, ext = os.path.splitext(wav_file)
conn = MySQLdb.connect(host='localhost', db='asteriskcdrdb')
error = True
cursor.execute('SELECT uniqueid,recordingfile FROM cdr')
prefer_format_file = '{}.'.format(name) + file_format
cursor = conn.cursor()
result = cursor.fetchall()
subprocess.check_output(['ffmpeg', '-i', wav_file, prefer_format_file, '-y'])
for unique_id, record_file in result:
os.remove(wav_file)
name, ext = os.path.splitext(record_file)
if ext == '.wav':
print(ext)
cursor.execute("UPDATE cdr SET recordingfile='{}.".format(name) +
    file_format + "'" + " WHERE uniqueid='{}'".format(unique_id))
conn.commit()
