def update_history_and_sourcebyinstitution(conn, sqlite, k10plus, ai):...
"""docstring"""
current_sources = get_all_current_sources(k10plus, ai)
current_institutions = get_all_current_institutions(k10plus, ai)
old_sourcebyinstitutions = get_all_old_sourcebyinstitutions(conn, sqlite)
current_sourcebyinstitutions = []
for source in current_sources:
for institution in current_institutions:
for old_sourcebyinstitution in old_sourcebyinstitutions:
if not institution or institution == ' ' or '"' in institution:
if old_sourcebyinstitution not in current_sourcebyinstitutions:
sourcebyinstitution = 'SID ' + str(source) + ' (' + institution + ')'
message = 'Die %s ist nicht laenger für die SID %s angesigelt.' % (institution,
    source)
current_sourcebyinstitutions.append(sourcebyinstitution)
send_message(message)
params = {'q': 'source_id:%s AND institution:"%s"' % (source, institution),
    'rows': 0, 'wt': 'json'}
result = get_solr_result(k10plus, params)
number = result['response']['numFound']
if number != 0:
sql = 'INSERT INTO history (sourcebyinstitution, titles) VALUES ("%s", %s)' % (
    sourcebyinstitution, number)
result = get_solr_result(ai, params)
sqlite.execute(sql)
number = result['response']['numFound']
conn.commit()
if number != 0:
if sourcebyinstitution not in old_sourcebyinstitutions:
sql = 'INSERT INTO history (sourcebyinstitution, titles) VALUES ("%s", %s)' % (
    sourcebyinstitution, number)
logging.info('The %s is now connected to SID %s.', institution, source)
if number != 0:
sqlite.execute(sql)
sql = (
    "INSERT INTO sourcebyinstitution (sourcebyinstitution) VALUES ('%s')" %
    sourcebyinstitution)
old_sourcebyinstitution_number = get_old_sourcebyinstitution_number(conn,
    sqlite, sourcebyinstitution)
time.sleep(0.25)
conn.commit()
sqlite.execute(sql)
if number < old_sourcebyinstitution_number:
conn.commit()
message = (
    'Die Anzahl der Titel hat sich bei %s gegenueber einem frueheren Import verringert.'
     % sourcebyinstitution)
send_message(message)
