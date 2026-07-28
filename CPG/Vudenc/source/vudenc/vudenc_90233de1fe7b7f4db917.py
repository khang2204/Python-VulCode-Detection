def build_history_info(nzo, storage='', downpath='', postproc_time=0,...
"""docstring"""
if not downpath:
downpath = nzo.downpath
path = decode_factory(downpath)
storage = decode_factory(storage)
script_line = decode_factory(script_line)
flagRepair, flagUnpack, flagDelete = nzo.repair_opts
nzo_info = decode_factory(nzo.nzo_info)
url = decode_factory(nzo.url)
completed = int(time.time())
name = decode_factory(nzo.final_name)
nzb_name = decode_factory(nzo.filename)
category = decode_factory(nzo.cat)
pp = _PP_LOOKUP.get(sabnzbd.opts_to_pp(flagRepair, flagUnpack, flagDelete), 'X'
    )
script = decode_factory(nzo.script)
status = decode_factory(nzo.status)
nzo_id = nzo.nzo_id
bytes = nzo.bytes_downloaded
if script_output:
script_log = sqlite3.Binary(zlib.compress(script_output))
script_log = ''
download_time = decode_factory(nzo_info.get('download_time', 0))
downloaded = nzo.bytes_downloaded
completeness = 0
fail_message = decode_factory(nzo.fail_msg)
url_info = nzo_info.get('details', '') or nzo_info.get('more_info', '')
stages = decode_factory(nzo.unpack_info)
lines = []
for key, results in stages.iteritems():
lines.append('%s:::%s' % (key, ';'.join(results)))
stage_log = '\r\n'.join(lines)
report = 'future' if nzo.futuretype else ''
series = u''
if postproc_time:
seriesname, season, episode, dummy = sabnzbd.newsunpack.analyse_show(nzo.
    final_name)
password = ''
if seriesname and season and episode:
passwords = get_all_passwords(nzo)
series = u'%s/%s/%s' % (seriesname.lower(), season, episode)
if passwords:
password = passwords[0]
return completed, name, nzb_name, category, pp, script, report, url, status, nzo_id, storage, path, script_log, script_line, download_time, postproc_time, stage_log, downloaded, completeness, fail_message, url_info, bytes, series, nzo.md5sum, password
