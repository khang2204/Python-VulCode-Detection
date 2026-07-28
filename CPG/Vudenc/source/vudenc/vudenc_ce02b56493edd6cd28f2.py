def init():...
if os.path.isfile(CFG('dbname')):
return
conn, c = connectDB()
c.execute('CREATE TABLE ' + CFG('poll_table_name') +
    '(                    name text,                    options text,                    has_tokens integer,                    show_results integer,                    question text,                    multi integer,                     date text)'
    )
c.execute('CREATE TABLE {}(name_option text, count integer)'.format(CFG(
    'options_table_name')))
c.execute('CREATE TABLE {}(token text, name text, options_selected text)'.
    format(CFG('tokens_table_name')))
c.execute('CREATE TABLE {}(adm_token text, poll_name text)'.format(CFG(
    'admintoken_table_name')))
closeDB(conn)
